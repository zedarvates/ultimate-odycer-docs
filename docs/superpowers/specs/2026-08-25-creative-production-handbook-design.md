# Creative Production Handbook — Design

Date: 2026-08-25  
Status: approved direction, implementation pending user review

## 1. Goal

Extend the bilingual Ultimate Odycer local-setup documentation into a practical
creative-production handbook. A technical beginner assisted by an LLM must be
able to understand what can be created, select a suitable tool path, preserve
commercial rights and provenance, convert the result into supported formats,
and organize the work with Kanboard and Botte Secrète.

The handbook must cover both:

1. Ultimate Odycer Tools Suite capabilities and their real maturity; and
2. external free, open-source, accessible paid, professional, and cloud tools.

The default recommendation remains local-first and free/open-source. Cloud and
paid alternatives are included when they materially improve a workflow.

## 2. Non-goals

- No exact product prices. Pricing changes too frequently.
- No purchase, subscription, account creation, deployment, or cloud upload.
- No installation of Kanboard, Botte Secrète, creative software, models, or
  plug-ins.
- No automatic mutation of Kanboard through its API.
- No automatic publication of generated assets to the Zig server.
- No claim that a Tools Suite screenshot, schema, preview, dry run, or contract
  is an end-to-end runtime feature.
- No legal advice or guarantee that a third-party licence will remain
  unchanged.
- No copied characters, places, dialogue, maps, visual identity, code, or
  assets from existing games or media.
- No confidential prompts, internal services, production data, credentials, or
  unaudited proprietary assets in the public documentation.

## 3. Audience and reading modes

### Beginner path

The beginner follows one recommended tool path per production stage. Each page
explains the goal, safe inputs, expected outputs, conversion step, validation,
and next Kanboard task.

### Advanced path

An indexed reference gives direct access to formats, conversion routes,
licensing checks, optimization gates, and alternative tools.

### LLM path

Machine-readable sources and reusable prompts let an LLM ask one question at a
time, recommend tools without inventing capabilities, and generate proposals
that require human and server validation.

## 4. Chosen documentation architecture

Three approaches were considered:

1. One very large tutorial. It is simple to publish but becomes unreadable and
   difficult to maintain.
2. A modular production handbook backed by one machine-readable catalog. This
   is the selected approach.
3. An interactive Tools Suite recommender. This remains a later product step
   because several tool surfaces are still scaffolding or local prototypes.

The existing `create-first-local-world` tutorial remains the short entry point.
It links into a modular handbook instead of duplicating every creative tool.

## 5. Document structure

The following bilingual pairs are added:

```text
docs/{fr,en}/tutorials/creative-production-handbook.md
docs/{fr,en}/how-to/draw-and-convert-map.md
docs/{fr,en}/how-to/organize-project-kanboard-botte-secrete.md
docs/{fr,en}/reference/creative-tools-catalog.md
docs/{fr,en}/reference/world-map-and-structure-tools.md
docs/{fr,en}/reference/3d-assets-materials-and-photogrammetry-tools.md
docs/{fr,en}/reference/character-creature-and-animation-tools.md
docs/{fr,en}/reference/audio-2d-ui-vfx-and-video-tools.md
docs/{fr,en}/reference/local-and-cloud-ai-tools.md
docs/{fr,en}/reference/import-optimization-licensing-and-provenance.md
```

Existing pages updated:

```text
docs/{fr,en}/tutorials/create-first-local-world.md
docs/{fr,en}/reference/engine-template-world-matrix.md
docs/{fr,en}/reference/llm-local-setup-prompts.md
docs/llm/context-index.json
docs/llm/README.md
llms.txt
README.md
PUBLICATION_STATUS.md
mkdocs.yml
```

Machine-readable sources:

```text
schemas/creative-tools-catalog-v1.schema.json
examples/creative-tools-catalog.json
```

## 6. Production stages

The handbook covers these stages in order:

