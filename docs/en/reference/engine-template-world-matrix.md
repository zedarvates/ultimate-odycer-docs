# Engine, template, and world-shape matrix

This reference helps a human or LLM recommend a starting point without turning
a preference into a compatibility promise.

## Engines

| Engine | Role in the journey | Current limitation |
|---|---|---|
| Godot | Recommended and fully documented path | Public templates remain under construction |
| Three.js | Web alternative | Networking adaptation and the 2.5D experience need validation |
| Unity | Alternative | No validated Ultimate Odycer template |
| Unreal Engine | Alternative | No validated Ultimate Odycer template |
| FoveaCore | Specialized FPS/RPG path | Foundation under construction |

## Planned or under-construction templates

| Repository | Display name | Experience | Status |
|---|---|---|---|
| `ultod-client-godot-classic-3d-mmorpg-template` | Godot Classic 3D MMORPG | Classic 3D MMORPG | `under_construction` |
| `ultod-client-godot-vr-mmorpg-template` | Godot VR MMORPG | Virtual-reality MMORPG | `under_construction` |
| `ultod-client-threejs-2-5d-mmorpg-template` | Three.js 2.5D MMORPG | Isometric Web MMORPG | `under_construction` |
| `ultod-client-foveacore-fps-rpg-template` | FoveaCore FPS-RPG Online | Online FPS/RPG | `under_construction` |
| `ultod-client-godot-open-city-crime-rpg-template` | Prêt à tout faire pour de l'argent | Open-city multiplayer RPG | `planned` |

A documentation-only repository without client code is a design direction, not
a playable client.

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
3. Start with `flat_map` for an urban game, arena, or dungeon.
4. Choose `planet` only when spherical continuity is essential to the first
   prototype.
5. Treat `mega_planet` and `solar_system` as advanced stages requiring proof of
   streaming, partitioning, persistence, and capacity.
6. An LLM recommends; the user decides and records the decision in the brief.

## Intrinsic choices, not automatic ones

A GTA-like project will usually lead to a flat map, but this is not a law. A
space game can begin on a station represented by a flat map before adding a
solar system. The guide explains the trade-off instead of selecting the most
spectacular architecture by default.
