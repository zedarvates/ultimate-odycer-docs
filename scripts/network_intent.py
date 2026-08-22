# SPDX-License-Identifier: MIT

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / 'schemas' / 'network-intent-v1.schema.json'
EXAMPLE_PATH = ROOT / 'examples' / 'network' / 'synthetic-talk-intent.json'
SCHEMA_VERSION = 'network-intent-v1'
FAMILIES = {
    'session',
    'move',
    'interact',
    'combat',
    'talk',
    'inventory',
    'craft',
    'economy',
    'sync',
}
ALLOWED_KEYS = {
    'schema_version',
    'status',
    'direction',
    'family',
    'intent',
    'actor_id',
    'target_id',
    'client_seq',
    'idempotency_key',
    'transport',
    'payload',
    'limitations',
}
FORBIDDEN_KEYS = {
    'hp',
    'gold',
    'damage',
    'speed',
    'inventory_grant',
    'opcode',
    'endpoint',
    'host',
    'port',
}
SYNTHETIC_ID = re.compile(r'^(player|npc|object)_demo_[a-z0-9_]+$')
INTENT_NAME = re.compile(r'^[a-z][a-z0-9_]*$')


class NetworkIntentError(ValueError):
    pass


def _reject_forbidden(data: object, prefix: str = '') -> None:
    if isinstance(data, dict):
        for key, value in data.items():
            path = f'{prefix}.{key}' if prefix else key
            if key in FORBIDDEN_KEYS:
                raise NetworkIntentError(f'forbidden field: {path}')
            _reject_forbidden(value, path)
    elif isinstance(data, list):
        for index, value in enumerate(data):
            _reject_forbidden(value, f'{prefix}[{index}]')


def validate_intent(data: dict[str, object]) -> dict[str, object]:
    if not isinstance(data, dict):
        raise NetworkIntentError('intent must be an object')
    unknown = set(data) - ALLOWED_KEYS
    if unknown:
        raise NetworkIntentError(f'unknown fields: {sorted(unknown)}')
    _reject_forbidden(data)
    if data.get('schema_version') != SCHEMA_VERSION:
        raise NetworkIntentError('unknown schema_version')
    if data.get('status') not in {'observed', 'estimated', 'decision', 'unavailable'}:
        raise NetworkIntentError('invalid status')
    if data.get('direction') != 'client_to_server':
        raise NetworkIntentError('direction must be client_to_server')
    if data.get('family') not in FAMILIES:
        raise NetworkIntentError('unknown family')
    intent = data.get('intent')
    if not isinstance(intent, str) or not INTENT_NAME.fullmatch(intent):
        raise NetworkIntentError('invalid intent')
    actor_id = data.get('actor_id')
    if not isinstance(actor_id, str) or not SYNTHETIC_ID.fullmatch(actor_id):
        raise NetworkIntentError('actor_id must be a synthetic demo identifier')
    if 'target_id' in data:
        target_id = data.get('target_id')
        if not isinstance(target_id, str) or not SYNTHETIC_ID.fullmatch(target_id):
            raise NetworkIntentError('target_id must be a synthetic demo identifier')
    client_seq = data.get('client_seq')
    if not isinstance(client_seq, int) or isinstance(client_seq, bool) or client_seq < 1:
        raise NetworkIntentError('client_seq must be a positive integer')
    transport = data.get('transport')
    if not isinstance(transport, dict):
        raise NetworkIntentError('transport is required')
    if transport.get('kind') != 'documentation_fixture':
        raise NetworkIntentError('transport.kind must be documentation_fixture')
    if transport.get('tls') not in {'required_outside_loopback', 'unavailable'}:
        raise NetworkIntentError('transport.tls is invalid')
    limitations = data.get('limitations')
    if not isinstance(limitations, list) or not limitations:
        raise NetworkIntentError('limitations must be a non-empty list')
    return data


def load_example() -> dict[str, object]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding='utf-8'))
    example = json.loads(EXAMPLE_PATH.read_text(encoding='utf-8'))
    missing = set(schema.get('required', [])) - set(example)
    if missing:
        raise NetworkIntentError(f'example is missing fields: {sorted(missing)}')
    return validate_intent(example)

