# Creative Production Handbook Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish a bilingual, machine-indexed creative-production handbook that explains Ultimate Odycer Tools Suite capabilities, curated free and paid alternatives, map drawing and conversion, asset validation, and project organization with Kanboard and Botte Secrète.

**Architecture:** The public Markdown remains canonical. A strict JSON catalog stores current tool maturity, pricing model, commercial-use conditions, privacy, formats, and official links; modular French and English pages consume the same vocabulary, while the existing static builder produces the offline Web/ZIP artifact.

**Tech Stack:** Python 3.11+, `unittest`, JSON, JSON Schema 2020-12, Markdown, MkDocs 1.6.1, SHA-256

**Spec:** `docs/superpowers/specs/2026-08-25-creative-production-handbook-design.md`

## Global Constraints

- Local-first and free/open-source recommendations appear before cloud or paid alternatives.
- Do not include exact prices; store only pricing models and official pricing/licence URLs.
- Use current Tools Suite proof states: Creature, City, Architecture, Dungeon, and Avatar Editor Lite are executable public slices whose previews remain `[Scaffolding / Proxy]`.
- Tools create proposals; the Zig server remains authoritative for publication and gameplay state.
- Cloud tools require explicit privacy, retention, training, ownership, and commercial-use warnings.
- A software price never implies commercial rights; plug-ins, presets, models, voices, fonts, and marketplace assets retain separate licences.
- The LLM produces proposals and uncertainty; it never writes an authoritative map or publishes an asset.
- Kanboard is the visible planning source of truth; Botte Secrète routes and validates work but does not mutate Kanboard by default.
- No Kanboard deployment, API token, Botte connector, purchase, upload, Web deployment, server ZIP release, or publication occurs in this plan.
- Preserve concurrent work and the existing public/private repository boundaries.
- All shell commands run with the `rtk` prefix.

---

## File Structure

- `schemas/creative-tools-catalog-v1.schema.json`: vocabulary and structural contract.
- `examples/creative-tools-catalog.json`: reviewed tool records and per-domain recommendations.
- `scripts/validate_docs.py`: fail-closed catalog and cross-document validation.
- `tests/test_public_docs.py`: catalog, bilingual-pair, navigation, and status tests.
- `docs/{fr,en}/tutorials/creative-production-handbook.md`: production journey entry point.
- `docs/{fr,en}/how-to/draw-and-convert-map.md`: drawing-to-map-intent workflow.
- `docs/{fr,en}/how-to/organize-project-kanboard-botte-secrete.md`: board and orchestration workflow.
- `docs/{fr,en}/reference/creative-tools-catalog.md`: catalog semantics and quick selection.
- `docs/{fr,en}/reference/world-map-and-structure-tools.md`: maps, terrain, city, architecture, dungeon.
- `docs/{fr,en}/reference/3d-assets-materials-and-photogrammetry-tools.md`: modeling, materials, scans, splats.
- `docs/{fr,en}/reference/character-creature-and-animation-tools.md`: avatars, creatures, rigging, mocap.
- `docs/{fr,en}/reference/audio-2d-ui-vfx-and-video-tools.md`: audio, music, illustration, UI, shaders, video.
- `docs/{fr,en}/reference/local-and-cloud-ai-tools.md`: ComfyUI, model licences, cloud services.
- `docs/{fr,en}/reference/import-optimization-licensing-and-provenance.md`: formats, Godot import, budgets, rights.
- Existing tutorial, matrix, prompt catalog, human/LLM indexes, README, status, MkDocs, and manifests: discoverability and build integration.

### Task 1: Current evidence snapshot and creative catalog contract

**Files:**
- Create: `schemas/creative-tools-catalog-v1.schema.json`
- Create: `examples/creative-tools-catalog.json`
- Modify: `scripts/validate_docs.py`
- Modify: `tests/test_public_docs.py`

**Interfaces:**
- Consumes: Tools Suite public README/release gates, official external tool pages, and the design vocabulary.
- Produces: `creative_tools_catalog_errors() -> list[str]` and schema `ultimate-odycer.creative-tools-catalog.v1`.

- [ ] **Step 1: Write failing catalog tests**

Add this path constant and test shape:

