# Client architecture

Status: `decision` for authority boundaries and `evidence-tracked` for public starter maturity. Live sockets to the canonical Zig server remain **unproven** until an exact server baseline and real E2E evidence are recorded.

## Current client state

| Profile | Public repository | Current verifiable state |
|---|---|---|
| Godot VR MMORPG | `ultod-client-godot-vr-mmorpg-template` | OpenXR shell; historical Godot 4.3 project metadata; 4.7.2 target not yet proven; historical networking `LEGACY_QUARANTINED`; transport-independent intent contract + abstract transport adapter present on the P0 PR |
| Godot Classic 3D | `ultod-client-godot-classic-3d-mmorpg-template` | desktop 3D shell; historical Godot 4.3 project metadata; 4.7.2 target not yet proven; transport-independent intent contract + abstract transport adapter present on the P0 PR |
| Three.js 2.5D | `ultod-client-threejs-2-5d-mmorpg-template` | Vite/TypeScript app; fail-closed `NetworkClient`; synthetic transport fixture/tests validated; proof level `SYNTHETIC_FIXTURE_ONLY`, real Zig compatibility `NOT_PROVEN` |
| FoveaCore FPS-RPG | `ultod-client-foveacore-fps-rpg-template` | specialized foundation under construction; do not infer Zig compatibility |
| NetherCore ARPG (Three.js) | `ultod-client-threejs-nethercore-arpg-template` | Web ARPG presentation; do not inherit compatibility claims from the Three.js 2.5D client |

Unity is **LEGACY** and is no longer an active Ultimate Odycer development target.

Existing proprietary Ultimate Odycer client/server implementation must not be imported into public starters without file-level provenance and license review.

## Current public network structure

The Godot P0 starters now separate:

```text
input / OpenXR / desktop
        |
        v
net/intent_contract.gd
  bounded client validation
  families: session / move / interact / talk
        |
        v
net/transport_adapter.gd
  abstract lifecycle: disconnected / connecting / authenticating / online
  no socket, endpoint, opcode, or private Zig framing
        |
        v
future real transport adapter
  BLOCKED until exact Zig baseline + real E2E proof
```

The public intent layer rejects client-authority fields such as damage, currency, inventory, permissions, arbitrary teleport, and server position. Client-side defense never replaces Zig validation.

Three.js already has a testable synthetic transport. That does not mean a browser can directly connect to the current Zig game transport.

## Presentation versus authority

```text
OpenXR / desktop / Web input
        |
        v
local pose, comfort locomotion, prediction
        |  discarded/reconciled if server rejects it
        v
bounded client intent
        v
authoritative server
        v
state diff / accepted or rejected event
        v
presentation, interpolation, LOD, audio, haptics
```

The client never decides damage, gold, inventory, rewards, permissions, or persistent world state.

## Proof levels that must not be conflated

- `DOCUMENTED` / `DECLARED`: documentation or metadata only;
- `SYNTHETIC_FIXTURE_ONLY`: controlled local fixture, no canonical Zig server;
- `ENGINE_LOAD_PROVEN`: named engine loads the project; does not prove networking;
- `OPENXR_INIT_PROVEN`: named OpenXR runtime initializes; does not prove headset or networking;
- `HEADSET_RUNTIME_PROVEN`: named headset/controllers execute the scenario; does not prove server interoperability;
- `REAL_SERVER_E2E`: exact client/server revisions with reproducible scenario;
- `FAKE-GREEN`: a green test used to claim more than the system it actually exercises.

## Connection path

Public documentation currently contains two layers that agents must distinguish:

1. `network-intent-v1` is a public synthetic, transport-independent contract;
2. `server-network-contract.md` documents a server transport state derived from implementation decisions, but **is not client compatibility proof** and must be revalidated against the exact Zig baseline before promotion.

In particular, the Three.js browser client must not assume that a player WebSocket endpoint exists. The currently documented game transport is raw binary TCP; a browser therefore needs a bridge/gateway or a separate official endpoint, both still requiring proof.

## Agent rule

Before modifying a client:

1. read this page;
2. read `../reference/network-contract.md`;
3. read `../reference/server-network-contract.md` while preserving its non-validated status;
4. read the engine/template matrix;
5. read the proof-level and compatibility-manifest files in the target client repository;
6. never promote `zig_compatibility`, Godot 4.7.2, OpenXR, or headset status to `PROVEN` without the matching executable receipt.

## Related pages

- [Ecosystem overview](ecosystem-overview.md)
- [Public network contract](../reference/network-contract.md)
- [Documented server network contract](../reference/server-network-contract.md)
- [Engine, template, and world matrix](../reference/engine-template-world-matrix.md)
