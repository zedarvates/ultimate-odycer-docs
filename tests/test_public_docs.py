# SPDX-License-Identifier: MIT

from __future__ import annotations

import json
import unittest
from pathlib import Path

from scripts.npc_capacity_estimator import CapacityError, CapacityInput, estimate_capacity
from scripts.validate_docs import validate


ROOT = Path(__file__).resolve().parents[1]
LOCAL_SETUP_DOCUMENTS = (
    "tutorials/create-first-local-world.md",
    "reference/engine-template-world-matrix.md",
    "how-to/install-local-server-windows.md",
    "how-to/install-local-server-linux.md",
    "how-to/backup-and-test-restore-postgresql.md",
    "how-to/connect-godot-template.md",
    "reference/local-setup-acceptance-checklist.md",
)


class PublicDocumentationTests(unittest.TestCase):
    def test_public_repository_passes_structural_validation(self) -> None:
        self.assertEqual(validate(), [])

    def test_scenario_capacity_is_deterministic(self) -> None:
        result = estimate_capacity(
            CapacityInput(
                reply_seconds=1.7,
                npc_interval_seconds=120,
                utilization=0.5,
                streams=1,
                basis="scenario",
            )
        )
        self.assertEqual(result["planned_replies_per_minute"], 17.647)
        self.assertEqual(result["supported_active_npcs"], 35)
        self.assertEqual(result["queue_policy"], "serialize_per_stream")

    def test_invalid_capacity_input_fails_closed(self) -> None:
        with self.assertRaises(CapacityError):
            estimate_capacity(CapacityInput(reply_seconds=0, npc_interval_seconds=60))
        with self.assertRaises(CapacityError):
            estimate_capacity(
                CapacityInput(
                    reply_seconds=1,
                    npc_interval_seconds=60,
                    utilization=1.1,
                )
            )

    def test_local_setup_catalog_contract(self) -> None:
        catalog = json.loads(
            (ROOT / "examples" / "local-setup-catalog.json").read_text(
                encoding="utf-8"
            )
        )

        self.assertEqual(
            catalog["schema_version"],
            "ultimate-odycer.local-setup-catalog.v1",
        )
        self.assertEqual(
            catalog["release_page"],
            "https://www.ultimateodycer.com/releases/",
        )
        self.assertEqual(catalog["current_server_release"], "unavailable")
        self.assertEqual(
            {item["id"] for item in catalog["platforms"]},
            {"windows", "linux", "android", "macos"},
        )
        self.assertIn(
            "ultod-client-godot-open-city-crime-rpg-template",
            {item["repository"] for item in catalog["templates"]},
        )

    def test_local_setup_has_required_bilingual_pairs(self) -> None:
        for relative in LOCAL_SETUP_DOCUMENTS:
            with self.subTest(relative=relative):
                self.assertTrue((ROOT / "docs" / "fr" / relative).is_file())
                self.assertTrue((ROOT / "docs" / "en" / relative).is_file())


if __name__ == "__main__":
    unittest.main()
