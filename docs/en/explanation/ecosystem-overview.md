# Ultimate Odycer ecosystem overview

This repository is the public documentation hub for Ultimate Odycer. It explains
how the public pieces fit together, what they currently cover, and what they
do not cover.

It is not a substitute for a published server, a playable client, or a certified
protocol. Those remain separate publication gates.

## What this repository covers

- bilingual home-lab NPC capacity tutorials and hardware guides;
- the public design philosophy and hybrid server / LLM / ESP32 boundary;
- the public architecture of the open ecosystem;
- contracts that an independent developer can use without proprietary source:
  JSON templates, client starter boundaries, network authority rules, and
  gameplay authoring conventions.

## What this repository does not cover

- proprietary Zig server source, private APIs, or production endpoints;
- a playable Godot, Three.js, or FoveaCore client;
- canonical network message identifiers, framing, or serialization;
- hosted infrastructure, billing, moderation tooling, or player data;
- certified compatibility between a named client version and a named server
  version.

Missing evidence is `unavailable`, not implied support.

## Official public repositories

| Repository | Role | Maturity | Compatibility |
|---|---|---|---|
| [ultimate-odycer-docs](https://github.com/zedarvates/ultimate-odycer-docs) | Public documentation hub | Public, bilingual, validated for structure | Documentation only |
| [ultod-json-template-registry](https://github.com/zedarvates/ultod-json-template-registry) | Versioned JSON templates and schemas | Experimental snapshots at `0.1.0` | Compatibility lists are empty until proven |
| [ultod-client-godot-vr-mmorpg-template](https://github.com/zedarvates/ultod-client-godot-vr-mmorpg-template) | Future Godot VR MMORPG starter | Documentation-only foundation | Server alignment blocked |
| [ultod-client-godot-classic-3d-mmorpg-template](https://github.com/zedarvates/ultod-client-godot-classic-3d-mmorpg-template) | Future Godot Classic 3D starter | Documentation-only foundation | Server alignment blocked |
| [ultod-client-threejs-2-5d-mmorpg-template](https://github.com/zedarvates/ultod-client-threejs-2-5d-mmorpg-template) | Future Three.js 2.5D starter | Documentation-only foundation | Server alignment blocked |
| [ultod-client-foveacore-fps-rpg-template](https://github.com/zedarvates/ultod-client-foveacore-fps-rpg-template) | Future FoveaCore FPS-RPG starter | Documentation-only foundation | Server alignment blocked |
| [ultimate-odycer-feedback](https://github.com/zedarvates/ultimate-odycer-feedback) | Public bug and suggestion tracker | Public issues, no source | Not a runtime component |

Private or unpublished components, including the canonical Zig server, existing
game clients, WebAdmin, and commercial services, are outside this public map.

## How the pieces assemble

```text
creators and players
        |
        v
public docs (this repository)
        |
        +--> JSON template registry -- versioned content contracts
        |
        +--> client starters -------- documentation-only until extraction
        |         Godot VR / Godot Classic 3D / Three.js / FoveaCore
        |
        +--> home-lab NPC path ----- local inference, ESP32 expression
        |
        v
authoritative game server (proprietary, unpublished)
        |
        +--> validates identity, movement, combat, inventory, economy
        +--> emits presentation and bounded NPC expression packets
        +--> persists world and character state
```

Templates never grant gold, items, damage, movement speed, or permissions.
Clients never become authoritative. A local LLM never becomes a rules engine.

## Where to start

| Goal | Start here |
|---|---|
| Understand the whole public map | this page |
| Understand authority, zones, and replication | [Architecture overview](architecture-overview.md) |
| Understand NPC / LLM behaviour | [NPC agent pipeline](npc-agent-pipeline.md) |
| Understand future clients | [Client architecture](client-architecture.md) |
| Understand the unpublished server boundary | [Server architecture](server-architecture.md) |
| Read the public network contract | [Network contract](../reference/network-contract.md) |
| Use or create JSON templates | [Use JSON templates](../how-to/use-json-templates.md) |
| Author a world, biome, NPC, or item | [Author world content](../how-to/author-world-content.md) |
| Size a home-lab NPC setup | [First NPC benchmark](../tutorials/first-npc-benchmark.md) |
| Report a public issue | [ultimate-odycer-feedback](https://github.com/zedarvates/ultimate-odycer-feedback) |

Continue with the [architecture overview](architecture-overview.md) for diagrams
and the [start a project tutorial](../tutorials/start-an-ultimate-odycer-project.md)
for a first working path that stays inside public material.
