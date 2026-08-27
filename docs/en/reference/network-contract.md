# Network contract

Status: public authority contract plus a versioned documentation fixture.
Canonical message identifiers, binary layouts, and live version numbers remain
`unavailable` until a protocol publication gate passes. This page is enough to
design a client or tool without cloning the unpublished server.

## Tick and coherence model

```text
client tick                server tick
  sample input               consume intents
  send intent                validate / simulate
  apply last ack             persist required state
  predict locally            replicate diffs
  reconcile on diff          drop unauthorized fields
```

Public rules:

- the server tick is authoritative;
- clients may predict movement for comfort and must reconcile;
- replication is interest-based: a client receives what it is allowed to see;
- state diffs and delta compression are server-owned optimizations, not a
  license to send full world snapshots from the client;
- exact tick rates remain `unavailable`.

## Intent families

A future protocol SHOULD group client-to-server intents by family rather than
by engine:

| Family | Typical intent | Server must validate |
|---|---|---|
| Session | login, logout, realm handoff, reconnect | identity, expiry, realm membership |
| Move | walk, stop, jump, teleport request | speed, collision, zone, anti-cheat |
| Interact | use object, talk, pick up, trade start | range, ownership, cooldowns |
| Combat | attack, cast, block, cancel | resources, line of rules, immunities |
| Talk | say, emote, NPC dialogue choice | mute, length, NPC availability |
| Inventory | equip, move, drop, consume | ownership, weight, bindings |
| Craft / economy | craft, buy, sell, mail | recipes, funds, fraud rules |
| Sync | ack, ping, view-target | timing only, no state mutation |

Names above are documentation families. They are not published opcodes.
Inventing a binary packet from this table would be incorrect.

## Payload rules

- JSON templates may describe content; live transport may be JSON, binary, or
  both. The unpublished implementation is not implied.
- numbers that affect gameplay must be typed and unit-explicit when they
  appear in templates: `duration_ms`, `distance_m`, `cooldown_seconds`.
- clients send intents and presentation hints, never HP, gold, or grants;
- unknown fields must be ignored for presentation and rejected for security;
- documentation examples use synthetic names only.

## Versioned documentation fixture

The structured source is
[`schemas/network-intent-v1.schema.json`](../../../schemas/network-intent-v1.schema.json).
A synthetic example lives at
[`examples/network/synthetic-talk-intent.json`](../../../examples/network/synthetic-talk-intent.json).

This fixture is `estimated`. It records family, intent, synthetic actor ids,
a client sequence, and an idempotency key. It is not a captured packet and
not a published opcode.

Consumers must:

- reject unknown `schema_version` values;
- reject `hp`, `gold`, `damage`, `speed`, grants, opcodes, hosts, and ports;
- use only `*_demo_*` identifiers;
- treat a matching JSON shape as documentation, not server compatibility.

Validate the example with the repository checks. A dedicated helper is
`scripts/network_intent.py`.

Illustrative JSON, now backed by the v1 fixture:

```json
{
  "schema_version": "network-intent-v1",
  "family": "talk",
  "intent": "talk",
  "actor_id": "player_demo_01",
  "target_id": "npc_demo_gatekeeper_01",
  "client_seq": 42
}
```

The server may answer with an accepted event, a rejected intent, or a state
diff. The client must not retry a rejected mutation as if it had succeeded.

## Timeouts, retries, and anti-cheat

- a missing ack is not permission to apply the local prediction permanently;
- retries must be idempotent by client sequence or server-issued id;
- duplicate intents must not duplicate gold, items, or damage;
- movement that exceeds validated speed, ignores collision, or shows impossible
  entropy is rejected;
- rate limits apply per session and per intent family;
- TLS is expected outside loopback. Loopback fixtures still use synthetic
  credentials.

Exact thresholds, entropy windows, and certificate pins remain `unavailable`.

## Compatibility gate

The public client starters currently mark Zig server alignment as blocked.
A third-party client is unsupported until the evidence listed in those
repositories exists. See [server architecture](../explanation/server-architecture.md).
