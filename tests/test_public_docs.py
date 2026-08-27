# SPDX-License-Identifier: MIT

from __future__ import annotations

import json
import unittest
from pathlib import Path

from scripts.npc_capacity_estimator import CapacityError, CapacityInput, estimate_capacity
from scripts.validate_docs import validate


ROOT = Path(__file__).resolve().parents[1]
CREATIVE_CATALOG = ROOT / "examples" / "creative-tools-catalog.json"
LOCAL_SETUP_DOCUMENTS = (
    "tutorials/create-first-local-world.md",
    "reference/engine-template-world-matrix.md",
    "how-to/install-local-server-windows.md",
    "how-to/install-local-server-linux.md",
    "how-to/backup-and-test-restore-postgresql.md",
    "how-to/connect-godot-template.md",
    "reference/local-setup-acceptance-checklist.md",
)
CREATIVE_DOCUMENTS = (
    "tutorials/creative-production-handbook.md",
    "how-to/draw-and-convert-map.md",
    "how-to/organize-project-kanboard-botte-secrete.md",
    "reference/creative-tools-catalog.md",
    "reference/world-map-and-structure-tools.md",
    "reference/3d-assets-materials-and-photogrammetry-tools.md",
    "reference/character-creature-and-animation-tools.md",
    "reference/audio-2d-ui-vfx-and-video-tools.md",
    "reference/local-and-cloud-ai-tools.md",
    "reference/import-optimization-licensing-and-provenance.md",
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

    def test_creative_tools_catalog_contract(self) -> None:
        catalog = json.loads(CREATIVE_CATALOG.read_text(encoding="utf-8"))
        self.assertEqual(
            catalog["schema_version"],
            "ultimate-odycer.creative-tools-catalog.v1",
        )
        self.assertEqual(catalog["pricing_policy"], "model_only_no_exact_prices")
        tools = {item["id"]: item for item in catalog["tools"]}
        self.assertEqual(
            tools["creature-editor-lite"]["maturity"], "executable_public"
        )
        self.assertEqual(tools["city-editor-lite"]["maturity"], "executable_public")
        self.assertEqual(
            tools["architecture-editor-lite"]["maturity"], "executable_public"
        )
        self.assertEqual(tools["dungeon-editor-lite"]["maturity"], "executable_public")
        self.assertEqual(tools["avatar-editor-lite"]["maturity"], "executable_public")
        self.assertEqual(
            tools["threejs-2-5d-template"]["maturity"], "executable_public"
        )
        forbidden_price_fields = {"price", "exact_price", "amount", "currency"}
        self.assertTrue(forbidden_price_fields.isdisjoint(catalog))
        for tool in tools.values():
            self.assertTrue(forbidden_price_fields.isdisjoint(tool))

    def test_creative_handbook_has_required_bilingual_pairs(self) -> None:
        for relative in CREATIVE_DOCUMENTS:
            with self.subTest(relative=relative):
                self.assertTrue((ROOT / "docs" / "fr" / relative).is_file())
                self.assertTrue((ROOT / "docs" / "en" / relative).is_file())

    def test_creative_handbook_is_indexed_for_humans_and_llms(self) -> None:
        llms_text = (ROOT / "llms.txt").read_text(encoding="utf-8")
        context = json.loads(
            (ROOT / "docs" / "llm" / "context-index.json").read_text(
                encoding="utf-8"
            )
        )
        indexed_paths = {item["path"] for item in context["documents"]}
        required_paths = {
            "docs/fr/tutorials/creative-production-handbook.md",
            "docs/en/tutorials/creative-production-handbook.md",
            "docs/fr/reference/creative-tools-catalog.md",
            "docs/en/reference/creative-tools-catalog.md",
        }
        for path in required_paths:
            with self.subTest(path=path):
                self.assertIn(path, llms_text)
                self.assertIn(path, indexed_paths)

    def test_public_docs_reject_patch_artifacts_and_local_worktree_paths(self) -> None:
        forbidden = ("*** Add File:", "*** Update File:", "*** Delete File:", ".worktrees/")
        for path in (ROOT / "docs").rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            for marker in forbidden:
                with self.subTest(path=path.relative_to(ROOT), marker=marker):
                    self.assertNotIn(marker, text)


if __name__ == "__main__":
    unittest.main()
