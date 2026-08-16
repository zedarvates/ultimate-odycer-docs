# SPDX-License-Identifier: MIT

from __future__ import annotations

import json
import hashlib
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
METRIC_STATUSES = {"observed", "estimated", "decision", "unavailable"}
REQUIRED_PATHS = (
    "README.md",
    "PUBLICATION_STATUS.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "LICENSES/README.md",
    "LICENSE.md",
    "LICENSES/CC-BY-4.0.md",
    "LICENSES/MIT.txt",
    "NOTICE.md",
    "MANIFEST.sha256",
    "llms.txt",
    "schemas/npc-benchmark-v1.schema.json",
    "examples/benchmark-results/estimated-esp32-s3.json",
    "docs/llm/README.md",
    "docs/llm/context-index.json",
)
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
FORBIDDEN_PATTERNS = (
    ("absolute Windows user path", re.compile(r"[A-Za-z]:\\Users\\", re.IGNORECASE)),
    ("serial port identifier", re.compile(r"\bCOM\d+\b", re.IGNORECASE)),
    (
        "private or loopback IPv4 address",
        re.compile(
            r"\b(?:10\.\d{1,3}|127\.\d{1,3}|192\.168|"
            r"172\.(?:1[6-9]|2\d|3[01]))\.\d{1,3}\.\d{1,3}\b"
        ),
    ),
    ("private key material", re.compile(r"BEGIN (?:RSA |EC )?PRIVATE KEY")),
)
MANIFEST_EXCLUDED_PARTS = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".venv",
    "build",
    "dist",
}


def bilingual_errors() -> list[str]:
    errors: list[str] = []
    for language, counterpart in (("fr", "en"), ("en", "fr")):
        language_root = ROOT / "docs" / language
        for path in language_root.rglob("*.md"):
            relative = path.relative_to(language_root)
            paired = ROOT / "docs" / counterpart / relative
            if not paired.is_file():
                errors.append(f"missing {counterpart} pair for {path.relative_to(ROOT)}")
    return errors


def markdown_link_errors() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            candidate = (path.parent / target).resolve()
            try:
                candidate.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(
                    f"link escapes repository: {path.relative_to(ROOT)} -> {raw_target}"
                )
                continue
            if not candidate.exists():
                errors.append(
                    f"missing link target: {path.relative_to(ROOT)} -> {raw_target}"
                )
    return errors


