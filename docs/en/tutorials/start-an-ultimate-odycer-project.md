# Start an Ultimate Odycer project from public material

This tutorial stays inside published repositories. You will leave with a
map of the ecosystem, a validated docs checkout, and a pinned JSON template
workflow. You will not connect to a production server or obtain a playable
MMO client.

## Expected outcome

- you can explain what is public and what is unpublished;
- the documentation validator returns `validation: ok`;
- you know how to pin a registry template without inventing compatibility.

## Prerequisites

- Python 3.11 or newer;
- a terminal opened at a local copy of this repository;
- no production credentials.

## 1. Read the public map

Open [ecosystem overview](../explanation/ecosystem-overview.md) and note:

- this docs hub;
- the JSON template registry;
- the four documentation-only client starters;
- the public feedback tracker;
- the unpublished Zig server.

## 2. Validate this repository

In PowerShell:

```powershell
rtk python scripts/validate_docs.py
rtk python -m unittest discover -s tests -v
```

The first command must finish with `validation: ok`.

## 3. Pin a content contract, not a live world

Clone or browse [ultod-json-template-registry](https://github.com/zedarvates/ultod-json-template-registry).
Resolve one catalogue entry, record its version and SHA-256, and treat an
empty compatibility list as unsupported.

Do not download templates automatically into a running game.

## 4. Choose a future client profile

Pick one documentation-only starter: Godot VR, Godot Classic 3D, Three.js
2.5D, or FoveaCore. Read its `SCOPE.md` and server-compatibility page.
If alignment is blocked, do not invent a network client.

## 5. Optional home-lab NPC path

If you are sizing local dialogue hardware, continue with
[your first NPC benchmark](first-npc-benchmark.md). Keep inference on
loopback and label results `scenario` or `estimated` until you measure.

## 6. Check success

The tutorial is complete when you can point to the public repositories, name
the unpublished server boundary, and refuse a compatibility claim that has
no evidence.

Next: [architecture overview](../explanation/architecture-overview.md),
[author world content](../how-to/author-world-content.md), or
[contribute and test](../how-to/contribute-and-test.md).
