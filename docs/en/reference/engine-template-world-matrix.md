# Engine, template, and world-shape matrix

This reference helps a human or LLM recommend a starting point without turning
a preference into a compatibility promise.

## Engines

| Engine | Role in the journey | Current limitation |
|---|---|---|
| Godot | Primary recommended path for 3D/VR clients | Public shells exist; real canonical Zig interoperability still needs P0 proof |
| Three.js | Lightweight Web client and reference protocol test bench | Public shell + local fixture exist; exact canonical Zig connection still needs proof |
| Unity | Legacy only | Previous Ultimate Odycer architecture; no longer an active development target |
| Unreal Engine | External alternative | No validated Ultimate Odycer template |
| FoveaCore | Specialized FPS/RPG path | Foundation under construction |

## Maturity scale

| State | Meaning |
|---|---|
| `PROVEN` | reproducible evidence against named server/client revisions |
| `IMPLEMENTED` | implemented but not fully proven |
| `PARTIAL` | incomplete implementation |
| `MOCK` | simulated/fake data or service |
| `SCAFFOLD` | structure/presentation shell only |
| `DECLARED` | documentation or declarative data only |
| `LEGACY` | old architecture retained only for history or targeted recovery |
| `BLOCKED` | required evidence/dependency unavailable |
| `WAITING` | work identified but a prerequisite is not closed |
| `FAKE-GREEN` | a green test that does not exercise the real system it appears to prove |

## Current client/server matrix

| Repository / component | Local presentation | Synthetic fixture | Canonical Zig live | Negative security | Global state |
|---|---:|---:|---:|---:|---|
| `ultod-client-threejs-2-5d-mmorpg-template` | yes | yes | `WAITING` for exact baseline + E2E proof | `WAITING` | `IMPLEMENTED/PARTIAL` |
| `ultod-client-godot-classic-3d-mmorpg-template` | yes | `WAITING` | `BLOCKED/WAITING` | `WAITING` | `SCAFFOLD/PARTIAL` |
| `ultod-client-godot-vr-mmorpg-template` | yes | `WAITING` | `BLOCKED`; old VR contract = `LEGACY` | `WAITING` | `SCAFFOLD/PARTIAL` |
| private canonical Zig server | not public | partially documented evidence | target source of truth | audit pending | `BLOCKED` for direct public proof until exact SHA is recovered |

P0 program tracked in `zedarvates/ultimate-odycer-feedback`:

- `#5` — freeze the canonical Zig revision, framing, version negotiation, and compatibility matrix;
- `#6` — prove the real Zig ↔ Three.js authoritative round trip;
- `#7` — replay the same canonical fixture from Godot Classic and Godot VR;
- `#8` — paranoid protocol security, fuzzing, anti-replay, and anti-duplication;
- `#9` — crash-safe persistence, snapshot, and restore;
- `#10` — deterministic social simulation and AI LOD after the P0 foundations;
- `#11` — private commercial ↔ public open-source license boundary.

No component receives `PROVEN` status without exact revisions and reproducible evidence. A synthetic fixture alone does not prove compatibility with the canonical server.

## Planned or under-construction templates

| Repository | Display name | Experience | Status |
|---|---|---|---|
| `ultod-client-godot-classic-3d-mmorpg-template` | Godot Classic 3D MMORPG | Classic 3D MMORPG | `partial / P0 interoperability waiting` |
| `ultod-client-godot-vr-mmorpg-template` | Godot VR MMORPG | Virtual-reality MMORPG | `partial / Zig alignment blocked` |
| `ultod-client-threejs-2-5d-mmorpg-template` | Three.js 2.5D MMORPG | Isometric Web MMORPG | `implemented presentation / canonical E2E waiting` |
| `ultod-client-foveacore-fps-rpg-template` | FoveaCore FPS-RPG Online | Online FPS/RPG | `under_construction` |
| `ultod-client-godot-open-city-crime-rpg-template` | Prêt à tout faire pour de l'argent | Open-city multiplayer RPG | `planned` |

A documentation-only repository or presentation shell is not a compatible MMO client until the authoritative network path is proven.

## License boundary

Public templates may contain only original code explicitly released under their public license and compatible third-party dependencies. The private canonical server, proprietary gameplay implementation, production configuration, private assets/lore, and commercial components remain proprietary/commercial, all rights reserved unless an explicit license says otherwise. Access to a private repository does not authorize copying implementation into a public repository. Any private → public extraction requires file-level provenance/license review; independently written adapters against approved public contracts and synthetic fixtures are preferred.

## World shapes

| Topology | Choose it for | Starting cost |
|---|---|---|
| `flat_map` | cities, regions, arenas, dungeons, urban games | lowest |
| `planet` | continuous exploration of one planet | high |
| `mega_planet` | a very large planet | very high |
| `solar_system` | travel between multiple bodies | highest |

## Drawn inputs and conversion

| Input | Processing | Output | Integration |
|---|---|---|---|
| Paper, PNG, JPEG, or SVG with legend | Human/LLM analysis preserving uncertainty | `uo.map-intent/v1` | `reference_only` then `conversion_required` |
| GeoJSON or QGIS layers | Scale, projection, and attribution checks | versioned world proposal | `conversion_required` |
| Blender blockout or GLB | Units, collision, LOD, and license review | 3D candidate | `conversion_required` |
| CityConfig Lite | City Editor Lite | bounded city proposal | `direct` to the Lite contract, not runtime |
| HouseBlueprint Lite | Architecture Editor Lite | building proposal | `direct` to the Lite contract, not runtime |
| XenoGenome Lite | Creature Editor Lite | creature proposal | `direct` to the Lite contract, server stats unchanged |

The listed Lite editors are `executable_public` for their public contracts and
tests. Their previews remain `[Scaffolding / Proxy]` and prove neither Godot,
Zig, VR, nor server publication.

## Recommendation rules

1. Choose the gameplay loop before the world size.
2. Use Godot unless a constraint requires another engine.
3. Use Three.js as the lightweight Web client and fast protocol test bench when it shortens validation.
4. Start with `flat_map` for an urban game, arena, or dungeon.
5. Choose `planet` only when spherical continuity is essential to the first prototype.
6. Treat `mega_planet` and `solar_system` as advanced stages requiring proof of streaming, partitioning, persistence, and capacity.
7. An LLM recommends; the user decides and records the decision in the brief.

## Intrinsic choices, not automatic ones

A GTA-like project will usually lead to a flat map, but this is not a law. A
space game can begin on a station represented by a flat map before adding a
solar system. The guide explains the trade-off instead of selecting the most
spectacular architecture by default.