```python
CREATIVE_CATALOG = ROOT / "examples" / "creative-tools-catalog.json"

def test_creative_tools_catalog_contract(self) -> None:
    catalog = json.loads(CREATIVE_CATALOG.read_text(encoding="utf-8"))
    self.assertEqual(
        catalog["schema_version"],
        "ultimate-odycer.creative-tools-catalog.v1",
    )
    self.assertEqual(catalog["pricing_policy"], "model_only_no_exact_prices")
    tools = {item["id"]: item for item in catalog["tools"]}
    self.assertEqual(tools["creature-editor-lite"]["maturity"], "executable_public")
    self.assertEqual(tools["city-editor-lite"]["maturity"], "executable_public")
    self.assertEqual(tools["architecture-editor-lite"]["maturity"], "executable_public")
    self.assertEqual(tools["dungeon-editor-lite"]["maturity"], "executable_public")
    self.assertEqual(tools["avatar-editor-lite"]["maturity"], "executable_public")
    forbidden_price_fields = {"price", "exact_price", "amount", "currency"}
    self.assertTrue(forbidden_price_fields.isdisjoint(catalog))
    for tool in tools.values():
        self.assertTrue(forbidden_price_fields.isdisjoint(tool))
```

- [ ] **Step 2: Run the focused test and confirm the red state**

Run: `rtk pytest -q tests/test_public_docs.py::PublicDocumentationTests::test_creative_tools_catalog_contract`  
Expected: failure because `creative-tools-catalog.json` does not exist.

- [ ] **Step 3: Create the JSON Schema**

Define these exact enums:

```json
{
  "maturity": [
    "executable_public",
    "prototype_local",
    "scaffolding_proxy",
    "planned",
    "available_external",
    "verification_required",
    "unavailable"
  ],
  "execution": ["local", "cloud", "hybrid", "not_applicable"],
  "pricing_model": [
    "free_open_source",
    "free",
    "free_noncommercial",
    "freemium",
    "one_time_purchase",
    "subscription",
    "credits",
    "revenue_limited",
    "project_budget_limited",
    "contact_sales",
    "mixed"
  ],
  "commercial_use": [
    "allowed",
    "conditional",
    "noncommercial_only",
    "plan_dependent",
    "asset_dependent",
    "model_dependent",
    "verification_required"
  ],
  "integration": ["direct", "conversion_required", "reference_only"]
}
```

Require `verified_on` dates, HTTPS official URLs, non-empty domains, inputs,
outputs, platforms, privacy, and bounded notes. Add a top-level
`recommendations` object whose domain entries contain 2-5 unique tool IDs and
one `default_tool` present in that list.

- [ ] **Step 4: Populate the reviewed catalog**

Include at least these IDs and no invented exact price:

```text
creature-editor-lite, city-editor-lite, architecture-editor-lite,
architecture-editor, dungeon-editor, creature-editor, avatar-editor,
city-editor, asset-factory, audio-factory, vault-webadmin, uo-godot-cli,
kanboard, botte-secrete,
twine, qgis, blender, inkarnate, world-machine, houdini,
material-maker, poly-haven, meshroom, substance-3d, maya, zbrush,
makehuman, vroid-studio, mixamo, cascadeur, metahuman,
reallusion-character-creator, audacity, lmms, reaper, fmod, wwise,
krita, gimp, inkscape, penpot, figma, comfyui, adobe-firefly,
meshy, elevenlabs, kdenlive, davinci-resolve, git-lfs
```

For Tools Suite entries, copy only public proof boundaries. For external tools,
use official URLs and a concise operational summary. Mark unverified or
asset/model-dependent rights explicitly.

- [ ] **Step 5: Implement fail-closed catalog validation**

Add constants matching the schema enums and implement:

```python
def creative_tools_catalog_errors() -> list[str]:
    # Parse schema and catalog.
    # Reject unknown enums, duplicate IDs, non-HTTPS URLs, exact-price keys,
    # unknown recommendation IDs, more than five recommendations per domain,
    # missing defaults, and Tools Suite Lite maturity drift.
```

Call the function from `validate()`. Add both new files to `REQUIRED_PATHS`.

- [ ] **Step 6: Run tests and validation**

Run:

```text
rtk pytest -q tests/test_public_docs.py::PublicDocumentationTests::test_creative_tools_catalog_contract
rtk python scripts/validate_docs.py
```

Expected: catalog test passes; source validation reports only stale manifest
until regeneration.

- [ ] **Step 7: Regenerate, verify, and commit**

