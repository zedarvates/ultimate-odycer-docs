# Local Setup Content and Static HTML Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish the bilingual beginner-to-local-runtime journey, advanced shortcuts, LLM prompts, and a deterministic offline HTML bundle from one Markdown source.

**Architecture:** Markdown under `docs/fr` and `docs/en` remains canonical. A machine-readable catalog records component status and compatibility, while a strict MkDocs build produces a self-contained HTML tree plus a checksummed build manifest for both the Web portal and server release packager.

**Tech Stack:** Python 3.11+, `unittest`, MkDocs 1.6.1, JSON, Markdown, SHA-256

**Spec:** `docs/superpowers/specs/2026-08-23-local-setup-documentation-design.md`

## Global Constraints

- Godot is the fully detailed default path; Three.js, Unity, Unreal Engine, and FoveaCore remain alternatives with explicit support limits.
- Windows is primary, Linux is a documented variant, macOS is out of scope, and a future mobile application targets Android only.
- Use only `available`, `under_construction`, `planned`, and `unavailable` for component status.
- Use only `observed`, `estimated`, `decision`, and `unavailable` for measurements and hardware claims.
- `https://www.ultimateodycer.com/releases/` is the sole server download page; an empty release list must stop the executable journey honestly.
- Never publish proprietary server code, credentials, production data, internal paths, unaudited assets, or commercial components.
- Do not claim runtime, client, PostgreSQL, Tools Suite, ComfyUI, network, or release proof from documentation tests.
- Preserve the existing Discord link and all concurrent work; stage only exact paths named by a task.
- All shell commands run with the `rtk` prefix.

---

## File Structure

- `schemas/local-setup-catalog-v1.schema.json`: public vocabulary and required catalog fields.
- `examples/local-setup-catalog.json`: current engine, template, topology, platform, and component statuses.
- `docs/{fr,en}/tutorials/create-first-local-world.md`: canonical beginner entry point.
- `docs/{fr,en}/reference/engine-template-world-matrix.md`: engine, template, and topology decisions.
- `docs/{fr,en}/how-to/install-local-server-windows.md`: Windows, Docker, PostgreSQL, release gate, and server startup.
- `docs/{fr,en}/how-to/install-local-server-linux.md`: bounded Linux differences.
- `docs/{fr,en}/how-to/backup-and-test-restore-postgresql.md`: persistence, backup, and non-destructive restore check.
- `docs/{fr,en}/how-to/connect-godot-template.md`: compatibility check and local Godot connection.
- `docs/{fr,en}/how-to/troubleshoot-local-setup.md`: symptom-to-proof troubleshooting.
- `docs/{fr,en}/reference/local-setup-acceptance-checklist.md`: completion gate.
- `docs/{fr,en}/reference/local-setup-advanced-index.md`: shortcuts for experienced operators.
- `docs/{fr,en}/reference/llm-local-setup-prompts.md`: safe prompts and question/answer examples.
- `requirements-docs.txt`: pinned static-site dependency.
- `mkdocs.yml`: bilingual navigation and offline-compatible build settings.
- `docs/assets/stylesheets/ultimate-odycer-docs.css`: local-only presentation.
- `scripts/build_static_docs.py`: strict builder and build-manifest writer.
- `tests/test_static_docs.py`: offline asset, checksum, and metadata tests.
- `README.md`, `llms.txt`, `docs/llm/context-index.json`: human and LM entry points.

### Task 1: Machine-readable local-setup catalog

**Files:**
- Create: `schemas/local-setup-catalog-v1.schema.json`
- Create: `examples/local-setup-catalog.json`
- Modify: `scripts/validate_docs.py`
- Modify: `tests/test_public_docs.py`

**Interfaces:**
- Consumes: existing public status vocabulary from `docs/llm/context-index.json`.
- Produces: `local_setup_catalog_errors() -> list[str]` and catalog schema `ultimate-odycer.local-setup-catalog.v1`.

- [ ] **Step 1: Write failing catalog tests**

Add tests that load `examples/local-setup-catalog.json` and assert:

```python
catalog = json.loads((ROOT / "examples/local-setup-catalog.json").read_text(encoding="utf-8"))
self.assertEqual(catalog["schema_version"], "ultimate-odycer.local-setup-catalog.v1")
self.assertEqual(catalog["release_page"], "https://www.ultimateodycer.com/releases/")
self.assertEqual(catalog["current_server_release"], "unavailable")
self.assertEqual({item["id"] for item in catalog["platforms"]}, {"windows", "linux", "android", "macos"})
self.assertIn("ultod-client-godot-open-city-crime-rpg-template", {item["repository"] for item in catalog["templates"]})
```

- [ ] **Step 2: Run the focused test and observe the missing catalog failure**

