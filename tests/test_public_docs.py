# SPDX-License-Identifier: MIT

from __future__ import annotations

import unittest

from scripts.network_intent import NetworkIntentError, load_example, validate_intent
from scripts.npc_capacity_estimator import CapacityError, CapacityInput, estimate_capacity
from scripts.validate_docs import validate


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
                basis='scenario',
            )
        )
        self.assertEqual(result['planned_replies_per_minute'], 17.647)
        self.assertEqual(result['supported_active_npcs'], 35)
        self.assertEqual(result['queue_policy'], 'serialize_per_stream')

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

    def test_synthetic_network_intent_is_accepted(self) -> None:
        example = load_example()
        self.assertEqual(example['schema_version'], 'network-intent-v1')
        self.assertEqual(example['family'], 'talk')
        self.assertEqual(example['transport']['kind'], 'documentation_fixture')

    def test_authoritative_fields_are_rejected(self) -> None:
        example = load_example()
        example['gold'] = 12
        with self.assertRaises(NetworkIntentError):
            validate_intent(example)
        example = load_example()
        example['actor_id'] = 'player_live_01'
        with self.assertRaises(NetworkIntentError):
            validate_intent(example)


if __name__ == '__main__':
    unittest.main()
