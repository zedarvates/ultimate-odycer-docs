# SPDX-License-Identifier: MIT

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
BUILD_ROOT = (ROOT / "build").resolve()
BUILD_MANIFEST = "docs-build-manifest.json"
TOKEN_PATTERN = re.compile(r"[0-9A-Za-z][0-9A-Za-z._+-]{0,63}")
COMMIT_PATTERN = re.compile(r"[0-9a-f]{7,40}")


class BuildFailure(RuntimeError):
    """Raised when an offline documentation build violates its contract."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def resolve_output_directory(value: str | Path) -> Path:
    candidate = Path(value)
    if not candidate.is_absolute():
        candidate = ROOT / candidate
    resolved = candidate.resolve()
    try:
        relative = resolved.relative_to(BUILD_ROOT)
    except ValueError as error:
        raise BuildFailure("output directory must stay inside repository build/") from error
    if not relative.parts:
        raise BuildFailure("output directory must be a child inside repository build/")
    return resolved


def validate_token(value: str, label: str) -> str:
    if TOKEN_PATTERN.fullmatch(value) is None:
        raise BuildFailure(f"{label} must be a bounded filesystem-safe identifier")
    return value


def validate_source_commit(value: str) -> str:
    if COMMIT_PATTERN.fullmatch(value) is None:
        raise BuildFailure("source commit must be 7 to 40 lowercase hexadecimal characters")
    return value


def payload_files(site: Path) -> list[Path]:
    return sorted(
        (
            path
            for path in site.rglob("*")
            if path.is_file() and path.name != BUILD_MANIFEST
        ),
        key=lambda path: path.relative_to(site).as_posix(),
    )


def contract_data_directories() -> tuple[Path, Path]:
    return (ROOT / "schemas", ROOT / "examples")


def contract_root_files() -> tuple[Path, ...]:
    return (ROOT / "CONTRIBUTING.md",)


def rewrite_contract_links(site: Path) -> None:
    replacements = {
        'href="../../../schemas/': 'href="../../schemas/',
        'href="../../../examples/': 'href="../../examples/',
        'href="../../../CONTRIBUTING.md"': 'href="../../CONTRIBUTING.md"',
    }
    for path in sorted(site.rglob("*.html")):
        text = path.read_text(encoding="utf-8")
        rewritten = text
        for old, new in replacements.items():
            rewritten = rewritten.replace(old, new)
        if rewritten != text:
            path.write_text(rewritten, encoding="utf-8", newline="\n")


class _RuntimeAssetParser(HTMLParser):
    def __init__(self, relative: str) -> None:
        super().__init__(convert_charrefs=True)
        self.relative = relative
        self.errors: list[str] = []

    @staticmethod
    def _is_remote(value: str) -> bool:
        lowered = value.strip().lower()
        return lowered.startswith(("http://", "https://", "//"))

    def handle_starttag(
        self,
        tag: str,
        attrs: list[tuple[str, str | None]],
    ) -> None:
        values = {name.lower(): value or "" for name, value in attrs}
        attribute: str | None = None
        if tag in {"script", "img", "source", "video", "audio"}:
            attribute = "src"
        elif tag == "link" and "stylesheet" in values.get("rel", "").lower().split():
            attribute = "href"
        if attribute and self._is_remote(values.get(attribute, "")):
            self.errors.append(
                f"{self.relative}: {tag} {attribute} uses remote runtime asset"
            )


class _LocalLinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.targets: list[str] = []

    def handle_starttag(
        self,
        tag: str,
        attrs: list[tuple[str, str | None]],
    ) -> None:
        values = {name.lower(): value or "" for name, value in attrs}
        for attribute in ("href", "src"):
            value = values.get(attribute)
            if value:
                self.targets.append(value)


def external_runtime_assets(site: Path) -> list[str]:
    errors: list[str] = []
    for path in sorted(site.rglob("*.html")):
        parser = _RuntimeAssetParser(path.relative_to(site).as_posix())
        parser.feed(path.read_text(encoding="utf-8"))
        errors.extend(parser.errors)
    return sorted(errors)


def internal_link_errors(site: Path) -> list[str]:
    errors: list[str] = []
    resolved_site = site.resolve()
    for path in sorted(site.rglob("*.html")):
        relative = path.relative_to(site).as_posix()
        parser = _LocalLinkParser()
        parser.feed(path.read_text(encoding="utf-8"))
        for raw_target in parser.targets:
            target = urlsplit(raw_target)
            if target.scheme in {"http", "https", "mailto", "tel", "data"}:
                continue
            if target.scheme or target.netloc:
                errors.append(f"{relative}: unsupported link target {raw_target}")
                continue
            if not target.path:
                continue
            decoded = unquote(target.path)
            if decoded.startswith("/"):
                errors.append(f"{relative}: absolute offline link {raw_target}")
                continue
            candidate = (path.parent / decoded).resolve()
            try:
                candidate.relative_to(resolved_site)
            except ValueError:
                errors.append(f"{relative}: link escapes offline site {raw_target}")
                continue
            if not candidate.exists():
                errors.append(f"{relative}: missing offline target {raw_target}")
    return sorted(set(errors))


def write_build_manifest(
    site: Path,
    *,
    documentation_version: str,
    server_compatibility: str,
    source_commit: str,
) -> dict[str, object]:
    documentation_version = validate_token(documentation_version, "documentation version")
    server_compatibility = validate_token(server_compatibility, "server compatibility")
    source_commit = validate_source_commit(source_commit)
    if not (site / "index.html").is_file():
        raise BuildFailure("offline documentation entrypoint index.html is missing")
    remote_assets = external_runtime_assets(site)
    if remote_assets:
        raise BuildFailure("; ".join(remote_assets))

    files = {
        path.relative_to(site).as_posix(): {
            "sha256": sha256_file(path),
            "size_bytes": path.stat().st_size,
        }
        for path in payload_files(site)
    }
    manifest: dict[str, object] = {
        "schema": "ultimate-odycer.docs-build.v1",
        "documentation_version": documentation_version,
        "compatibility": {"server": server_compatibility},
        "source_commit": source_commit,
        "entrypoint": "index.html",
        "languages": ["fr", "en"],
        "files": files,
    }
    (site / BUILD_MANIFEST).write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return manifest


def verify_manifest(site: Path) -> list[str]:
    errors: list[str] = []
    manifest_path = site / BUILD_MANIFEST
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return [f"invalid offline docs manifest: {error}"]
    if manifest.get("schema") != "ultimate-odycer.docs-build.v1":
        errors.append("offline docs manifest uses an unknown schema")
    declared = manifest.get("files")
    if not isinstance(declared, dict):
        return errors + ["offline docs manifest files must be an object"]
    actual = {
        path.relative_to(site).as_posix(): path
        for path in payload_files(site)
    }
    if set(actual) != set(declared):
        missing = sorted(set(actual) - set(declared))
        extra = sorted(set(declared) - set(actual))
        errors.append(f"offline docs file set differs: missing={missing}, extra={extra}")
    for relative in sorted(set(actual) & set(declared)):
        record = declared[relative]
        if not isinstance(record, dict):
            errors.append(f"offline docs manifest record is invalid: {relative}")
            continue
        if record.get("sha256") != sha256_file(actual[relative]):
            errors.append(f"offline docs digest mismatch: {relative}")
        if record.get("size_bytes") != actual[relative].stat().st_size:
            errors.append(f"offline docs size mismatch: {relative}")
    errors.extend(external_runtime_assets(site))
    errors.extend(internal_link_errors(site))
    return sorted(set(errors))


def build_site(
    output: Path,
    *,
    documentation_version: str,
    server_compatibility: str,
    source_commit: str,
) -> dict[str, object]:
    output = resolve_output_directory(output)
    if output.exists():
        shutil.rmtree(output)
    subprocess.run(
        [
            sys.executable,
            "-m",
            "mkdocs",
            "build",
            "--strict",
            "--site-dir",
            str(output),
        ],
        cwd=ROOT,
        check=True,
    )
    not_found_page = output / "404.html"
    if not_found_page.is_file():
        not_found_page.unlink()
    for source in contract_data_directories():
        shutil.copytree(source, output / source.name)
    for source in contract_root_files():
        shutil.copy2(source, output / source.name)
    rewrite_contract_links(output)
    shutil.copy2(ROOT / "llms.txt", output / "llms.txt")
    manifest = write_build_manifest(
        output,
        documentation_version=documentation_version,
        server_compatibility=server_compatibility,
        source_commit=source_commit,
    )
    errors = verify_manifest(output)
    if errors:
        raise BuildFailure("; ".join(errors))
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--documentation-version", required=True)
    parser.add_argument("--server-compatibility", required=True)
    parser.add_argument("--source-commit", required=True)
    args = parser.parse_args()
    try:
        manifest = build_site(
            args.output_dir,
            documentation_version=args.documentation_version,
            server_compatibility=args.server_compatibility,
            source_commit=args.source_commit,
        )
    except (BuildFailure, OSError, subprocess.CalledProcessError) as error:
        print(f"offline docs build failed: {error}", file=sys.stderr)
        return 1
    print(
        "offline docs build: ok "
        f"({len(manifest['files'])} files, {args.documentation_version})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
