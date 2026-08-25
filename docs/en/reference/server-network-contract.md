# Server Network Contract Overview

Status: **decision-documented, compatibility not validated**.

This page describes the network surface of the canonical Zig server exactly as
implemented in its current source. It exists so that client templates,
including web templates, can document what they must support before claiming
any interoperability. Describing the wire format does **not** validate a
client, an engine, or a deployment.

## Transport reality check

The canonical services speak **raw binary TCP**, not WebSocket or WebTransport:

- Login service: TCP, configured port 2106 by default.
- Game service: TCP, configured port 7777 by default.
- WebAdmin: HTTP plus WebSocket on its own port, 8082 by default, for
  administration dashboards only. It is not the player game channel.

A browser cannot connect to the login or game TCP endpoints directly. Any web
client therefore requires either a documented bridge/gateway process or a new
official WebSocket endpoint. Until one of those exists and is documented, a
browser-based MMORPG template is **not compatible** with the canonical server.
This matches the fail-closed rule of the Three.js template scope.

## Frame format

All integers are big-endian. Every message uses the same envelope:

```text
[4B total_length][2B opcode][payload]
```

- `total_length` counts everything after itself: 2 opcode bytes plus payload.
- Opcodes are u16 values from the shared message registry.
- The game event loop rejects frames whose declared length exceeds 256 KiB.
- Unknown opcodes received on the game socket are logged and ignored without
  closing the connection.

## Session flow

1. Optional account creation or guest registration on the login service.
2. Login on the login service returns a JWT session token.
3. Realm list, then realm selection, which returns the advertised game host
   and port.
4. Connection to the game service with a handshake carrying the JWT token.
5. Character listing, creation, then selection.
6. World spawn selection, then normal play.

### Key opcodes

| Opcode | Name | Direction | Purpose |
|---|---|---|---|
| 1 / 2 | handshake request/response | C<->S | Version check, JWT admission |
| 9 | time sync | C<->S | Echo 8-byte client millis, return server millis |
| 10 / 11 | login request/response | C<->S | Credentials in, JWT out |
| 20 | character create | C->S | Name, race, starter class |
| 22 / 23 | character select/list | C->S | Select by database id; bounded summaries out |
| 30 | position update | C->S | 12 bytes: three float32 coordinates |
| 80 | entity update | S->C | Delta replication batch |
| 205-208 | realm list/select | C<->S | Shard discovery and handoff target |
| 253 / 254 | heartbeat | C<->S | Keepalive with server time and tick interval |
| 255 | error message | S->C | Framed human-readable error |
| 575 / 576 | guest register | C<->S | Trial account creation without email |
| 580 | world spawn select | C<->S | Nonce-checked spawn allowlist per world |

The full registry contains several hundred opcodes covering combat, inventory,
trade, guilds, quests, housing, auctions, VR poses, and more. New client work
should begin with the subset above; the rest follows the same envelope rules.

## Handshake detail

Request payload for JWT authentication (auth type 2):

```text
[1B version_len][version string][1B capabilities]
[1B tls_required][1B auth_type][2B token_len][JWT token]
[32B asset manifest hash, only when the server expects one]
```

- Versions below 1.0.0 are rejected.
- Auth type 0 (unauthenticated) is always refused.
- Auth type 1 (password on the game socket) is deprecated; clients must log in
  through the login service first.
- When the server requires TLS, plain connections fail the handshake.
- Success response: [1B success=1][8B player_id][2B token_len=0].
- Failure response: [1B success=0][4B error_len][error text].

After a successful handshake the server pushes a session resume token
(opcode 95) as 64 hex characters, usable once to resume a dropped session.

## Login and account payloads

- Account create request (opcode 5):
  `[1B username_len][username][1B password_len][password]` followed, when
  answering a CAPTCHA challenge, by
  `[1B challenge_len][challenge][1B answer_len][answer]`.
- The server may reply with status code 2 meaning a math CAPTCHA is required;
  the challenge id and question travel inside the response.
- Login request (opcode 10):
  `[1B username_len][username][1B password_len][password]`.
- Login success response:
  `[1B success=1][8B player_id][2B token_len][JWT token]`.
- Guest registration (opcode 575) appends a 4-byte trial-days value and never
  requires CAPTCHA or license; accounts are capped (level cap, expiry).

Passwords are hashed server-side with Argon2id; passwords never appear in
responses. License possession is checked against the database before a token
is issued, and maintenance mode blocks both login and handshake.

## Replication batch (opcode 80)

```text
[2B entity_count]
repeated entity_count times:
    [4B delta_size][delta]
delta:
    [8B entity_id][1B field_count]
    repeated field_count times:
        [1B field_id][4B big-endian value]
```

Field ids currently emitted include position X/Y/Z (1-3), velocity X/Z (4, 6),
facing rotation Y (7), and health (10). Values for positions and rotations are
bit-cast float32; health is an unsigned integer count. A client interpolates
between batches; it must never extrapolate authority.

## Authority rules

- Identity, role, license state, inventory, gold, health, speed, and movement
  outcomes are decided server-side only.
- Client-sent roles are treated as untrusted hints and replaced by the
  database value.
- Position updates are validated against world bounds and anti-cheat checks
  before acceptance.
- Spawn placement comes from server-side spawn tables; clients select among
  allowlisted worlds using a nonce, never arbitrary coordinates.

## Compatibility evidence still missing

- No official WebSocket or WebTransport endpoint exists in the canonical
  server today.
- No bridge/gateway specification has been published.
- No browser client has completed a loopback fixture against these binaries.

Until all three change with named evidence, this page remains a description of
the server, not proof of any client compatibility.