1. concept, narrative, quests, dialogue, and world rules;
2. hand-drawn maps and LLM-assisted interpretation;
3. terrain, biomes, roads, rivers, regions, and world topology;
4. cities, buildings, architecture, interiors, caves, and dungeons;
5. props, 3D models, scans, and photogrammetry;
6. textures, materials, decals, PBR channels, and asset libraries;
7. avatars, clothing, hair, creatures, and modular parts;
8. rigging, animation, retargeting, and motion capture;
9. sound effects, voice, music, and interactive audio;
10. illustration, UI, icons, typography, and localization;
11. VFX, shaders, lighting, video, and cinematics;
12. local and cloud generative AI;
13. Godot import, collision, navigation, LOD, streaming, compression, and
    performance budgets;
14. licensing, provenance, hashes, human review, server validation, and
    publication boundaries;
15. project organization with Kanboard and Botte Secrète.

## 7. Tool selection rule

Each production need lists at most five choices:

1. Ultimate Odycer Tools Suite path;
2. best free and local recommendation;
3. another open-source or zero-cost option;
4. accessible paid option;
5. professional or cloud option.

This is a curated decision aid, not an encyclopedia. A tool is included only if
it has a clear purpose, an official source, a documented pricing model, and a
plausible path into the production pipeline.

## 8. Machine-readable catalog contract

The catalog schema is `ultimate-odycer.creative-tools-catalog.v1`.

Top-level fields:

```json
{
  "schema_version": "ultimate-odycer.creative-tools-catalog.v1",
  "verified_on": "2026-08-25",
  "pricing_policy": "model_only_no_exact_prices",
  "default_strategy": "local_first_free_open_source",
  "tools": []
}
```

Each tool record contains:

```json
{
  "id": "blender",
  "name": "Blender",
  "provider": "Blender Foundation",
  "ownership": "ultimate_odycer_or_external",
  "domains": ["maps"],
  "maturity": "available",
  "execution": "local",
  "pricing_model": ["free_open_source"],
  "commercial_use": "allowed",
  "commercial_use_note": "Short limitation summary",
  "privacy": "local_no_upload",
  "ai_training_terms": "not_applicable",
  "integration": "direct_or_conversion_required",
  "inputs": ["png"],
  "outputs": ["glb"],
  "platforms": ["windows", "linux"],
  "official_url": "https://www.blender.org/",
  "pricing_or_license_url": "https://www.blender.org/about/license/",
  "verified_on": "2026-08-25",
  "notes": "Bounded factual note"
}
```

Allowed maturity values:

- `executable_public`;
- `prototype_local`;
- `scaffolding_proxy`;
- `planned`;
- `available_external`;
- `verification_required`;
- `unavailable`.

Allowed pricing models:

- `free_open_source`;
- `free`;
- `free_noncommercial`;
- `freemium`;
- `one_time_purchase`;
- `subscription`;
- `credits`;
- `revenue_limited`;
- `project_budget_limited`;
- `contact_sales`;
- `mixed`.

Allowed commercial-use values:

- `allowed`;
- `conditional`;
- `noncommercial_only`;
- `plan_dependent`;
- `asset_dependent`;
- `model_dependent`;
- `verification_required`.

No exact prices appear in the catalog. The official pricing or licence link is
the source of current truth.

## 9. Tools Suite capability and proof states

The public handbook reflects the current evidence rather than the ambitions of
the private monorepo.

| Tool family | Candidate output | Public description |
|---|---|---|
| Creature Editor Lite | XenoGenome Lite JSON | Executable public slice; preview remains proxy |
| City Editor Lite | CityConfig Lite proposals | Executable public survey slice; no Zig/Godot runtime proof |
| Architecture Editor Lite | HouseBlueprint Lite proposals | Executable public drafting slice; no costs, HP, assets, collision, HLOD, Godot, VR, or publication proof |
| Architecture Editor | House and procedural blueprints | Local authoring/prototype; individual proofs remain bounded |
| Dungeon Editor | Dungeon blueprints | Presentation or local prototype unless a release says otherwise |
| Creature Editor | XenoGenome-compatible JSON | Full internal editor remains extraction-gated |
| Avatar Editor | Avatar and morph templates | Local/proxy until clean public runtime gates pass |
| City Editor | CityConfig and authored layouts | Local planning and preview; server remains authoritative |
| Asset Factory | Reviewed GLB candidates, manifests, optional splat contracts | Contract and review gates exist; producer/runtime proofs remain separate |
| Audio Factory | Verified catalog, format and budget evidence | Candidate audio pack validation, not gameplay publication |
| Vault WebAdmin | Authenticated administration actions | Operational surface, not a content-generation authority |
| Godot CLI | Debug inspection and bounded validation | Separate development-only product boundary |

