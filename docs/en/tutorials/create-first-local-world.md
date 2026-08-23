# Create your first local world

This tutorial guides a technical beginner working with an LLM from an initial
idea to a verified local setup. It assumes neither a studio nor a cloud server
nor previous system-administration experience.

> **Current state — `unavailable`:** no public server release can be downloaded
> yet. You can complete the project preparation, but you must stop at step 6
> until the [official releases page](https://www.ultimateodycer.com/releases/)
> lists a real archive with its SHA-256 digest.

## What you will decide

1. the creative vision for your game;
2. the 3D engine;
3. the client template;
4. the world topology;
5. the local-machine profile;
6. the components that are actually available;
7. the next work that may be handed to an LLM.

## 1. Write a short project brief

Answer in simple sentences:

- What are the game's genre and time period?
- What do players do during an ordinary ten-minute session?
- Do they play alone, in small groups, or in a densely populated world?
- How do they travel?
- Does the world continue to evolve while they are offline?
- Which device must run the client?
- What scale do you want to test first?

Original example:

> A multiplayer urban RPG. Players accept jobs, drive, trade, and grow their
> activities in a persistent city. The first prototype uses one district and a
> few local players.

A reference such as “GTA-like” describes a family of functions. It does not
authorize copying characters, places, story, code, dialogue, assets, or visual
identity from an existing work.

## 2. Choose the engine

Choose **Godot** unless a strong constraint requires another engine. It is the
reference path documented by Ultimate Odycer.

- Godot: recommended and fully documented;
- Three.js: an alternative Web path;
- Unity or Unreal Engine: possible, with no currently validated template;
- FoveaCore: a specialized path still under construction.

Read the [engine, template, and world matrix](../reference/engine-template-world-matrix.md)
before continuing.

## 3. Choose the template

A template provides a client direction; it does not prove that the game,
networking, or assets are complete. Always check its status.

For the beginner path, select the Godot template closest to the intended
experience. If its status is `under_construction` or `planned`, record the
choice in the project brief and do not invent the missing files.

## 4. Choose the topology

- `flat_map`: city, dungeon, arena, region, or urban world;
- `planet`: one spherical world;
- `mega_planet`: an immense planet requiring streaming and partitioning;
- `solar_system`: multiple bodies and transition spaces.

Start with the smallest structure that can prove your gameplay loop. The urban
RPG example begins on a `flat_map`, not on an entire planet.

## 5. Choose the local profile

The following figures are `estimated` planning values, not release-certified
minimums.

| Profile | Processor | Memory | Free SSD | Use |
|---|---:|---:|---:|---|
| Dedicated server | 4 cores | 8 GiB | 20 GiB | Server and PostgreSQL only |
| Shared workstation | 6 cores | 16 GiB | 40 GiB | Work or play while the server runs |
| Creation workstation | 8 cores | 32 GiB | 100 GiB | Godot and optional creation tools |

The ComfyUI GPU requirement remains `unavailable` until a module, its model set,
and a reproducible measurement are published. See
[choose hardware](../how-to/choose-hardware.md) for more context.

## 6. Check the release

Open the [official page](https://www.ultimateodycer.com/releases/).

Continue only if it displays:

- a version;
- an archive for your platform;
- its size;
- a complete SHA-256 digest;
- compatibility documentation.

If the page says that no public release exists, the valid result is the saved
project brief with its engine, template, topology, and hardware profile. Return
later; do not use an archive received elsewhere.

## 7. Install the local foundation

When a release exists, follow this order:

1. [Windows installation](../how-to/install-local-server-windows.md);
2. [Linux variant](../how-to/install-local-server-linux.md), if needed;
3. [backup and restore check](../how-to/backup-and-test-restore-postgresql.md);
4. [Godot template connection](../how-to/connect-godot-template.md);
5. [final acceptance checklist](../reference/local-setup-acceptance-checklist.md).

## 8. Choose optional modules

The installation must offer two version-compatible paths:

- server only;
- server with selected Tools Suite modules.

The Tools Suite, dungeon, city, architecture, creature, and avatar editors,
Asset Factory with ComfyUI, and other modules are currently
`under_construction`. A module absent from the release cannot be installed.

## Tutorial outcome

Setup is complete only when every applicable acceptance check passes. A good
documentation page or documentation test never proves that the server,
PostgreSQL, Godot, or a tool works on your machine.
