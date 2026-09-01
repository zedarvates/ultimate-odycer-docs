# Server Network Contract Overview

Status: **unpinned implementation snapshot — compatibility not validated**.

This page must no longer be read as “the current canonical protocol.” Historically documented transport/opcode details must be **revalidated against an exact `zig-server-v2` baseline** before reuse in a client, SDK, gateway, or compatibility claim.

## Stable public authority decisions

- The server is authoritative for identity/session, movement, combat, inventory, economy, permissions, and persistence.
- Clients send intents; they never decide damage, gold, inventory, or persistent outcomes.
- Authentication, handoff, versioning, framing, replication, reconnect, and transport must be bounded and tested.
- TLS is expected outside loopback according to approved configuration.
- Invalid, unknown, oversized, or replayed input must neither mutate authoritative state nor crash a shard.

## Historically documented transport state

A previous documentation revision described login/game services as **raw binary TCP** and WebAdmin as HTTP/WebSocket separate from the player game channel. That information is retained only as a **baseline clue to verify**.

It does not prove today that:

- historical ports remain unchanged;
- historical opcodes are still valid;
- historical framing is still canonical;
- historical handshake/JWT/resume behavior is unchanged;
- a player WebSocket bridge/endpoint exists;
- any public client is compatible.

## Required baseline before promotion

Promotion to `VERIFIED_SERVER_CONTRACT` requires a private receipt containing at least:

- exact monorepo Git SHA;
- exact `zig-server-v2` tree object;
- clean subtree state;
- Zig version/toolchain;
- handler/message inventory at the same revision;
- reproducible tests supporting every published claim.

Sensitive or proprietary details do not need to be published to provide this proof. Public documentation should expose only the explicitly approved subset.

## Three.js

Until a browser endpoint is proven, the Three.js client remains fail-closed. It must never reuse WebAdmin WebSocket traffic for gameplay or invent a player endpoint.

## Godot

Classic and VR must keep their abstract socket-free transport adapter until the exact Zig baseline is captured and the transport contract is approved. Historical VR networking remains `LEGACY_QUARANTINED`.

## Public reference usable today

For development without depending on an unpinned/proprietary wire protocol, use [`network-contract.md`](network-contract.md) and `network-intent-v1`. They define authority and transport-independent synthetic fixtures without claiming live interoperability.
