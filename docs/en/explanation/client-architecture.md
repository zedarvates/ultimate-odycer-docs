# Client architecture

Status: `decision` for intended public starters; no playable client is
published. The Godot VR, Godot Classic 3D, Three.js 2.5D, and FoveaCore
repositories currently contain scope, roadmap, and compatibility gates, not
game projects.

## Intended client shells

| Profile | Public repository | Current contents |
|---|---|---|
| Godot VR MMORPG | [ultod-client-godot-vr-mmorpg-template](https://github.com/zedarvates/ultod-client-godot-vr-mmorpg-template) | documentation only |
| Godot Classic 3D | [ultod-client-godot-classic-3d-mmorpg-template](https://github.com/zedarvates/ultod-client-godot-classic-3d-mmorpg-template) | documentation only |
| Three.js 2.5D | [ultod-client-threejs-2-5d-mmorpg-template](https://github.com/zedarvates/ultod-client-threejs-2-5d-mmorpg-template) | documentation only |
| FoveaCore FPS-RPG | [ultod-client-foveacore-fps-rpg-template](https://github.com/zedarvates/ultod-client-foveacore-fps-rpg-template) | documentation only |

Existing Ultimate Odycer client code must not be imported without a
file-level public extraction audit.

## Target project structure

A future original starter SHOULD look like this, without copying proprietary
scenes or assets:

```text
client-starter/
  project files for the chosen engine
  scenes/
    bootstrap           engine, platform, and quality checks
    login               credentials never stored in the scene
    realm-handoff       joins a server-assigned space
    player              local presentation of an authoritative entity
    npc                 presentation and interaction prompts only
    zone                streamed geometry and interest objects
    ui                  HUD, menus, VR panels
  input/
    desktop or OpenXR abstractions
  net/
    protocol client, once a public contract exists
  content/
    pinned JSON registry snapshots
```

Missing folders in the public repositories mean the starter is not published,
not that a hidden project is implied.

## Presentation versus authority

```text
OpenXR / desktop input
        |
        v
local pose, comfort locomotion, prediction
        |  discarded if the server rejects it
        v
intent: move, interact, talk, use, craft
        v
authoritative server
        v
state diff, animation hints, NPC expression
        v
scene streaming, LOD, audio, haptics
```

Local physics and collisions may keep a headset comfortable. They must not
award loot, apply damage, change inventory, or accept a speed hack. VR
comfort settings are client-side; world rules are not.

## Connection path

Until a public protocol version is approved, a client can only:

1. document the intended login and realm-handoff sequence;
2. consume pinned JSON templates for labels and synthetic fixtures;
3. run local, non-networked presentation experiments;
4. refuse production endpoints, credentials, and protocol dumps.

A synthetic loopback fixture is the first allowed network proof. Isolated
desktop execution does not prove VR interoperability.

## Related pages

- [Ecosystem overview](ecosystem-overview.md)
- [Network contract](../reference/network-contract.md)
- [Use JSON templates](../how-to/use-json-templates.md)
- [Start a project](../tutorials/start-an-ultimate-odycer-project.md)