```text
rtk python scripts/generate_manifest.py
rtk python scripts/validate_docs.py
rtk python -m unittest discover -s tests -v
rtk git add MANIFEST.sha256 schemas/creative-tools-catalog-v1.schema.json examples/creative-tools-catalog.json scripts/validate_docs.py tests/test_public_docs.py
rtk git commit -m "docs: add creative tools catalog contract"
```

### Task 2: French handbook, map drawing, and world tools

**Files:**
- Create: `docs/fr/tutorials/creative-production-handbook.md`
- Create: `docs/fr/how-to/draw-and-convert-map.md`
- Create: `docs/fr/reference/creative-tools-catalog.md`
- Create: `docs/fr/reference/world-map-and-structure-tools.md`
- Modify: `tests/test_public_docs.py`

**Interfaces:**
- Consumes: catalog domain IDs and current Tools Suite maturity.
- Produces: French beginner route from creative brief through map/world proposals.

- [ ] **Step 1: Add failing required-pair tests**

Extend the required bilingual-pair tuple with all ten new relative paths from
the design. Run the pair test and confirm failure before creating English files.

- [ ] **Step 2: Write the French handbook entry**

Use these sections exactly:

```text
Avant de commencer
Choisir un parcours gratuit/local, économique ou professionnel
Écriture et conception du monde
Cartes, terrains, villes et donjons
3D, matériaux et photogrammétrie
Personnages et animation
Audio, UI, VFX et vidéo
IA locale ou cloud
Import, optimisation, licences et provenance
Organisation Kanboard et Botte Secrète
Checklist avant de déclarer un asset prêt
```

Every section links to the relevant reference page and ends with one Kanboard
card outcome.

- [ ] **Step 3: Write the map drawing workflow**

Require orientation, scale/unknown-scale marker, boundaries, elevation intent,
water, roads, districts, landmarks, footprints, transitions, spawns, quest,
danger/safe zones, legend, and uncertainty.

Show the flow:

```text
PNG/JPEG/SVG + légende + fiche projet
→ analyse LM avec incertitudes
→ proposition uo.map-intent/v1
→ éditeur disponible en preview_only
→ corrections humaines
→ JSON versionné
→ schéma/hash/provenance
→ validation serveur
```

Provide a complete map-analysis prompt. State that an unavailable Map Editor
leaves a valid drawing/proposal artifact and a blocked Kanboard card.

- [ ] **Step 4: Write the catalog guide and world/structure reference**

Document the catalog columns and compare Tools Suite, QGIS, Blender, Inkarnate,
World Machine, Houdini, and the current Lite/full editors. Use pricing models,
not numbers. Distinguish direct, conversion-required, and reference-only paths.

- [ ] **Step 5: Validate French source and commit**

Run `rtk python scripts/validate_docs.py`; expected failures are missing English
pairs plus stale manifest only. Stage exactly the four French files and commit:

```text
rtk git commit -m "docs(fr): add creative production and map journey"
```

### Task 3: French 3D, character, audio, UI, VFX, video, and AI references

**Files:**
- Create: `docs/fr/reference/3d-assets-materials-and-photogrammetry-tools.md`
- Create: `docs/fr/reference/character-creature-and-animation-tools.md`
- Create: `docs/fr/reference/audio-2d-ui-vfx-and-video-tools.md`
- Create: `docs/fr/reference/local-and-cloud-ai-tools.md`
- Create: `docs/fr/reference/import-optimization-licensing-and-provenance.md`

**Interfaces:**
- Consumes: catalog records and format vocabulary.
- Produces: detailed French production references with safe conversion gates.

- [ ] **Step 1: Write 3D/material/photogrammetry reference**

Cover Asset Factory, Blender, Material Maker, Poly Haven, Meshroom, Substance
3D, Maya, ZBrush, Houdini, RealityCapture-class workflows, GLB/glTF, OBJ/FBX,
PLY/SPLAT/FOVEA, PBR channels, UVs, retopology, and human review. Preserve the
current negative fact: a splat contract does not prove a reviewed splat producer
or GPU/OpenXR runtime.

- [ ] **Step 2: Write character/creature/animation reference**

Cover Creature/Avatar editors, MakeHuman, VRoid, Mixamo, Cascadeur, MetaHuman,
Reallusion, Blender, rigging, retargeting, mocap, GLB/VRM/FBX conversion, and
asset-dependent rights. State Mixamo's biped limitation and keep gameplay stats
server-authoritative.

- [ ] **Step 3: Write audio/2D/UI/VFX/video reference**

