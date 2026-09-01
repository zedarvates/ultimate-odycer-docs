# Engine, template, and world-shape matrix

This reference helps a human or LLM choose a starting point without turning a preference into a compatibility promise.

## Engines

| Engine | Role | Current limitation |
|---|---|---|
| Godot | primary 3D/VR path | 4.7.2 target; executable engine proof pending; live Zig networking unproven |
| Three.js | lightweight Web client + protocol test bench | synthetic fixture proven; browser ↔ canonical Zig live path unproven |
| Unity | `LEGACY` only | no longer an active development target |
| FoveaCore | specialized FPS/RPG path | foundation under construction |
| Unreal Engine | external alternative | no validated Ultimate Odycer template |

## Maturity scale

`PROVEN` means reproducible evidence against named revisions. `IMPLEMENTED` is code without complete proof. `PARTIAL` is incomplete. `MOCK` is simulated. `SCAFFOLD` is structure only. `DECLARED` is documentation/metadata. `LEGACY` is historical reuse-only. `BLOCKED` means required evidence is inaccessible. `WAITING` means a prerequisite is open. `FAKE-GREEN` is a green test used to claim more than it exercises.

## Current P0 client/server matrix

| Component | Presentation | Intent contract | Abstract/synthetic transport | Canonical Zig live | Status |
|---|---:|---:|---:|---:|---|
| Three.js 2.5D | yes | yes | **synthetic fixture + NetworkClient validated** | `NOT_PROVEN` | `IMPLEMENTED/PARTIAL` |
| Godot Classic | yes | yes, socket-free | abstract socket-free adapter; synthetic fixture next | `NOT_PROVEN` | `PARTIAL` |
| Godot VR | yes | yes, socket-free | abstract socket-free adapter; historical network `LEGACY_QUARANTINED` | `NOT_PROVEN` | `PARTIAL` |
| private Zig server | n/a public | target authority source | transport documented but exact baseline must be recaptured | target source of truth | `BLOCKED` for proof promotion |
| private WebAdmin | yes | n/a | separate admin HTTP/WS, not player channel | fail-closed P0 audit in progress | `PARTIAL / evidence-tracked` |

### Godot 4.7.2 / VR

The Godot P0 PRs include local validators that can write JSON receipts under `.evidence/`:

- Classic: import + headless bootstrap with **Godot 4.7.2-stable**;
- VR: the same engine proof with `--xr-mode off`; the receipt explicitly leaves `openxr_runtime_proven=false`, `headset_runtime_proven=false`, and `network_compatibility_proven=false`.

Until those commands run against the exact binary, `project.godot` remains historically declared as 4.3 and the 4.7.2 target remains `NOT_PROVEN`.

### Three.js

The current synthetic gate validates the built client, transport controls, and negative fixtures. Its proof level remains `SYNTHETIC_FIXTURE_ONLY`; it does not prove a round trip with `zig-server-v2`.

### Server transport

`server-network-contract.md` currently describes login/game as **raw binary TCP**. A browser must not assume a player WebSocket endpoint. Three.js therefore needs a documented bridge/gateway or separate official endpoint before live proof. That server description must itself be tied to an exact Zig baseline before promotion to a verified canonical contract.

## P0 program

Public tracker `ultimate-odycer-feedback`:

- `#5` exact Zig baseline and protocol/versioning;
- `#6` real Zig ↔ Three.js proof;
- `#7` same proof in Godot Classic/VR;
- `#8` fuzzing, anti-replay, anti-duplication;
- `#9` crash-safe persistence/snapshot/restore;
- `#10` deterministic social simulation + AI LOD;
- `#11` public/open-source ↔ private/commercial license boundary.

The private WebAdmin also tracks Zig provenance, read-only contract proof, and quarantined mutations separately.

## Agent rules

Before changing client/network code:

1. never use a document date as technical proof;
2. read the target repository proof levels and compatibility manifest;
3. keep synthetic data explicitly synthetic;
4. never copy the historical VR network without provenance/license/security review;
5. never invent a player WebSocket for Three.js;
6. never promote Godot 4.7.2, OpenXR, headset, or Zig status without the matching executable receipt;
7. preserve licensing: public material uses its explicit public license; private server/gameplay/production configuration remains proprietary/commercial, all rights reserved unless explicitly stated otherwise.

## Templates

| Repository | Experience | Current state |
|---|---|---|
| `ultod-client-godot-classic-3d-mmorpg-template` | Classic 3D MMORPG | `PARTIAL / engine+network proof pending` |
| `ultod-client-godot-vr-mmorpg-template` | VR MMORPG | `PARTIAL / legacy network quarantined` |
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
