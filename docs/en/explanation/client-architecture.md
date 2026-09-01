# Client architecture

Status: `decision` for authority boundaries and `evidence-tracked` for public starter maturity. Live sockets to the canonical Zig server remain **unproven** until an exact server baseline and real E2E evidence are recorded.

## Current client state

| Profile | Public repository | Current verifiable state |
|---|---|---|
| Godot VR MMORPG | `ultod-client-godot-vr-mmorpg-template` | OpenXR shell; historical Godot 4.3 metadata; 4.7.2 target not proven; historical networking `LEGACY_QUARANTINED`; socket-free intent/transport layers plus deterministic synthetic transport **prepared and CI-guarded**, runtime fixture not yet executed |
| Godot Classic 3D | `ultod-client-godot-classic-3d-mmorpg-template` | desktop 3D shell; historical Godot 4.3 metadata; 4.7.2 target not proven; socket-free intent/transport layers plus deterministic synthetic transport **prepared and CI-guarded**, runtime fixture not yet executed |
| Three.js 2.5D | `ultod-client-threejs-2-5d-mmorpg-template` | Vite/TypeScript app; fail-closed `NetworkClient`; synthetic transport fixture/tests executed and validated; proof level `SYNTHETIC_FIXTURE_ONLY`, real Zig compatibility `NOT_PROVEN` |
| FoveaCore FPS-RPG | `ultod-client-foveacore-fps-rpg-template` | specialized foundation under construction; do not infer Zig compatibility |
| NetherCore ARPG (Three.js) | `ultod-client-threejs-nethercore-arpg-template` | Web ARPG presentation; no inherited compatibility claim from the 2.5D client |

Unity is **LEGACY** and no longer an active Ultimate Odycer development target.

Existing proprietary Ultimate Odycer client/server implementation must not be imported into public starters without file-level provenance and license review.

## Current public network structure

The Godot P0 starters now separate:

```text
input / OpenXR / desktop
        |
        v
net/intent_contract.gd
  bounded client validation
  session / move / interact / talk
        |
        v
net/transport_adapter.gd
  abstract lifecycle
  disconnected / connecting / authenticating / online
        |
        v
net/synthetic_transport.gd
  deterministic socket-free test authority
  PREPARED / CI-GUARDED
  runtime execution still pending
        |
        v
future real transport adapter
  BLOCKED until exact Zig baseline + real E2E proof
```

The public intent layer rejects client-authority fields such as damage, currency, inventory, permissions, arbitrary teleport, and server position. Client-side defense never replaces Zig validation.

The Godot synthetic fixture includes explicit offline failure, authentication gating, malformed/authority-field rejection, sanitized movement, connection drop, reconnect/resume, and close behavior. Its maximum allowed result remains `SYNTHETIC_FIXTURE_ONLY`. Hosted documentation CI checks the fixture structure and proof boundaries but **does not execute Godot**.

For VR, the prepared synthetic runner uses `--xr-mode off`; OpenXR runtime, headset/controllers, VR-specific pose/grab/release networking, and Zig interoperability remain independent unproven gates.

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
authoritative server or explicitly synthetic test authority
        v
state diff / accepted or rejected event
        v
presentation, interpolation, LOD, audio, haptics
```

The client never decides damage, gold, inventory, rewards, permissions, or persistent world state.

## Proof levels that must not be conflated

- `DOCUMENTED` / `DECLARED`: documentation or metadata only;
- `PREPARED_CI_GUARDED`: implementation exists and static/structural gates pass, but the runtime scenario has not executed;
- `SYNTHETIC_FIXTURE_ONLY`: controlled fixture actually executed, no canonical Zig server;
- `ENGINE_LOAD_PROVEN`: named engine loads the project; does not prove networking;
- `OPENXR_INIT_PROVEN`: named OpenXR runtime initializes; does not prove headset or networking;
- `HEADSET_RUNTIME_PROVEN`: named headset/controllers execute the scenario; does not prove server interoperability;
- `REAL_SERVER_E2E`: exact client/server revisions with reproducible scenario;
- `FAKE-GREEN`: a green test used to claim more than the system it actually exercises.

## Connection path

Public documentation contains two layers that agents must distinguish:

1. `network-intent-v1` is a public synthetic, transport-independent contract;
2. `server-network-contract.md` is an **unpinned implementation snapshot**, not a verified current protocol and not client compatibility proof.

The historical snapshot described raw binary TCP for login/game. Until those details are tied to an exact current Zig SHA/tree/toolchain, agents must treat the current transport as unverified. In particular, a browser client must not invent or assume a player WebSocket endpoint; a bridge/gateway or separate official endpoint requires its own named proof.

## Agent rule

Before modifying a client:

1. read this page;
2. read `../reference/network-contract.md`;
3. read `../reference/server-network-contract.md` while preserving its unpinned/non-validated status;
4. read the engine/template matrix;
5. read the proof-level and compatibility-manifest files in the target client repository;
6. distinguish prepared/CI-guarded fixtures from executed runtime receipts;
7. never promote `zig_compatibility`, Godot 4.7.2, OpenXR, headset, or synthetic runtime status without the matching executable receipt.

## Related pages

- [Ecosystem overview](ecosystem-overview.md)
- [Public network contract](../reference/network-contract.md)
- [Unpinned server network snapshot](../reference/server-network-contract.md)
- [Engine, template, and world matrix](../reference/engine-template-world-matrix.md)
