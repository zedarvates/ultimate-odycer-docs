# SPDX-License-Identifier: MIT

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "MANIFEST.sha256"


def manifest_paths() -> list[Path]:
    paths: list[Path] = []
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        _, relative = line.split("  ", 1)
        source = ROOT / relative
        if not source.is_file():
            raise RuntimeError(f"manifest source is missing: {relative}")
        paths.append(source)
    return paths


def run_check(command: list[str], cwd: Path, environment: dict[str, str]) -> None:
    completed = subprocess.run(
        command,
        cwd=cwd,
        env=environment,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if completed.stdout:
        print(completed.stdout, end="")
    if completed.stderr:
        print(completed.stderr, end="", file=sys.stderr)
    if completed.returncode != 0:
        raise RuntimeError(
            f"fresh-copy command failed with exit code {completed.returncode}: {command}"
        )


def main() -> int:
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    with tempfile.TemporaryDirectory(prefix="ultimate-odycer-docs-fresh-") as directory:
        destination = Path(directory).resolve()
        for source in manifest_paths():
            relative = source.relative_to(ROOT)
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
        shutil.copy2(MANIFEST, destination / MANIFEST.name)

        run_check(
            [sys.executable, "-B", "scripts/validate_docs.py"],
            destination,
            environment,
        )
        run_check(
            [
                sys.executable,
                "-B",
                "-m",
                "unittest",
                "discover",
                "-s",
                "tests",
                "-v",
            ],
            destination,
            environment,
        )
        print(f"fresh-copy: ok ({len(manifest_paths())} manifest files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
