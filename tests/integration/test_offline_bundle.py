# SPDX-License-Identifier: MIT
"""Real HTML build gate; requires requirements-docs.txt, never a server."""

import os
import tempfile
import unittest
from pathlib import Path

from scripts import build_static_docs as docs


class OfflineBundleIntegrationTests(unittest.TestCase):
    def test_real_bundle_contains_publication_status_and_valid_navigation(self):
        docs.BUILD_ROOT.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="integration-", dir=docs.BUILD_ROOT) as directory:
            site = Path(directory) / "site"
            manifest = docs.build_site(
                site,
                documentation_version="docs-ci-test",
                server_compatibility="unavailable",
                # Synthetic provenance outside GitHub: this temporary test is not a release.
                source_commit=os.environ.get("GITHUB_SHA", "0000000"),
            )
            self.assertTrue((site / "PUBLICATION_STATUS.md").is_file())
            self.assertEqual(
                (site / "PUBLICATION_STATUS.md").read_bytes(),
                (docs.ROOT / "PUBLICATION_STATUS.md").read_bytes(),
            )
            self.assertIn("PUBLICATION_STATUS.md", manifest["files"])
            self.assertEqual(docs.verify_manifest(site), [])
            # A missing root document must also break navigation, not just its digest.
            (site / "PUBLICATION_STATUS.md").unlink()
            self.assertTrue(any("PUBLICATION_STATUS.md" in error
                                for error in docs.internal_link_errors(site)))


if __name__ == "__main__":
    unittest.main()