All Tools Suite pages use the exact current label. A screenshot never upgrades
`scaffolding_proxy` to `executable_public`.

## 10. External tool shortlist

### Narrative and world design

- Twine: free/open-source nonlinear narrative, local app or browser, commercial
  output allowed by its official documentation.
- LibreOffice: free/open-source writing and tabular planning.
- Worldbuilding or collaborative cloud tools: freemium/subscription alternatives
  with data-hosting warnings.

### Maps, terrain, cities, and dungeons

- QGIS: free/open-source digitizing, layers, cartography, analysis, GeoJSON and
  GIS conversion.
- Blender: free/open-source 3D terrain, blockout, modeling, sculpting, geometry
  nodes, UVs, animation, and export.
- Inkarnate: cloud freemium/subscription map creation; commercial rights depend
  on the selected plan.
- World Machine: free noncommercial tier, paid commercial perpetual tiers.
- Gaea, World Creator, or Houdini: professional procedural terrain alternatives
  with plan or revenue restrictions.

### 3D assets, materials, and photogrammetry

- Blender: default local modeling and conversion hub.
- Material Maker: free/open-source node-based PBR authoring with Godot export.
- Poly Haven: CC0 HDRIs, textures, and 3D models; provenance still recorded.
- Meshroom/AliceVision: free/open-source local photogrammetry with GPU
  considerations.
- Substance 3D, Maya, ZBrush, Houdini, or RealityCapture: professional paths
  with subscription, perpetual, revenue-limited, or engine licence terms.

### Characters, creatures, and animation

- MakeHuman: free/open-source application; bundled assets and exports have a
  separate documented licence boundary.
- VRoid Studio: free character creation; preset and third-party asset terms
  remain asset-dependent.
- Mixamo: free with Adobe ID; royalty-free commercial use documented for
  characters and animations, currently limited to biped humanoid auto-rigging.
- Cascadeur: free noncommercial tier and commercial subscriptions/perpetual
  entitlement conditions.
- MetaHuman or Reallusion Character Creator: professional alternatives with
  engine, revenue, perpetual, subscription, plug-in, or asset-store terms.

### Audio, 2D, UI, VFX, and video

- Audacity, LMMS, Krita, GIMP, Inkscape, Penpot, Blender, Kdenlive, and Godot:
  free/open-source defaults for their respective roles.
- REAPER: evaluation plus discounted/commercial one-time licence model.
- FMOD and Wwise: middleware with revenue/project-budget licensing gates.
- Figma, Affinity, Adobe, ElevenLabs, and other cloud/professional tools:
  freemium, purchase, subscription, or credits, with explicit data and
  commercial-use checks.

### Generative AI

- ComfyUI: preferred local orchestration surface, but the licence of every
  model, LoRA, custom node, dataset, and generated source remains independent.
- Adobe Firefly: cloud freemium/subscription/credits; commercial claims depend
  on feature state and applicable terms.
- Meshy and similar 3D services: cloud freemium/credits; output ownership and
  commercial rights depend on plan.
- ElevenLabs and similar voice services: cloud subscription/credits; voice
  consent, cloning rights, commercial licence, and biometric/privacy concerns
  require explicit review.

## 11. Supported exchange formats