Cover Audio Factory, Audacity, LMMS, REAPER, FMOD, Wwise, Krita, GIMP, Inkscape,
Penpot, Figma, Blender, Godot, Kdenlive, DaVinci Resolve, ElevenLabs, WAV/FLAC
masters, OGG runtime, SVG/PNG, fonts, shaders, cinematics, and middleware licence
gates.

- [ ] **Step 4: Write AI and import/licensing references**

Separate ComfyUI software from models, LoRAs, custom nodes, datasets, and output
rights. Cover Firefly, Meshy, ElevenLabs, cloud upload/privacy/training terms,
and local alternatives. Define format validation, LOD, collision, navigation,
texture compression, performance budgets, licence inventory, provenance, hashes,
and human approval.

- [ ] **Step 5: Run link and boundary validation**

Run: `rtk python scripts/validate_docs.py`  
Expected: no forbidden content or broken internal link; missing English pairs and
stale manifest remain.

- [ ] **Step 6: Commit the French reference set**

```text
rtk git add docs/fr/reference/3d-assets-materials-and-photogrammetry-tools.md docs/fr/reference/character-creature-and-animation-tools.md docs/fr/reference/audio-2d-ui-vfx-and-video-tools.md docs/fr/reference/local-and-cloud-ai-tools.md docs/fr/reference/import-optimization-licensing-and-provenance.md
rtk git commit -m "docs(fr): add creative tool production references"
```

### Task 4: Kanboard and Botte Secrète organization guide

**Files:**
- Create: `docs/fr/how-to/organize-project-kanboard-botte-secrete.md`
- Create: `docs/en/how-to/organize-project-kanboard-botte-secrete.md`
- Modify: `docs/{fr,en}/reference/llm-local-setup-prompts.md`

**Interfaces:**
- Consumes: Kanboard official board/API model and Botte Secrète public-safe capabilities.
- Produces: reusable board structure, card template, safe prompts, and explicit no-connector boundary.

- [ ] **Step 1: Write the French organization guide**

Define columns and swimlanes exactly as in the spec. Include this card template:

```markdown
## Objectif observable

## Entrées autorisées

## Outil retenu et alternatives

## Formats et conversion

## Licence, provenance et confidentialité

## Critères d'acceptation

## Preuves attendues

## Prompt LM sans secret

## Blocage actuel
```

Explain Kanboard backups, attachments, optional plug-in review, and user API
security. State that the application API is not the default because it exposes
all procedures without project permission checks.

- [ ] **Step 2: Write the English mirror**

Preserve column semantics, API boundaries, code identifiers, and URLs. Translate
only human prose.

- [ ] **Step 3: Add Botte Secrète prompts**

Add complete prompts for converting a creative need into a Kanboard card,
routing a card through Botte Secrète, and reviewing evidence before Done. Each
prompt prohibits secrets and automatic task mutation.

- [ ] **Step 4: Validate and commit**

Run source validation and focused bilingual tests. Commit exactly the two guides
and prompt files:

```text
rtk git commit -m "docs: add Kanboard and Botte Secrete workflow"
```

### Task 5: English production handbook and reference mirrors

**Files:**
- Create: English counterparts for the nine French files from Tasks 2-3.

**Interfaces:**
- Consumes: approved French structure and machine catalog IDs.
- Produces: complete English parity without changing identifiers, formats, or licence meaning.

- [ ] **Step 1: Translate isolated pages with local routing when available**

Use the project local-LLM policy for first-pass translation only. Preserve
headings, commands, URLs, tool IDs, status labels, file formats, and code blocks.
If the local cluster times out or returns incomplete content, translate directly
and record the fallback.

- [ ] **Step 2: Review every English page manually**

Check commercial-use qualifiers, Tools Suite maturity, cloud privacy warnings,
direct/conversion labels, and Kanboard/Botte boundaries. Do not accept a literal
translation that changes legal meaning.

- [ ] **Step 3: Run bilingual and link validation**

Run:

```text
rtk pytest -q tests/test_public_docs.py::PublicDocumentationTests::test_local_setup_has_required_bilingual_pairs
rtk python scripts/validate_docs.py
```

Expected: bilingual and link gates pass; manifest remains stale.

- [ ] **Step 4: Commit English mirrors**

