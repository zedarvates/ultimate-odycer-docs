# SPDX-License-Identifier: MIT

from __future__ import annotations

import json
import hashlib
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
METRIC_STATUSES = {"observed", "estimated", "decision", "unavailable"}
COMPONENT_STATUSES = {"available", "under_construction", "planned", "unavailable"}
CREATIVE_MATURITY = {"executable_public", "prototype_local", "scaffolding_proxy", "planned", "available_external", "verification_required", "unavailable"}
CREATIVE_EXECUTION = {"local", "cloud", "hybrid", "not_applicable"}
CREATIVE_PRICING = {"free_open_source", "free", "free_noncommercial", "freemium", "one_time_purchase", "subscription", "credits", "revenue_limited", "project_budget_limited", "contact_sales", "mixed"}
CREATIVE_COMMERCIAL = {"allowed", "conditional", "noncommercial_only", "plan_dependent", "asset_dependent", "model_dependent", "verification_required"}
CREATIVE_INTEGRATION = {"direct", "conversion_required", "reference_only"}
REQUIRED_PATHS = (
    "requirements-docs.txt",
    "mkdocs.yml",
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
    "schemas/local-setup-catalog-v1.schema.json",
    "schemas/creative-tools-catalog-v1.schema.json",
    "examples/benchmark-results/estimated-esp32-s3.json",
    "examples/local-setup-catalog.json",
    "examples/creative-tools-catalog.json",
    "docs/llm/README.md",
    "docs/llm/context-index.json",
    "docs/index.md",
    "docs/assets/stylesheets/ultimate-odycer-docs.css",
    "scripts/build_static_docs.py",
)
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
FORBIDDEN_PATTERNS = (
    ("absolute Windows user path", re.compile(r"[A-Za-z]:\\Users\\", re.IGNORECASE)),
    (
        "patch artifact marker",
        re.compile(r"^\*\*\* (?:Add|Update|Delete) File:", re.MULTILINE),
    ),
    (
        "local worktree path",
        re.compile(r"[A-Za-z]:[/\\].*?\.worktrees[/\\]", re.IGNORECASE),
    ),
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
    ".worktrees",
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
        if any(
            part in MANIFEST_EXCLUDED_PARTS for part in path.relative_to(ROOT).parts
        ):
            continue
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
        if (
            not path.is_file()
            or path.suffix.lower() not in text_extensions
            or any(
                part in MANIFEST_EXCLUDED_PARTS
                for part in path.relative_to(ROOT).parts
            )
        ):
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


def local_setup_catalog_errors() -> list[str]:
    errors: list[str] = []
    catalog_path = ROOT / "examples" / "local-setup-catalog.json"
    schema_path = ROOT / "schemas" / "local-setup-catalog-v1.schema.json"
    try:
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return [f"invalid local setup catalog contract: {error}"]

    if catalog.get("schema_version") != "ultimate-odycer.local-setup-catalog.v1":
        errors.append("local setup catalog uses an unknown schema version")
    if catalog.get("release_page") != "https://www.ultimateodycer.com/releases/":
        errors.append("local setup catalog must use the official HTTPS release page")
    if catalog.get("default_engine") != "godot":
        errors.append("local setup catalog default engine must be Godot")
    if catalog.get("primary_platform") != "windows":
        errors.append("local setup catalog primary platform must be Windows")

    current_release = catalog.get("current_server_release")
    if current_release != "unavailable":
        if not isinstance(current_release, dict):
            errors.append("local setup current server release must be unavailable or an object")
        else:
            artifacts = current_release.get("artifacts")
            if not current_release.get("version") or not isinstance(artifacts, list) or not artifacts:
                errors.append("available local setup release requires a version and artifacts")
            else:
                for artifact in artifacts:
                    if (
                        not isinstance(artifact, dict)
                        or not str(artifact.get("url", "")).startswith("https://")
                        or re.fullmatch(r"[0-9a-f]{64}", str(artifact.get("sha256", "")))
                        is None
                    ):
                        errors.append("local setup release artifact requires HTTPS and SHA-256")
                        break

    def unique_ids(items: object, label: str, key: str = "id") -> set[str]:
        if not isinstance(items, list) or not items:
            errors.append(f"local setup catalog requires {label}")
            return set()
        identifiers = [str(item.get(key, "")) for item in items if isinstance(item, dict)]
        if len(identifiers) != len(items) or any(not identifier for identifier in identifiers):
            errors.append(f"local setup catalog has invalid {label} identifiers")
        if len(set(identifiers)) != len(identifiers):
            errors.append(f"local setup catalog has duplicate {label} identifiers")
        return set(identifiers)

    platform_ids = unique_ids(catalog.get("platforms"), "platform")
    if platform_ids != {"windows", "linux", "android", "macos"}:
        errors.append("local setup platform catalog does not match the public contract")
    engine_ids = unique_ids(catalog.get("engines"), "engine")
    if engine_ids != {"godot", "threejs", "unity", "unreal", "foveacore"}:
        errors.append("local setup engine catalog does not match the public contract")
    template_ids = unique_ids(catalog.get("templates"), "template", "repository")
    if "ultod-client-godot-open-city-crime-rpg-template" not in template_ids:
        errors.append("local setup catalog is missing the open-city Godot template")
    unique_ids(catalog.get("components"), "component")
    hardware_ids = unique_ids(catalog.get("hardware_profiles"), "hardware profile")
    if hardware_ids != {"dedicated_server", "shared_workstation", "creation_workstation"}:
        errors.append("local setup hardware profiles do not match the public contract")

    for group in ("platforms", "engines", "templates", "components"):
        for item in catalog.get(group, []):
            if not isinstance(item, dict) or item.get("status") not in COMPONENT_STATUSES:
                errors.append(f"local setup catalog has invalid component status in {group}")
                break
    for profile in catalog.get("hardware_profiles", []):
        if not isinstance(profile, dict) or profile.get("status") not in METRIC_STATUSES:
            errors.append("local setup catalog has invalid hardware status")
            break
        for field in ("cpu_cores", "ram_gib", "free_ssd_gib"):
            if not isinstance(profile.get(field), int) or profile[field] <= 0:
                errors.append(f"local setup hardware profile has invalid {field}")
                break

    if set(catalog.get("topologies", [])) != {
        "flat_map",
        "planet",
        "mega_planet",
        "solar_system",
    }:
        errors.append("local setup topology catalog does not match the public contract")

    try:
        schema_statuses = set(schema["$defs"]["component_status"]["enum"])
        schema_measurements = set(schema["$defs"]["measurement_status"]["enum"])
    except (KeyError, TypeError):
        errors.append("local setup schema is missing status vocabularies")
    else:
        if schema_statuses != COMPONENT_STATUSES:
            errors.append("local setup schema component statuses are inconsistent")
        if schema_measurements != METRIC_STATUSES:
            errors.append("local setup schema measurement statuses are inconsistent")
    return errors


def creative_tools_catalog_errors() -> list[str]:
    errors: list[str] = []
    catalog_path = ROOT / "examples" / "creative-tools-catalog.json"
    schema_path = ROOT / "schemas" / "creative-tools-catalog-v1.schema.json"
    try:
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return [f"invalid creative tools catalog contract: {error}"]
    if catalog.get("schema_version") != "ultimate-odycer.creative-tools-catalog.v1":
        errors.append("creative tools catalog uses an unknown schema version")
    if catalog.get("pricing_policy") != "model_only_no_exact_prices":
        errors.append("creative tools catalog pricing policy is invalid")
    if catalog.get("default_strategy") != "local_first_free_open_source":
        errors.append("creative tools catalog default strategy is invalid")
    if re.fullmatch(r"20\d{2}-\d{2}-\d{2}", str(catalog.get("verified_on", ""))) is None:
        errors.append("creative tools catalog verification date is invalid")
    forbidden_price_fields = {"price", "exact_price", "amount", "currency"}
    if forbidden_price_fields & set(catalog):
        errors.append("creative tools catalog contains exact price fields")
    tools = catalog.get("tools")
    if not isinstance(tools, list) or not tools:
        return errors + ["creative tools catalog requires tools"]
    tool_ids: list[str] = []
    by_id: dict[str, dict[str, object]] = {}
    for tool in tools:
        if not isinstance(tool, dict):
            errors.append("creative tools catalog has a non-object tool")
            continue
        tool_id = str(tool.get("id", ""))
        if not tool_id:
            errors.append("creative tools catalog has a missing tool id")
            continue
        tool_ids.append(tool_id)
        by_id[tool_id] = tool
        if forbidden_price_fields & set(tool):
            errors.append(f"creative tool contains exact price fields: {tool_id}")
        if tool.get("maturity") not in CREATIVE_MATURITY:
            errors.append(f"creative tool has invalid maturity: {tool_id}")
        if tool.get("execution") not in CREATIVE_EXECUTION:
            errors.append(f"creative tool has invalid execution: {tool_id}")
        pricing = tool.get("pricing_model")
        if not isinstance(pricing, list) or not pricing or not set(pricing) <= CREATIVE_PRICING:
            errors.append(f"creative tool has invalid pricing model: {tool_id}")
        if tool.get("commercial_use") not in CREATIVE_COMMERCIAL:
            errors.append(f"creative tool has invalid commercial use: {tool_id}")
        if tool.get("integration") not in CREATIVE_INTEGRATION:
            errors.append(f"creative tool has invalid integration: {tool_id}")
        for field in ("official_url", "pricing_or_license_url"):
            if not str(tool.get(field, "")).startswith("https://"):
                errors.append(f"creative tool requires HTTPS {field}: {tool_id}")
        if re.fullmatch(r"20\d{2}-\d{2}-\d{2}", str(tool.get("verified_on", ""))) is None:
            errors.append(f"creative tool has invalid verification date: {tool_id}")
        for field in ("domains", "inputs", "outputs", "platforms"):
            value = tool.get(field)
            if not isinstance(value, list) or not value or len(value) != len(set(value)):
                errors.append(f"creative tool has invalid {field}: {tool_id}")
    if len(tool_ids) != len(set(tool_ids)):
        errors.append("creative tools catalog has duplicate tool ids")
    for lite_id in (
        "creature-editor-lite",
        "city-editor-lite",
        "architecture-editor-lite",
        "dungeon-editor-lite",
        "avatar-editor-lite",
    ):
        if by_id.get(lite_id, {}).get("maturity") != "executable_public":
            errors.append(f"creative tools catalog Lite maturity drift: {lite_id}")
    recommendations = catalog.get("recommendations")
    if not isinstance(recommendations, dict) or not recommendations:
        errors.append("creative tools catalog requires recommendations")
    else:
        known = set(tool_ids)
        for domain, recommendation in recommendations.items():
            if not isinstance(recommendation, dict):
                errors.append(f"creative recommendation is invalid: {domain}")
                continue
            selected = recommendation.get("tools")
            default = recommendation.get("default_tool")
            if not isinstance(selected, list) or not 2 <= len(selected) <= 5 or len(selected) != len(set(selected)):
                errors.append(f"creative recommendation tool count is invalid: {domain}")
                continue
            if not set(selected) <= known:
                errors.append(f"creative recommendation references unknown tools: {domain}")
            if default not in selected:
                errors.append(f"creative recommendation default is invalid: {domain}")
    try:
        defs = schema["$defs"]
        enum_contracts = {
            "maturity": CREATIVE_MATURITY,
            "execution": CREATIVE_EXECUTION,
            "pricing_model": CREATIVE_PRICING,
            "commercial_use": CREATIVE_COMMERCIAL,
            "integration": CREATIVE_INTEGRATION,
        }
        for name, expected in enum_contracts.items():
            if set(defs[name]["enum"]) != expected:
                errors.append(f"creative tools schema {name} vocabulary is inconsistent")
    except (KeyError, TypeError):
        errors.append("creative tools schema is missing vocabularies")
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
        and not any(
            part in MANIFEST_EXCLUDED_PARTS for part in path.relative_to(ROOT).parts
        )
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
    errors.extend(local_setup_catalog_errors())
    errors.extend(creative_tools_catalog_errors())
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