| Domain | Preferred source or interchange | Runtime or validated target |
|---|---|---|
| Drawn maps | PNG, JPEG, SVG | Versioned map intent JSON, then editor-specific proposal |
| GIS | GeoJSON, raster layers | Converted map/world recipes |
| Terrain | PNG, EXR, RAW heightmaps | Godot-compatible terrain representation after validation |
| 3D | GLB/glTF preferred; OBJ/FBX as interchange | Reviewed GLB or an explicitly supported runtime format |
| Avatars | GLB, VRM, FBX | Reviewed GLB and versioned avatar template |
| Gaussian splats | PLY, SPLAT, FOVEA | Hashed artifact matching the declared format |
| PBR materials | Albedo, normal, roughness, metallic, AO, height | Engine material plus provenance |
| Audio masters | WAV or FLAC | OGG/WAV according to runtime contract |
| Narrative/localization | JSON, CSV, Twine/Twee or documented intermediate | Versioned game content JSON |
| UI/vector | SVG, PNG, source design file | Godot UI assets and theme definitions |

Every format row says `direct`, `conversion_required`, or `reference_only`.

## 12. Hand-drawn map workflow

The user may draw a map on paper, tablet, image editor, vector editor, QGIS, or
another mapping tool.

Minimum drawing annotations:

- north or orientation;
- scale or explicit absence of scale;
- world boundary;
- terrain and elevation intent;
- water, roads, districts, regions, and landmarks;
- building footprints;
- entrances, exits, portals, and transition points;
- intended spawn, quest, danger, and safe zones;
- legend and uncertain areas.

Flow:

```text
PNG/JPEG/SVG + legend + project brief
→ LLM analysis with explicit uncertainties
→ uo.map-intent/v1 proposal
→ Map/City/Dungeon/Architecture editor when available
→ preview_only transaction
→ human corrections and approval
→ versioned editor JSON
→ schema/hash/provenance checks
→ authoritative server validation
→ Godot consumption
```

The LLM never writes an authoritative map directly. If visual import or the Map
Editor is unavailable, the valid result is the preserved drawing, map-intent
proposal, uncertainties, and next Kanboard task.

## 13. Kanboard project organization

Kanboard is the visible planning source of truth.

Recommended columns:

```text
Ideas
→ Design
→ Ready
→ In progress
→ Review
→ Validation
→ Blocked
→ Done
```

Recommended swimlanes:

- world and maps;
- Godot client;
- server;
- Tools Suite;
- 3D assets and materials;
- characters and animation;
- audio;
- UI, VFX, and video;
- documentation and releases.

Each card contains:

- observable objective;
- chosen tool and alternatives;
- inputs and expected outputs;
- formats and conversion route;
- dependencies;
- licence, provenance, and privacy notes;
- acceptance criteria;
- evidence links or hashes;
- bounded secret-free LLM prompt;
- blocked reason when applicable.

Kanboard backup and attachment retention are documented. Plug-ins are optional
and must be reviewed because the official plug-in directory has no centralized
approval or code-review guarantee.

## 14. Botte Secrète workflow

Botte Secrète assists execution but does not replace Kanboard.

It may:

- classify a card into deterministic, local-model, or cloud reasoning work;
- improve and bound a prompt;
- reduce context and tool output;
- discover relevant capabilities and skills;
- enforce cost and token budgets;
- run project checkups and drift checks;
- retain proof summaries and safe local dashboards.

Default flow:

```text
Kanboard card
→ Botte Secrète policy/capability check
→ bounded prompt and route
→ deterministic tool, local LM, or cloud LM
→ validation and evidence
→ human updates Kanboard
```

Botte Secrète does not mutate Kanboard by default. A future connector is a
separate feature and requires:

- user API or personal token with project permissions;
- HTTPS outside a strictly local deployment;
- token storage outside prompts and public files;
- read-only discovery before mutation;
- explicit operator approval for task creation or movement;
- idempotency and audit evidence.

Kanboard's application API is not the default because it exposes all procedures
without project permission checks.

## 15. Reusable LLM prompts

The prompt catalog gains prompts for:

- selecting a creative tool path;
- checking commercial rights and model/asset licences;
- converting a hand-drawn map into a map-intent proposal;
- preparing 3D import and optimization work;
- reviewing PBR channels and asset provenance;
- preparing avatar, creature, animation, audio, UI, VFX, or localization tasks;
- converting a production need into a Kanboard card;
- asking Botte Secrète to route a card safely;
- reviewing evidence before moving a card to Done.

Every prompt requires one step at a time, no secrets, official-source checks,
explicit uncertainty, preservation of existing files, and confirmation before
upload, purchase, deletion, network exposure, deployment, or publication.

## 16. Staleness, licensing, and privacy handling

- `verified_on` records the last official-source review date.
- A stale or unreachable official link changes the tool to
  `verification_required`; it is not silently removed or declared safe.
- Pricing pages supply only the pricing model, never copied exact prices.
- Commercial use is a separate field from software price.
- Third-party presets, models, plug-ins, voices, fonts, textures, and marketplace
  assets retain their own licences.
- Local software is not automatically trusted; models and extensions are still
  scanned and provenance-checked.
- Cloud tools disclose upload, retention, training, biometric, and ownership
  considerations when the official terms provide them.
- The handbook states that licence summaries are operational guidance, not
  legal advice.

## 17. Error handling and fail-closed behavior

- Unknown Tools Suite maturity: `verification_required`.
- No public executable slice: preserve proposal and stop before runtime claims.
- Missing converter: label `conversion_required` and block the next gate.
- Unsupported input format: preserve the source and recommend a reviewed
  conversion path.
- Missing licence or provenance: block publication and runtime-ready status.
- Cloud-only tool with confidential input: recommend a local path first.
- Failed schema/hash/budget check: retain negative evidence and keep the
  Kanboard card in Validation or Blocked.
- Kanboard unavailable: preserve a local card template; do not invent task IDs.
- Botte Secrète unavailable: preserve the bounded prompt and manual route.

## 18. Validation strategy

The implementation must add automated checks for:

- creative catalog schema and vocabulary;
- unique tool IDs and official HTTPS links;
- permitted maturity, execution, pricing, commercial-use, and integration
  values;
- no exact copied price fields;
- every catalog domain represented in both language indexes;
- bilingual file pairs and internal Markdown links;
- LLM index paths and non-mutating authority;
- status consistency between prose and machine catalog;
- public-boundary scans for secrets, private paths, internal addresses, and
  confidential names;
- source SHA-256 manifest regeneration;
- offline HTML build with local runtime assets and valid internal links;
- fresh-copy validation;
- Gitleaks scan of the exact repository tree.

External URLs are checked for structure automatically and reviewed manually for
meaning. A successful link request does not prove current licence terms.

## 19. Publication and integration boundaries

This documentation change may update the public docs source and its generated
local HTML artifact. It does not by itself:

- deploy the Web portal;
- rebuild or publish a server ZIP;
- release the Tools Suite;
- install Kanboard or Botte Secrète;
- create a Kanboard API connector;
- validate a real Godot import;
- certify commercial rights for a user's selected asset.

Any later Web or ZIP integration consumes the already validated docs-build
manifest through the existing fail-closed contracts.

## 20. Acceptance criteria

The design is satisfied when:

1. a beginner can identify every major creative-production stage;
2. every stage offers a Tools Suite path plus curated free and paid
   alternatives;
3. local/open-source choices appear first;
4. pricing is expressed only as a model with official links;
5. commercial use, asset/model dependencies, cloud privacy, and conversion
   requirements are explicit;
6. a drawn map can become a versioned proposal without bypassing human or
   server validation;
7. Tools Suite maturity labels match current evidence;
8. Kanboard provides a reusable project board and card contract;
9. Botte Secrète has a bounded, non-authoritative orchestration role;
10. humans and LLMs can navigate the same canonical sources;
11. source validation, tests, offline build, fresh copy, and secret scan pass;
12. no deployment, purchase, publication, or external mutation occurs.