Run: `rtk python -m unittest tests.test_public_docs.PublicDocumentationTests.test_local_setup_catalog_contract -v`  
Expected: failure because `examples/local-setup-catalog.json` does not exist.

- [ ] **Step 3: Add the schema and current catalog**

The catalog must encode these decisions exactly:

```json
{
  "schema_version": "ultimate-odycer.local-setup-catalog.v1",
  "release_page": "https://www.ultimateodycer.com/releases/",
  "current_server_release": "unavailable",
  "default_engine": "godot",
  "primary_platform": "windows",
  "platforms": [
    {"id": "windows", "role": "primary", "status": "available"},
    {"id": "linux", "role": "variant", "status": "planned"},
    {"id": "android", "role": "future-mobile", "status": "planned"},
    {"id": "macos", "role": "unsupported", "status": "unavailable"}
  ],
  "templates": [
    {"repository": "ultod-client-godot-classic-3d-mmorpg-template", "engine": "godot", "status": "under_construction"},
    {"repository": "ultod-client-godot-vr-mmorpg-template", "engine": "godot", "status": "under_construction"},
    {"repository": "ultod-client-threejs-2-5d-mmorpg-template", "engine": "threejs", "status": "under_construction"},
    {"repository": "ultod-client-foveacore-fps-rpg-template", "engine": "foveacore", "status": "under_construction"},
    {"repository": "ultod-client-godot-open-city-crime-rpg-template", "display_name": "Prêt à tout faire pour de l'argent", "engine": "godot", "status": "planned"}
  ],
  "topologies": ["flat_map", "planet", "mega_planet", "solar_system"],
  "components": [
    {"id": "server", "status": "unavailable", "install_mode": "required"},
    {"id": "webadmin", "status": "under_construction", "install_mode": "optional"},
    {"id": "tools-suite", "status": "under_construction", "install_mode": "optional-modules"},
    {"id": "asset-factory-comfyui", "status": "under_construction", "install_mode": "optional-module"}
  ],
  "hardware_profiles": [
    {"id": "dedicated_server", "status": "estimated", "cpu_cores": 4, "ram_gib": 8, "free_ssd_gib": 20},
    {"id": "shared_workstation", "status": "estimated", "cpu_cores": 6, "ram_gib": 16, "free_ssd_gib": 40},
    {"id": "creation_workstation", "status": "estimated", "cpu_cores": 8, "ram_gib": 32, "free_ssd_gib": 100, "gpu_requirement": "unavailable"}
  ]
}
```

The hardware values are planning estimates for a first local trial, not certified release minima. A future release replaces them only with reproducible `observed` measurements and retains the estimate history.

The schema restricts every status with JSON `enum` values and requires unique IDs in the validator.

- [ ] **Step 4: Implement fail-closed catalog validation**

Add `local_setup_catalog_errors()` to reject unknown statuses, duplicate template repositories, a non-HTTPS release page, a default engine other than Godot, a primary platform other than Windows, or a non-`unavailable` current release without a concrete artifact record.

- [ ] **Step 5: Run structural validation**

Run: `rtk python scripts/validate_docs.py`  
Expected: validation fails only because the manifest has not yet been regenerated.

- [ ] **Step 6: Commit the catalog contract**

```text
rtk git add schemas/local-setup-catalog-v1.schema.json examples/local-setup-catalog.json scripts/validate_docs.py tests/test_public_docs.py
rtk git commit -m "docs: add local setup catalog contract"
```

### Task 2: French beginner journey and decision material

**Files:**
- Create: `docs/fr/tutorials/create-first-local-world.md`
- Create: `docs/fr/reference/engine-template-world-matrix.md`
- Create: `docs/fr/how-to/install-local-server-windows.md`
- Create: `docs/fr/how-to/install-local-server-linux.md`
- Create: `docs/fr/how-to/backup-and-test-restore-postgresql.md`
- Create: `docs/fr/how-to/connect-godot-template.md`
- Create: `docs/fr/reference/local-setup-acceptance-checklist.md`

**Interfaces:**
- Consumes: catalog IDs and statuses from Task 1; public release archive contract (`VERSION`, `SHA256SUMS.txt`, `deploy/QUICKSTART.md`, `docs/index.html`).
- Produces: complete French path from project idea to verified local startup, with a hard stop when no release exists.

- [ ] **Step 1: Add a failing bilingual-pair expectation for the intended paths**

Extend `tests/test_public_docs.py` with a list of seven required French paths and assert each future English counterpart exists. Run the test before creating English files and record the expected missing-pair failure.

- [ ] **Step 2: Write the French entry tutorial**

Use this exact sequence of gates:

```text
Projet et vision créative
→ moteur
→ template
→ topologie
→ profil matériel
→ page officielle des releases
→ Docker/PostgreSQL
→ serveur
→ Godot
→ sauvegarde/restauration de contrôle
→ validation finale
→ prompts LM
```