```text
rtk git add docs/en/tutorials/creative-production-handbook.md docs/en/how-to/draw-and-convert-map.md docs/en/reference/creative-tools-catalog.md docs/en/reference/world-map-and-structure-tools.md docs/en/reference/3d-assets-materials-and-photogrammetry-tools.md docs/en/reference/character-creature-and-animation-tools.md docs/en/reference/audio-2d-ui-vfx-and-video-tools.md docs/en/reference/local-and-cloud-ai-tools.md docs/en/reference/import-optimization-licensing-and-provenance.md
rtk git commit -m "docs(en): add creative production handbook"
```

### Task 6: Existing journey, prompts, and human/LLM indexes

**Files:**
- Modify: `docs/{fr,en}/tutorials/create-first-local-world.md`
- Modify: `docs/{fr,en}/reference/engine-template-world-matrix.md`
- Modify: `docs/{fr,en}/reference/llm-local-setup-prompts.md`
- Modify: `docs/llm/context-index.json`
- Modify: `docs/llm/README.md`
- Modify: `llms.txt`
- Modify: `README.md`

**Interfaces:**
- Consumes: all new bilingual pages and catalog paths.
- Produces: discoverable human and machine navigation.

- [ ] **Step 1: Link the handbook from the existing journey**

After topology choice, add drawing-map and full-creative-production branches.
After local setup, link Kanboard/Botte organization. Preserve the current server
release hard stop.

- [ ] **Step 2: Refresh the engine/world matrix**

Add drawn-map inputs, `uo.map-intent/v1`, direct/conversion labels, and current
Creature/City/Architecture Editor Lite evidence.

- [ ] **Step 3: Register every page in LLM indexes**

Add unique FR/EN IDs, correct Diátaxis types, goals, audiences, exact paths, and
`mutating: false`. Add the handbook, catalog, map guide, organization guide, and
all reference pages to `llms.txt`.

- [ ] **Step 4: Update LLM safety rules and README**

Require current `verified_on`, official-source checks, no exact pricing, no
secret upload, and no automatic Kanboard mutation. Add concise FR/EN entry links
to root README without removing Discord or existing local-setup links.

- [ ] **Step 5: Test navigation and commit**

Add a test that requires handbook and catalog paths in `llms.txt` and
`context-index.json`. Run all source tests, then commit exact index files:

```text
rtk git commit -m "docs: index creative production handbook"
```

### Task 7: Offline HTML, publication status, and fresh-copy proof

**Files:**
- Modify: `PUBLICATION_STATUS.md`
- Modify: `MANIFEST.sha256`
- Generated only: `build/local-setup-html/`

**Interfaces:**
- Consumes: complete canonical source.
- Produces: a validated offline artifact still labelled as local proof, not deployed.

- [ ] **Step 1: Update publication status honestly**

Record source/catalog/offline-build validation and current three Lite executable
slices. State that no Kanboard instance, Botte connector, Tools Suite release,
Web deployment, server ZIP, purchase, or commercial-right certification is
proven.

- [ ] **Step 2: Regenerate source manifest**

Run `rtk python scripts/generate_manifest.py` and require a nonzero bounded file
count that includes every new page, schema, and catalog.

- [ ] **Step 3: Run complete source proof**

```text
rtk python scripts/validate_docs.py
rtk python -m unittest discover -s tests -v
rtk pytest -q
rtk python scripts/fresh_copy_check.py
rtk git diff --check
```

Expected: all commands exit 0.

- [ ] **Step 4: Build and verify offline HTML**

Using the existing isolated MkDocs environment, run:

```text
$docsCommit = (rtk git rev-parse --short=7 HEAD).Trim()
rtk .venv\Scripts\python.exe scripts/build_static_docs.py --output-dir build/local-setup-html --documentation-version docs-2026.08 --server-compatibility unavailable --source-commit $docsCommit
```

Expected: no remote runtime assets, all internal links valid, creative catalog
and schema copied, and `docs-build-manifest.json` hashes every output file.

- [ ] **Step 5: Scan secrets**

Run: `rtk gitleaks detect --source . --no-git --redact --exit-code 1`  
Expected: no leaks.

- [ ] **Step 6: Commit final status and manifest**

```text
rtk git add PUBLICATION_STATUS.md MANIFEST.sha256
rtk git commit -m "docs: validate creative production handbook"
```

- [ ] **Step 7: Run project hygiene**

Run the configured Botte Secrète checkup from the Ultimate Odycer root with the
documented `PYTHONPATH`. Treat a bounded timeout as inconclusive, not successful,
and retain the scoped repository proofs.
