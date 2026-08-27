# SPDX-License-Identifier: MIT

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import build_static_docs as static_docs  # noqa: E402


class StaticDocumentationTests(unittest.TestCase):
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
                '<a href="../../../schemas/example.json">Schema</a>',
                encoding="utf-8",
            )
            static_docs.rewrite_contract_links(site)
            self.assertEqual(
                page.read_text(encoding="utf-8"),
                '<a href="../../schemas/example.json">Schema</a>',
            )


if __name__ == "__main__":
    unittest.main()