The release gate must say that, while `current_server_release` is `unavailable`, the reader stops after preparing and saving the project brief. It must not offer an internal binary or source build.

- [ ] **Step 3: Write the engine, template, and world matrix**

Include the five catalog templates, Godot as default, the original open-city template name, and the four topology rules. Describe a GTA-like only as a functional comparison and map its default to `flat_map`; prohibit copying protected identity, content, code, or assets.

- [ ] **Step 4: Write the Windows and Linux install guides**

The Windows guide must contain commands for:

```powershell
Get-FileHash -Algorithm SHA256 .\ultimate-odycer-server-<version>-windows-x86_64.zip
wsl --version
docker version
docker compose version
docker compose -f .\deploy\docker-compose.yml up -d postgres
docker compose -f .\deploy\docker-compose.yml ps
```

Angle-bracket values are explicitly described as values copied from a real release entry, never guessed. The Linux guide covers only the command differences (`sha256sum`, Docker Engine, executable permission) and links back to the canonical journey.

The Windows guide presents three clearly labeled planning profiles: dedicated server (4 cores, 8 GiB RAM, 20 GiB free SSD), shared workstation (6 cores, 16 GiB RAM, 40 GiB free SSD), and creation workstation (8 cores, 32 GiB RAM, 100 GiB free SSD). It labels every value `estimated`, explains that the shared profile reserves headroom for normal work, and leaves ComfyUI GPU/VRAM requirements `unavailable` until a module and model set are published and measured.

It also presents two installation choices: server only, or server plus individually selected compatible Tools Suite modules. The latter stays blocked while the Tools Suite catalog is `under_construction`.

- [ ] **Step 5: Write persistence and restore-check guidance**

Distinguish the named Docker volume from a backup stored on the Windows host. Require a custom-format `pg_dump`, a SHA-256 digest for the backup, restoration into a separate verification database, a row/schema check, and removal of only that verification database. Warn that `docker compose down -v` and volume-pruning commands destroy persistent data.

- [ ] **Step 6: Write the Godot connection and acceptance checklist**

Require matching compatibility identifiers, loopback-only addresses, a healthy PostgreSQL connection without SQLite fallback, login and game connection, visible test avatar, one minimal action, restart persistence, backup/restore proof, and no automatically opened Internet port. Mark unavailable template runtime checks as blocked, not passed.

- [ ] **Step 7: Run Markdown and public-boundary validation**

Run: `rtk python scripts/validate_docs.py`  
Expected: only missing English pairs and stale manifest remain.

- [ ] **Step 8: Commit French content**

Stage exactly the seven French files and commit:

```text
rtk git commit -m "docs(fr): add first local world journey"
```

### Task 3: English mirror, troubleshooting, advanced index, and LLM prompts

**Files:**
- Create: English counterparts for every Task 2 path.
- Create: `docs/{fr,en}/how-to/troubleshoot-local-setup.md`
- Create: `docs/{fr,en}/reference/local-setup-advanced-index.md`
- Create: `docs/{fr,en}/reference/llm-local-setup-prompts.md`
- Modify: `docs/llm/context-index.json`
- Modify: `docs/llm/README.md`
- Modify: `llms.txt`

**Interfaces:**
- Consumes: Task 2 headings, commands, gates, and status meanings.
- Produces: equivalent English content, fast paths, symptom-to-proof diagnostics, and safe LM prompt templates.

- [ ] **Step 1: Write English counterparts with structural parity**

Keep the same heading IDs, command scope, release hard stop, and acceptance criteria. Do not translate command names, filenames, catalog IDs, JSON keys, or URLs.

- [ ] **Step 2: Add troubleshooting pages**

Cover these exact symptoms: no public release; SHA mismatch; WSL/Docker unavailable; PostgreSQL unhealthy; server using SQLite fallback; port already in use; server healthy but Godot disconnected; missing volume; failed backup; failed restore check; shared workstation saturation; unavailable Tools Suite module.

- [ ] **Step 3: Add advanced indexes**

Index direct checks for Docker, PostgreSQL health, release checksum, server health, port listeners, logs, backup digest, compatibility metadata, and local-only binding. Every shortcut links to the explanatory source rather than duplicating it.

- [ ] **Step 4: Add safe LM prompts**

Provide complete prompts for project briefing, engine/template choice, world topology, Windows prerequisites, release verification, PostgreSQL diagnosis, Godot connection, validation failure, and next-step planning. Every prompt includes:

```text
Read current versions and status first. Do not invent a package or capability.
Never ask me to reveal a secret. Preserve existing files and data.
Give me one beginner-sized step at a time with an expected result.
Stop for confirmation before deletion, network exposure, purchase, deployment, or publication.
```

