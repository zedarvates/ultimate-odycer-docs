# Character, creature, and animation tools

## Ultimate Odycer character architecture

Creature Editor Lite validates XenoGenome Lite creature proposals. Avatar,
Creature, and complete generation pipelines remain local or proxy surfaces. The
server strictly maintains authoritative ownership of stats, attacks, spawns,
economy, and physics.

## Character creation tools

- MakeHuman: free and open source; bundled mesh assets and official exports have
  a documented CC0 public domain boundary, unlike third-party assets;
- VRoid Studio: free tool with VRM export; default presets and third-party
  content may add specific license terms;
- Epic MetaHuman: bound to Unreal Engine licensing and revenue/seat terms;
- Reallusion Character Creator: one-time purchase or subscription, with separate
  plug-ins and content store licenses.

## Animation tools

- Blender: local rigging, weight skinning, animation, and retargeting;
- Adobe Mixamo: free with Adobe ID, documented commercial use, bipedal auto-rigging;
- Cascadeur: free non-commercial tier, paid commercial tiers;
- Rokoko / Maya / motion capture solutions: dedicated accounts, subscriptions,
  or hardware required.

## Conversion and validation

VRM and FBX models must follow an audited conversion pipeline to GLB/Godot.
Verify skeleton hierarchy, bone orientation, scale, vertex skin weights, shape
keys/morph targets, materials, hair cards, animations, licenses, LODs, and
performance. A locally visible avatar does not prove multiplayer network
replication.

## Multiplayer and VR proof ladder

Validate each step independently: local avatar rendered, morph target applied,
correct `runtime_entity_id`, secondary avatar unmodified, two client
processes, authenticated TLS transport, appearance/cosmetic broadcast, remote
character rebuild, then head/hands/gestures tracking on physical VR headsets. A
synthetic loopback broker proves a targeted contract, not the live Zig server,
the public internet, hardware OpenXR, or production readiness.
