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

For walls and ground, consult the [surface relief reference](../reference/surface-relief-rendering.md):
geometry versus POM choices, the Crimson Desert video correction, and evidence
required before desktop, Web, or VR adoption.

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

## Worked exercise: the Three Passages neighborhood

**Status: proposed exercise, not a shipped or tested demonstration.** This
name identifies an original example, not a new official template. The journey
uses a flat map and targets a local Godot trial. Prepare files without waiting
for the Tools Suite; do not invent a connector when a module is missing.

Player goal: leave a square, reach a workshop, collect a fictional parcel and
deliver it to a courtyard. First version: walking only, one neighborhood, one
simple building and one temporary character. Vehicles, combat, persistent
economy and planetary worlds are out of scope.

Allow at most 30 minutes for each LLM proposal and two revisions before asking
for a human decision. This is an exercise budget, not an estimate of total
completion time or runtime performance.

### 1. Record decisions and organize files

Write a brief: goal, chosen engine and version, template and status, `flat_map`
topology, target machine and limits. Prepare separate folders for the brief,
source drawings, editable assets, exports, licenses and evidence. Keep secrets
and PostgreSQL dumps elsewhere.

**Expected result:** an approved brief and one Kanboard card per step with an
acceptance criterion. Botte Secrète may propose the breakdown; the LLM does not
automatically change the board.

> Prompt: "Rephrase my project as a short brief and eight ordered tasks. Separate
> confirmed decisions from open questions. Install nothing and create no tasks
> in an external service."

### 2. Draw the neighborhood

Draw a square, three passages, the workshop and the courtyard. Add a legend,
starting point, destination and explicitly chosen scale. A square measuring
100 meters per side can serve as a starting convention; it is not a dimension
measured from the image. Separate terrain, walkable areas, building footprints
and annotations.

**Expected result:** preserved source drawing and a list of ambiguities, using
the [map conversion guide](../how-to/draw-and-convert-map.md).

> Prompt: "Describe only what is visible in my drawing. Propose a legend and
> coordinates with their origin and units. Flag every inferred dimension. Wait
> for my approval before proposing conversion."

### 3. Prepare the map proposal

Translate the approved drawing into a structured proposal following the map
conversion guide's contract. Keep elevation, circulation, buildings and play
areas separate. If a compatible tool is available, check its import in a project
copy. Otherwise retain the plan and build simple placeholder volumes in the
chosen editor: this fallback is not a Tools Suite import.

**Expected result:** reviewed proposal, explicit origin and units, documented
transformations. Status remains `planned` until an actual trial.

> Prompt: "Prepare a reversible conversion proposal. List the files to produce
> and capabilities actually available. No server calls, source changes or
> invented APIs."

### 4. Create only essential elements

Prepare a simple workshop, a parcel and a temporary character. A capsule can
stand in for the character while appearance is not the test's subject. Keep
editable files separate from exports; record each element's author, origin and
rights. An editor preview does not automatically provide an exportable 3D model.

**Expected result:** three identifiable elements with provenance records.
A character mesh does not authorize its gameplay statistics.

> Prompt: "Propose the three minimum elements for this delivery. Reuse my
> authorized sources and list missing rights and expected formats. No purchases,
> uploads or paid generation without my approval."

### 5. Verify isolated visual import

In a dedicated engine project copy, check scale, orientation, materials and
missing assets. Then test collisions and traversal through the three streets
if the chosen client provides these capabilities. Record 'visible', 'collision
verified' and 'navigation verified' separately.

**Expected result:** actual capture, versions and import log. Without execution,
retain `[Scaffolding / Proxy]`; a successful import remains isolated evidence,
not multiplayer or VR validation.

> Prompt: "Check one element at a time in this authorized copy. Describe expected
> and observed results. Do not mark collision or navigation verified from a
> screenshot alone. Stop if a required file or tool is missing."

### 6. Prepare and then test delivery

Write three states: parcel available, carried and delivered. Define transition
conditions, rejection of a second pickup and rejection of delivery outside the
courtyard. A client-only interaction can serve as a mockup; it does not validate
inventory, rewards or server persistence.

**Expected result:** test scenario with permitted and rejected actions. Each
server transition requires a verified contract and implementation.

> Prompt: "Describe the delivery states and tests without inventing network
> messages. Separate local mockup from server decisions. Do not create money
> or persistent items to simulate success."

### 7. Cross the server gate only when available

Follow the [first local world journey](create-first-local-world.md) and its
checklist: official archive, compatible versions, PostgreSQL, login and world
entry. If the release or template is missing, mark this step `blocked` and
retain the creative work; do not substitute a fake service and declare success.

**Expected result:** separate evidence of connection, accepted or rejected
action, then persistence only if it was actually tested.

> Prompt: "Check public prerequisites and available evidence. If a condition is
> missing, explain the blocker. Otherwise propose one authorized local test
> without opening Internet ports."

### 8. Back up and prepare a handoff

Archive creative sources and their licenses. For server data, follow the
[PostgreSQL guide](../how-to/backup-and-test-restore-postgresql.md): an asset ZIP
does not back up characters. Keep restoration evidence separate from the
confidential dump.

**Expected result:** a report listing versions, files, successful and failed
tests, blockers and the next action. 'Creative preparation complete' and
'first local loop verified' are different outcomes.

> Prompt: "Write a handoff using only the supplied evidence. Distinguish observed,
> planned and blocked. Include no secrets, dump contents or personal paths.
> Propose just one next step for approval."

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