- [ ] **Step 5: Register all new sources in the LM indexes**

Add unique document IDs, correct `language`, Diátaxis `type`, beginner or advanced `audience`, exact path, and `mutating: false`. Add the entry tutorial and prompt catalog to `llms.txt`.

- [ ] **Step 6: Run bilingual and LM validation**

Run: `rtk python scripts/validate_docs.py`  
Expected: no bilingual or LM index errors; stale manifest is the sole remaining error.

- [ ] **Step 7: Commit bilingual support material**

```text
rtk git commit -m "docs: add local setup support and LLM prompts"
```

### Task 4: Deterministic static HTML bundle

**Files:**
- Create: `requirements-docs.txt`
- Create: `mkdocs.yml`
- Create: `docs/index.md`
- Create: `docs/assets/stylesheets/ultimate-odycer-docs.css`
- Create: `scripts/build_static_docs.py`
- Create: `tests/test_static_docs.py`
- Modify: `.gitignore`

**Interfaces:**
- Consumes: canonical Markdown and `docs/llm/context-index.json`.
- Produces: `build/local-setup-html/` containing `index.html`, local assets, LM indexes, and `docs-build-manifest.json`.

- [ ] **Step 1: Write failing static-build tests**

Test a fixture output with these assertions:

```python
self.assertTrue((site / "index.html").is_file())
self.assertTrue((site / "docs-build-manifest.json").is_file())
self.assertEqual(manifest["schema"], "ultimate-odycer.docs-build.v1")
self.assertEqual(manifest["compatibility"]["server"], "unavailable")
self.assertIn("index.html", manifest["files"])
self.assertFalse(external_runtime_assets(site))
self.assertEqual(verify_manifest(site), [])
```

- [ ] **Step 2: Pin and configure MkDocs**

Set `requirements-docs.txt` to `mkdocs==1.6.1`. Configure `use_directory_urls: false`, strict navigation, local CSS, French and English sections, and `site_dir: build/local-setup-html`. Do not add remote themes, analytics, fonts, JavaScript, or CDN assets.

- [ ] **Step 3: Implement the builder**

Expose this CLI:

```text
python scripts/build_static_docs.py \
  --output-dir build/local-setup-html \
  --documentation-version docs-2026.08 \
  --server-compatibility unavailable \
  --source-commit <40-hex-commit>
```

The script validates bounded filesystem-safe values, requires an output directory inside repository `build/`, refuses symlinks, runs `python -m mkdocs build --strict`, copies `llms.txt` and `docs/llm/context-index.json`, scans `script/src`, `img/src`, `source/src`, and stylesheet links for remote runtime assets, hashes every file except the build manifest, and writes sorted JSON.

- [ ] **Step 4: Run the static builder and tests**

Run:

```text
rtk python scripts/build_static_docs.py --output-dir build/local-setup-html --documentation-version docs-2026.08 --server-compatibility unavailable --source-commit 56eab71
rtk python -m unittest tests.test_static_docs -v
```

Expected: build succeeds; every asset required to read the HTML is local; all declared SHA-256 values match.

- [ ] **Step 5: Commit the builder**

```text
rtk git commit -m "build: generate offline documentation bundle"
```

### Task 5: Human entry points and final repository proof

**Files:**
- Modify: `README.md`
- Modify: `MANIFEST.sha256`
- Modify: `PUBLICATION_STATUS.md`

**Interfaces:**
- Consumes: all earlier tasks.
- Produces: discoverable public entry points and a clean reproducible repository state.

- [ ] **Step 1: Add French and English local-setup links to README**

Keep the Discord line. Label the server release and Tools Suite states honestly and link the official release page.

- [ ] **Step 2: Update publication status without claiming runtime proof**

Record that source documentation and offline HTML generation are validated. State that no public server release, client runtime, site deployment, or ZIP inclusion is proven by this repository gate.

- [ ] **Step 3: Regenerate and verify the source manifest**

Run:

```text
rtk python scripts/generate_manifest.py
rtk python scripts/validate_docs.py
rtk python -m unittest discover -s tests -v
rtk git diff --check
```

Expected: all commands exit 0.

- [ ] **Step 4: Verify a fresh copy**

Run the existing fresh-copy check against a temporary destination outside the repository. Expected: internal links, manifest, tests, and source boundaries pass in the copy.

- [ ] **Step 5: Commit final entry-point changes**

```text
rtk git add README.md PUBLICATION_STATUS.md MANIFEST.sha256
rtk git commit -m "docs: publish local setup entry points"
```

- [ ] **Step 6: Run project hygiene**

From `F:/_Serv ULtimate Od`, run the configured Botte Secrète checkup with `PYTHONPATH=C:/Users/redga/botte-secrete`. If it produces no result within the bounded diagnostic window, record it as inconclusive without weakening the scoped repository proofs.