def forbidden_content_errors() -> list[str]:
    errors: list[str] = []
    text_extensions = {".md", ".txt", ".json", ".py"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in text_extensions:
            continue
        if path.resolve() == Path(__file__).resolve():
            continue
        text = path.read_text(encoding="utf-8")
        for label, pattern in FORBIDDEN_PATTERNS:
            if pattern.search(text):
                errors.append(f"{label} in {path.relative_to(ROOT)}")
    return errors


def llm_index_errors() -> list[str]:
    errors: list[str] = []
    index_path = ROOT / "docs" / "llm" / "context-index.json"
    index = json.loads(index_path.read_text(encoding="utf-8"))
    if index.get("authority") != "documentation_only":
        errors.append("LLM index authority must be documentation_only")
    if set(index.get("metric_statuses", [])) != METRIC_STATUSES:
        errors.append("LLM index metric statuses do not match the public contract")

    document_ids: set[str] = set()
    for document in index.get("documents", []):
        document_id = document.get("id")
        if not document_id or document_id in document_ids:
            errors.append(f"missing or duplicate LLM document id: {document_id!r}")
        document_ids.add(document_id)
        if document.get("mutating") is not False:
            errors.append(f"LLM document must be non-mutating: {document_id}")
        target = ROOT / str(document.get("path", ""))
        if not target.is_file():
            errors.append(f"LLM document path is missing: {document.get('path')}")

    llms_text = (ROOT / "llms.txt").read_text(encoding="utf-8")
    for line in llms_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("- docs/"):
            target = ROOT / stripped.removeprefix("- ")
            if not target.is_file():
                errors.append(f"llms.txt path is missing: {target.relative_to(ROOT)}")
    return errors


def metric_example_errors() -> list[str]:
    errors: list[str] = []
    schema = json.loads(
        (ROOT / "schemas" / "npc-benchmark-v1.schema.json").read_text(
            encoding="utf-8"
        )
    )
    example = json.loads(
        (ROOT / "examples" / "benchmark-results" / "estimated-esp32-s3.json").read_text(
            encoding="utf-8"
        )
    )

    expected_required = set(schema.get("required", []))
    missing = expected_required - set(example)
    if missing:
        errors.append(f"metric example is missing fields: {sorted(missing)}")
    if example.get("schema_version") != "npc-benchmark-v1":
        errors.append("metric example uses an unknown schema version")
    if example.get("status") not in METRIC_STATUSES:
        errors.append("metric example has an invalid status")
    if example.get("status") == "estimated":
        measurements = example.get("measurements", {})
        for field in ("sample_count", "p50_seconds", "p95_seconds"):
            if measurements.get(field) != "unavailable":
                errors.append(f"estimated example must not imply observed {field}")
    if example.get("status") == "observed":
        measurements = example.get("measurements", {})
        if not isinstance(measurements.get("sample_count"), int) or measurements.get(
            "sample_count", 0
        ) <= 0:
            errors.append("observed example requires a positive sample_count")
    capacity = example.get("capacity", {})
    if capacity.get("queue_policy") != "serialize_per_stream":
        errors.append("metric example must declare its queue policy")
    return errors


def manifest_errors() -> list[str]:
    errors: list[str] = []
    manifest_path = ROOT / "MANIFEST.sha256"
    if not manifest_path.is_file():
        return ["missing MANIFEST.sha256"]

    declared: dict[str, str] = {}
    for line_number, line in enumerate(
        manifest_path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        try:
            digest, relative = line.split("  ", 1)
        except ValueError:
            errors.append(f"invalid manifest line {line_number}")
            continue
        if not re.fullmatch(r"[0-9a-f]{64}", digest):
            errors.append(f"invalid SHA-256 on manifest line {line_number}")
        if relative in declared:
            errors.append(f"duplicate manifest path: {relative}")
        declared[relative] = digest

    included = {
        path.relative_to(ROOT).as_posix(): path
        for path in ROOT.rglob("*")
        if path.is_file()
        and path != manifest_path
        and not any(part in MANIFEST_EXCLUDED_PARTS for part in path.parts)
    }
    missing = set(included) - set(declared)
    extra = set(declared) - set(included)
    if missing:
        errors.append(f"manifest is missing paths: {sorted(missing)}")
    if extra:
        errors.append(f"manifest has unknown paths: {sorted(extra)}")
    for relative in sorted(set(included) & set(declared)):
        actual = hashlib.sha256(included[relative].read_bytes()).hexdigest()
        if actual != declared[relative]:
            errors.append(f"manifest digest mismatch: {relative}")
    return errors


def license_errors() -> list[str]:
    errors: list[str] = []
    license_map = (ROOT / "LICENSE.md").read_text(encoding="utf-8")
    mit_text = (ROOT / "LICENSES" / "MIT.txt").read_text(encoding="utf-8")
    context_index = json.loads(
        (ROOT / "docs" / "llm" / "context-index.json").read_text(encoding="utf-8")
    )

    for identifier in ("CC-BY-4.0", "MIT"):
        if identifier not in license_map:
            errors.append(f"LICENSE.md is missing {identifier}")
    if "Permission is hereby granted, free of charge" not in mit_text:
        errors.append("MIT permission notice is incomplete")
    expected_licenses = {
        "documentation": "CC-BY-4.0",
        "scripts_schemas_examples": "MIT",
    }
    if context_index.get("licenses") != expected_licenses:
        errors.append("LLM index license mapping is inconsistent")

    for directory in (ROOT / "scripts", ROOT / "tests"):
        for path in directory.rglob("*.py"):
            first_line = path.read_text(encoding="utf-8").splitlines()[0]
            if first_line != "# SPDX-License-Identifier: MIT":
                errors.append(f"missing MIT SPDX header: {path.relative_to(ROOT)}")
    return errors


def validate() -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_PATHS:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required path: {relative}")
    errors.extend(bilingual_errors())
    errors.extend(markdown_link_errors())
    errors.extend(forbidden_content_errors())
    errors.extend(llm_index_errors())
    errors.extend(metric_example_errors())
    errors.extend(license_errors())
    errors.extend(manifest_errors())
    return sorted(set(errors))


def main() -> int:
    errors = validate()
    if errors:
        print("validation: failed")
        for error in errors:
            print(f"- {error}")
        return 1
    markdown_count = sum(1 for _ in ROOT.rglob("*.md"))
    print(f"validation: ok ({markdown_count} Markdown files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
