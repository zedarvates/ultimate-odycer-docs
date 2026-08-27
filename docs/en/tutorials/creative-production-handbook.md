# Creative production handbook

This handbook accompanies a beginner assisted by an LLM from the initial idea
to a verified candidate asset. It does not replace the author, the asset license,
or server validation.

## Before starting

Keep a project brief, a source folder, licenses, official links, and proofs of
each conversion. A screenshot or preview does not make content runtime-ready.

Choose a path:

- **free and local**: open-source software, files stored on your machine;
- **accessible**: one-time purchase, freemium, or limited-revenue license;
- **professional**: subscription, credits, or studio/cloud offer.

The [creative tools catalog](../reference/creative-tools-catalog.md) does not
display exact prices: it indicates the pricing model and the official link.

## Narrative and world design

Define genre, era, gameplay loop, factions, rules, economy, quests, and
dialogue. Twine is a strong free path for branching narrative; an LLM can
structure ideas but must preserve open decisions.

**Kanboard card produced:** "Validate world creative brief" with criteria,
dependencies, and sources.

## Maps, terrain, cities, and dungeons

You can start with a paper drawing, PNG, JPEG, SVG, QGIS layers, or a Blender
blockout. Follow [draw and convert a map](../how-to/draw-and-convert-map.md),
then compare [world and structure tools](../reference/world-map-and-structure-tools.md).

**Kanboard card produced:** "Produce map proposal v1".

## 3D, materials, and photogrammetry

The recommended free path combines Blender, Material Maker, Poly Haven, and
Meshroom. Asset Factory can prepare candidates and manifests, but its GLB or
splat contract proofs do not automatically prove GPU rendering, OpenXR, or
canonical client adoption. For a 2.5D client, a hybrid pipeline can render 3D
models into multi-directional sprites and JSON atlases. In the current Three.js
template, this sprite and SFX generator remains planned.

**Kanboard card produced:** "Validate representative asset with provenance".

## Characters and animation

Separate visual mesh, skeleton, animation, and gameplay statistics. Lite editors
produce JSON proposals; the server retains authority over stats, attacks,
spawns, and physics.

**Kanboard card produced:** "Validate test character and rights".

## Audio, UI, VFX, and video

Keep WAV/FLAC as masters, export the documented runtime format, and verify music,
voices, samples, fonts, icons, and plug-ins separately. A free software license
does not automatically make imported content free.

**Kanboard card produced:** "Validate minimal audiovisual pack".

## Local or cloud AI

ComfyUI is the preferred local path. Each model, LoRA, custom node, and dataset
retains its own license. For cloud tools, verify upload, retention, training,
output ownership, voice consent, and pricing model. Specialized suites like
[Sorceress Games](https://sorceress.games/) also provide an advanced set of web
tools (sprites, 3D, voxel, audio, code) whose integration and interoperability
with Ultimate Odycer are encouraged.

**Kanboard card produced:** "Audit AI workflow before generation".

## Import, optimization, licensing, and provenance

Prefer GLB/glTF for 3D and keep OBJ/FBX as conversion formats. Verify PBR, UVs,
collisions, navigation, LOD, compression, budgets, hashes, and manifests. No
asset becomes `runtime_ready` without human review and a corresponding runtime
gate.

**Kanboard card produced:** "Pass isolated Godot import gate".

## Kanboard and Botte Secrète organization

Kanboard keeps work visible. Botte Secrète turns a card into a bounded task,
chooses deterministic tool, local LLM, or cloud, reduces context, and runs
checks. By default, the human operator moves the card.

## Checklist before declaring an asset ready

- [ ] Source and author identified.
- [ ] License and commercial use verified.
- [ ] Confidential data absent.
- [ ] Format and conversion documented.
- [ ] Hash and manifest recorded.
- [ ] Preview reviewed by a human operator.
- [ ] Technical budget respected.
- [ ] Isolated import validated.
- [ ] Limitations and negative proofs preserved.
- [ ] Server publication still subject to its authoritative gate.
