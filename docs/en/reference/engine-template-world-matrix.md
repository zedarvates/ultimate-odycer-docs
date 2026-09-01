# Engine, template, and world-shape matrix

This reference helps a human or LLM choose a starting point without turning a preference into a compatibility promise.

## Engines

| Engine | Role | Current limitation |
|---|---|---|
| Godot | primary 3D/VR path | 4.7.2 target; engine execution pending; synthetic fixture prepared/CI-guarded but not runtime-proven; live Zig networking unproven |
| Three.js | lightweight Web client + protocol test bench | synthetic fixture actually executed/proven; browser ↔ canonical Zig live path unproven |
| Unity | `LEGACY` only | no longer an active development target |
| FoveaCore | specialized FPS/RPG path | foundation under construction |
| Unreal Engine | external alternative | no validated Ultimate Odycer template |

## Maturity scale

`PROVEN` means reproducible evidence against named revisions. `IMPLEMENTED` is code without complete proof. `PARTIAL` is incomplete. `MOCK` is simulated. `SCAFFOLD` is structure only. `DECLARED` is documentation/metadata. `PREPARED_CI_GUARDED` means implementation exists and structural gates pass but runtime proof has not executed. `LEGACY` is historical reuse-only. `BLOCKED` means required evidence is inaccessible. `WAITING` means a prerequisite is open. `FAKE-GREEN` is a green test used to claim more than it exercises.

## Current P0 client/server matrix

| Component | Presentation | Intent contract | Abstract/synthetic transport | Canonical Zig live | Status |
|---|---:|---:|---:|---:|---|
| Three.js 2.5D | yes | yes | **synthetic fixture + NetworkClient executed and validated** | `NOT_PROVEN` | `IMPLEMENTED/PARTIAL` |
| Godot Classic | yes | yes, socket-free | abstract adapter + deterministic fixture `PREPARED_CI_GUARDED`; runtime `NOT_YET_EXECUTED` | `NOT_PROVEN` | `PARTIAL` |
| Godot VR | yes | yes, socket-free | same prepared fixture with XR off; historical network `LEGACY_QUARANTINED`; runtime `NOT_YET_EXECUTED` | `NOT_PROVEN` | `PARTIAL` |
| private Zig server | n/a public | target authority source | current exact transport/protocol baseline not pinned | target source of truth | `BLOCKED` for proof promotion |
| private WebAdmin | yes | n/a | separate admin surface; fail-closed P0 audit | exact Zig contract proof pending | `PARTIAL / evidence-tracked` |

### Godot synthetic proof preparation

Both Godot P0 branches now contain:

- bounded base intent validation;
- an abstract socket-free transport lifecycle;
- a deterministic socket-free synthetic authority;
- a GDScript scenario covering offline/auth/failure/authority-field/movement/drop/resume/close behavior;
- a Python runner requiring exact Godot 4.7.2 and writing a `.evidence/` JSON receipt.

Their hosted CI validates only structure, proof-denial markers and Python syntax. It does **not** execute Godot, so the runtime state remains `NOT_YET_EXECUTED` and may not be promoted to `SYNTHETIC_FIXTURE_ONLY` until the runner actually succeeds.

For VR, that prepared runner uses `--xr-mode off`; OpenXR/headset proof remains separate and false.

### Godot 4.7.2 / VR

The engine validators can produce independent receipts:

- Classic: import + headless bootstrap under Godot 4.7.2-stable;
- VR: same with `--xr-mode off`, explicitly keeping OpenXR/headset/network proof false.

Until the exact commands execute successfully, project metadata remains historically 4.3 and 4.7.2 remains `NOT_PROVEN`.

### Three.js

Three.js has a genuinely executed synthetic transport gate. Its proof level remains `SYNTHETIC_FIXTURE_ONLY`; it does not prove a round trip with `zig-server-v2`.

### Server transport

`server-network-contract.md` is now an **unpinned implementation snapshot**. A historical snapshot described raw binary TCP, but the current transport/protocol is not verified until tied to an exact current Zig SHA/tree/toolchain. A browser must therefore never assume a player WebSocket endpoint; any bridge/gateway or official endpoint requires separate evidence.

## P0 program

Public tracker `ultimate-odycer-feedback`:

- `#5` exact Zig baseline and protocol/versioning;
- `#6` real Zig ↔ Three.js proof;
- `#7` same proof in Godot Classic/VR;
- `#8` fuzzing, anti-replay, anti-duplication;
- `#9` crash-safe persistence/snapshot/restore;
- `#10` deterministic social simulation + AI LOD;
- `#11` public/open-source ↔ private/commercial license boundary.

## Agent rules

Before changing client/network code:

1. do not use document freshness as proof;
2. read proof levels and compatibility manifest in the target repository;
3. distinguish prepared/static-gated fixtures from executed runtime evidence;
4. keep synthetic data explicitly synthetic;
5. never copy the historical VR network without provenance/license/security review;
6. never invent a player WebSocket for Three.js;
7. never promote Godot 4.7.2, synthetic runtime, OpenXR, headset, or Zig without the matching executable receipt;
8. preserve public-license vs private proprietary/commercial boundaries.

## Templates

| Repository | Experience | Current state |
|---|---|---|
| `ultod-client-godot-classic-3d-mmorpg-template` | Classic 3D MMORPG | `PARTIAL / synthetic fixture PREPARED_CI_GUARDED / runtime pending` |
| `ultod-client-godot-vr-mmorpg-template` | VR MMORPG | `PARTIAL / synthetic fixture PREPARED_CI_GUARDED / legacy network quarantined` |
| `ultod-client-threejs-2-5d-mmorpg-template` | 2.5D Web MMORPG | `IMPLEMENTED presentation / SYNTHETIC_FIXTURE_ONLY` |
| `ultod-client-foveacore-fps-rpg-template` | FPS/RPG | `under_construction` |
| `ultod-client-threejs-nethercore-arpg-template` | Web ARPG | separate presentation; no inherited compatibility claim |

## World shapes

| Topology | Use it for | Starting cost |
|---|---|---|
| `flat_map` | cities, regions, arenas, dungeons | low |
| `planet` | continuous planetary exploration | high |
| `mega_planet` | very large planet | very high |
| `solar_system` | multiple bodies and travel | highest |

World-shape choices do not weaken network, persistence, or security proof gates.
