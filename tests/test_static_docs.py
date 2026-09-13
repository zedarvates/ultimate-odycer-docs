# SPDX-License-Identifier: MIT

from __future__ import annotations

import sys
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import build_static_docs as static_docs  # noqa: E402


class StaticDocumentationTests(unittest.TestCase):
    def test_missing_llm_index_targets_are_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            (site / "llm").mkdir()
            (site / "llms.txt").write_text(
                "[Guide](docs/fr/guide.md)\n", encoding="utf-8"
            )
            (site / "llm/context-index.json").write_text(json.dumps({
                "documents": [{"path": "docs/en/guide.md"}]
            }), encoding="utf-8")
            errors = static_docs.internal_link_errors(site)
            self.assertTrue(any("docs/fr/guide.md" in error for error in errors))
            self.assertTrue(any("docs/en/guide.md" in error for error in errors))

    def test_machine_indexes_use_bundled_html_without_changing_authority(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            (site / "llm").mkdir()
            (site / "fr").mkdir()
            (site / "fr/guide.html").write_text("Guide", encoding="utf-8")
            (site / "llm/index.html").write_text("Rules", encoding="utf-8")
            source = site / "source.txt"
            source.write_text(
                "documentation_only\n[Guide](docs/fr/guide.md#start)\n"
                "[Rules](docs/llm/README.md)\n"
                "[External](https://example.org/docs/guide.md)\n",
                encoding="utf-8",
            )
            record = {"authority": "documentation_only", "documents": [
                {"id": "guide-fr", "path": "docs/fr/guide.md", "mutating": False}
            ]}
            index = site / "llm/context-index.json"
            index.write_text(json.dumps(record), encoding="utf-8")
            static_docs.rewrite_machine_indexes(site, source)
            text = (site / "llms.txt").read_text(encoding="utf-8")
            self.assertIn("(fr/guide.html#start)", text)
            self.assertIn("(llm/index.html)", text)
            self.assertIn("(https://example.org/docs/guide.md)", text)
            rewritten = json.loads(index.read_text(encoding="utf-8"))
            self.assertEqual(rewritten["path_base"], "site-root")
            self.assertEqual(rewritten["authority"], "documentation_only")
            self.assertEqual(rewritten["documents"], [
                {"id": "guide-fr", "path": "fr/guide.html", "mutating": False}
            ])
            self.assertEqual(static_docs.internal_link_errors(site), [])

    def test_machine_index_cannot_escape_site(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            (site / "llms.txt").write_text(
                "[Escape](../outside.txt)\n", encoding="utf-8"
            )
            self.assertTrue(any("escapes offline site" in error
                                for error in static_docs.internal_link_errors(site)))

    def test_manifest_verifies_complete_offline_site(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            (site / "assets").mkdir()
            (site / "index.html").write_text(
                '<!doctype html><link rel="stylesheet" href="assets/site.css">',
                encoding="utf-8",
            )
            (site / "assets" / "site.css").write_text(
                "body { color: #eee; }\n",
                encoding="utf-8",
            )
            (site / "llms.txt").write_text("documentation only\n", encoding="utf-8")

            manifest = static_docs.write_build_manifest(
                site,
                documentation_version="docs-2026.08",
                server_compatibility="unavailable",
                source_commit="56eab71",
            )

            self.assertTrue((site / "index.html").is_file())
            self.assertTrue((site / "docs-build-manifest.json").is_file())
            self.assertEqual(manifest["schema"], "ultimate-odycer.docs-build.v1")
            self.assertEqual(manifest["compatibility"]["server"], "unavailable")
            self.assertIn("index.html", manifest["files"])
            self.assertEqual(static_docs.external_runtime_assets(site), [])
            self.assertEqual(static_docs.internal_link_errors(site), [])
            self.assertEqual(static_docs.verify_manifest(site), [])

    def test_manifest_rejects_extra_and_modified_payload_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            (site / "assets").mkdir()
            (site / "index.html").write_text(
                '<!doctype html><link rel="stylesheet" href="assets/site.css">',
                encoding="utf-8",
            )
            stylesheet = site / "assets" / "site.css"
            stylesheet.write_text("body { color: #eee; }\n", encoding="utf-8")
            (site / "llms.txt").write_text("documentation only\n", encoding="utf-8")
            static_docs.write_build_manifest(
                site,
                documentation_version="docs-2026.08",
                server_compatibility="unavailable",
                source_commit="56eab71",
            )

            unexpected = site / "unexpected.txt"
            unexpected.write_text("unexpected\n", encoding="utf-8")
            self.assertTrue(any(
                "offline docs file set differs" in error
                for error in static_docs.verify_manifest(site)
            ))
            unexpected.unlink()

            stylesheet.write_text("body { color: #000; }\n", encoding="utf-8")
            self.assertIn(
                "offline docs digest mismatch: assets/site.css",
                static_docs.verify_manifest(site),
            )

            stylesheet.write_text("body { color: #000; } extra\n", encoding="utf-8")
            self.assertIn(
                "offline docs size mismatch: assets/site.css",
                static_docs.verify_manifest(site),
            )

    def test_repository_contract_data_is_part_of_a_real_build(self) -> None:
        source_directories = {
            path.name for path in static_docs.contract_data_directories()
        }
        self.assertEqual(source_directories, {"examples", "schemas"})

    def test_external_runtime_assets_are_rejected_but_links_are_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            (site / "index.html").write_text(
                """<!doctype html>
<a href="https://www.ultimateodycer.com/releases/">Releases</a>
<script src="https://cdn.invalid/app.js"></script>
""",
                encoding="utf-8",
            )
            self.assertEqual(
                static_docs.external_runtime_assets(site),
                ["index.html: script src uses remote runtime asset"],
            )

    def test_output_directory_must_stay_inside_build_root(self) -> None:
        outside = ROOT.parent / "unsafe-doc-output"
        with self.assertRaisesRegex(static_docs.BuildFailure, "inside repository build"):
            static_docs.resolve_output_directory(outside)

    def test_missing_internal_link_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            (site / "index.html").write_text(
                '<!doctype html><a href="missing.html">Missing</a>',
                encoding="utf-8",
            )
            self.assertEqual(
                static_docs.internal_link_errors(site),
                ["index.html: missing offline target missing.html"],
            )

    def test_repository_root_contract_links_are_rewritten_for_offline_site(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            page = site / "en" / "how-to" / "guide.html"
            page.parent.mkdir(parents=True)
            page.write_text(
                (
                    '<a href="../../../schemas/example.json">Schema</a>'
                    '<a href="../../../CONTRIBUTING.md">Contributing</a>'
                ),
                encoding="utf-8",
            )
            static_docs.rewrite_contract_links(site)
            self.assertEqual(
                page.read_text(encoding="utf-8"),
                (
                    '<a href="../../schemas/example.json">Schema</a>'
                    '<a href="../../CONTRIBUTING.md">Contributing</a>'
                ),
            )


if __name__ == "__main__":
    unittest.main()
