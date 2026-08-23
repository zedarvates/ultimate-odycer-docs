# Local Setup Server Release Bundle Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Require the validated offline documentation, safe PostgreSQL persistence helpers, and exact compatibility metadata in every future Windows customer-release archive.

**Architecture:** The existing fail-closed Python packager receives a required docs-build directory, verifies its manifest and compatibility before collecting it under `docs/`, and includes every file in the release SHA-256 inventory. Separate Docker-safe scripts create a host backup and test restoration in an isolated verification database.

**Tech Stack:** Python 3.11+, `unittest`, PowerShell 7, Docker Compose, PostgreSQL 16, ZIP/SHA-256

**Spec:** `artifacts/github-prep/ultimate-odycer-docs/docs/superpowers/specs/2026-08-23-local-setup-documentation-design.md`

## Global Constraints

- Every server, test, docs, and DevOps file stays under `Development/Backend/Servers/zig-server-v2/`.
- Existing packager and E2E files are concurrent uncommitted additions. Inspect their scoped diff and preserve their current behavior; never replace, reset, stash, clean, or bulk-stage them.
- No real archive is published, uploaded, tagged, or added to the Web releases list by this plan.
- An absent, invalid, mismatched, or symlinked documentation bundle blocks packaging.
- PostgreSQL 16 uses a named volume, while backups live outside that volume on the Windows host.
- Restore verification uses a separate database and never drops the live `ultimate_odycer` database.
- PostgreSQL, Redis, GameServer, LoginServer, and WebAdmin stay on loopback for the local path.
- Do not claim Godot rendering or a public release from packager unit tests or isolated archive smoke tests.
- All shell commands run with the `rtk` prefix.

---

## File Structure

- `scripts/package_customer_release.py`: docs validation, payload inclusion, and manifest metadata.
- `tests/test_package_customer_release.py`: docs bundle and payload unit tests.
- `tests/e2e/customer_release_archive_e2e.py`: extracted archive docs and persistence-helper verification.
- `deploy/docker-compose.yml`: loopback-only PostgreSQL and Redis bindings.
- `deploy/backup-postgres.ps1`: fail-closed Docker backup to host.
- `deploy/test-restore-postgres.ps1`: non-destructive restore verification database.
- `deploy/QUICKSTART.md`: release-local path into `docs/index.html` and persistence gate.
- `tests/test_customer_deploy_contract.py`: compose, helper, and quickstart contract tests.

### Task 0: Concurrent-work ownership gate

**Files:**
- Inspect only: `scripts/package_customer_release.py`
- Inspect only: `tests/test_package_customer_release.py`
- Inspect only: `tests/e2e/customer_release_archive_e2e.py`
- Inspect only: all existing deploy files named by Tasks 3-5.

**Interfaces:**
- Consumes: scoped Git status and diff under `Development/Backend/Servers/zig-server-v2/`.
- Produces: a safe go/no-go decision before editing the staged packager foundation.

- [ ] **Step 1: Inspect exact server paths**

Run scoped `rtk git status --short -- <paths>` and `rtk git diff --cached -- <paths>` from the monorepo root.

- [ ] **Step 2: Enforce the ownership gate**

The three packager/E2E files are currently staged additions. Do not modify or recommit them until their owner has committed them or the user explicitly authorizes inclusion of their complete staged content. Do not unstage them. New non-overlapping test or deploy files may be prepared, but Tasks 1, 2, 4, and 6 remain blocked.

- [ ] **Step 3: Continue only on a stable baseline**

Re-run scoped status and continue when the packager foundation is present in the current commit and the named target files are clean.

### Task 1: Documentation bundle validation in the packager

**Files:**
- Modify: `scripts/package_customer_release.py`
- Modify: `tests/test_package_customer_release.py`

**Interfaces:**
- Consumes: `--documentation-dir PATH` with `docs-build-manifest.json` schema `ultimate-odycer.docs-build.v1`.
- Produces: `DocumentationBundle(root: Path, manifest_sha256: str, documentation_version: str, source_commit: str, files: tuple[PayloadFile, ...])`.

- [ ] **Step 1: Write failing validation tests**

Add fixtures and tests for a valid bundle plus rejection of: missing manifest, wrong schema, server compatibility mismatch, missing index, unknown file, digest mismatch, symlink, unsafe relative path, and private key marker.

```python
bundle = release.validate_documentation_bundle(docs_root, "0.1.0")
self.assertEqual(bundle.documentation_version, "docs-2026.08")
self.assertEqual(bundle.files[0].target.parts[0], "docs")
```

- [ ] **Step 2: Run the focused tests**

Run: `rtk python -m unittest tests.test_package_customer_release.PackageCustomerReleaseTests.test_valid_documentation_bundle -v`  
Expected: attribute-not-found failure.

- [ ] **Step 3: Implement `DocumentationBundle` and validator**

Require:

```text
schema == ultimate-odycer.docs-build.v1
compatibility.server == requested release version
documentation_version is a bounded filesystem-safe identifier
source_commit matches 7 to 40 lowercase hexadecimal characters
files includes index.html
actual regular-file set equals declared files plus docs-build-manifest.json
all SHA-256 digests match
no symlink, traversal, hidden runtime state, or private key marker
```

Map every declared file to `docs/<relative>` and the manifest to `docs/docs-build-manifest.json`.

- [ ] **Step 4: Run packager unit tests**

Run: `rtk python -m unittest tests.test_package_customer_release -v`  
Expected: all tests pass.

- [ ] **Step 5: Commit docs validation**

```text
rtk git add Development/Backend/Servers/zig-server-v2/scripts/package_customer_release.py Development/Backend/Servers/zig-server-v2/tests/test_package_customer_release.py
rtk git commit -m "feat(release): validate offline documentation bundle"
```

### Task 2: Require docs in release payload and manifest

**Files:**
- Modify: `scripts/package_customer_release.py`
- Modify: `tests/test_package_customer_release.py`
- Modify: `tests/e2e/customer_release_archive_e2e.py`

**Interfaces:**
- Consumes: `DocumentationBundle` from Task 1.
- Produces: release manifest `documentation` object and checksummed `docs/` tree.

- [ ] **Step 1: Add failing payload and manifest tests**

Assert `--documentation-dir` is required, `build_payload(..., documentation_bundle)` includes `docs/index.html`, and generated metadata has:

```json
{
  "schema": "ultimate-odycer.docs-build.v1",
  "path": "docs/index.html",
  "documentation_version": "docs-2026.08",
  "source_commit": "<hex>",
  "manifest_sha256": "<64 lowercase hex>"
}
```

- [ ] **Step 2: Patch CLI and payload construction**

Add required `--documentation-dir`. Validate it after `args.version`, pass the bundle into `build_payload`, and append its files with provenance `validated public documentation bundle`.

- [ ] **Step 3: Add release manifest linkage**

Add the metadata object before manifest serialization. Because docs files are normal payload items, their hashes and sizes automatically enter `files` and `SHA256SUMS.txt`.

- [ ] **Step 4: Extend extracted-archive verification**

In both `verify_extracted()` and the customer-release E2E, load `docs/docs-build-manifest.json`, check the release manifest linkage, verify every docs digest, and require `docs/index.html` to contain an HTML doctype.

- [ ] **Step 5: Run focused tests**

Run:

```text
rtk python -m unittest tests.test_package_customer_release -v
rtk python -m py_compile scripts/package_customer_release.py tests/e2e/customer_release_archive_e2e.py
```

Expected: all tests and compilation pass.

- [ ] **Step 6: Commit archive integration**

```text
rtk git commit -m "feat(release): embed version-matched offline docs"
```

### Task 3: Loopback-only Docker persistence contract

**Files:**
- Modify: `deploy/docker-compose.yml`
- Create: `tests/test_customer_deploy_contract.py`

**Interfaces:**
- Consumes: Docker Compose environment variable `ODYCER_DB_PASSWORD`.
- Produces: PostgreSQL host port `5433` and Redis host port `6379`, both bound only to the IPv4 loopback address, with named volume `odycer_pgdata`.

- [ ] **Step 1: Write failing compose contract test**

Parse the YAML as text without adding a YAML dependency and assert:

```python
loopback = ".".join(("127", "0", "0", "1"))
self.assertIn(f'{loopback}:5433:5432', compose)
self.assertIn(f'{loopback}:6379:6379', compose)
self.assertIn('odycer_pgdata:/var/lib/postgresql/data', compose)
self.assertNotIn('${ODYCER_DB_PASSWORD:-change_me_db_password}', compose)
```

- [ ] **Step 2: Run the focused test and observe failure**

Run: `rtk python -m unittest tests.test_customer_deploy_contract -v`.

- [ ] **Step 3: Harden Compose defaults**

Bind both published ports to the IPv4 loopback address. Require `${ODYCER_DB_PASSWORD:?Set ODYCER_DB_PASSWORD}` so the default password cannot start PostgreSQL. Keep PostgreSQL 16 Alpine, the named volume, and the current healthcheck.

- [ ] **Step 4: Validate Compose rendering without starting containers**

Set a temporary non-secret test password in the command environment and run `rtk docker compose -f deploy/docker-compose.yml config`. Expected: valid configuration with loopback bindings; no container is started.

- [ ] **Step 5: Commit the persistence contract**

```text
rtk git commit -m "security(deploy): keep local databases on loopback"
```

### Task 4: Safe backup and non-destructive restore check

**Files:**
- Create: `deploy/backup-postgres.ps1`
- Create: `deploy/test-restore-postgres.ps1`
- Modify: `tests/test_customer_deploy_contract.py`
- Modify: `scripts/package_customer_release.py`

**Interfaces:**
- Consumes: running Compose service `postgres`, `ODYCER_DB_PASSWORD`, optional bounded `-BackupDirectory`.
- Produces: host file `backups/ultimate_odycer_<UTC timestamp>.dump`, adjacent `.sha256`, and a restore-check result using database `ultimate_odycer_restore_check`.

- [ ] **Step 1: Write failing script contract tests**

Assert both scripts use strict mode, require `ODYCER_DB_PASSWORD` presence without printing it, verify resolved backup paths remain within the selected backup directory, use `docker compose`, and never contain `DROP DATABASE ultimate_odycer`.

- [ ] **Step 2: Implement backup through the container**

The script creates `/tmp/ultimate_odycer.dump` inside the PostgreSQL container using `pg_dump -Fc`, copies it to a temporary host filename, removes the container temporary file, atomically renames the host file, writes its SHA-256, and returns a nonzero code on every failed subprocess. It never supplies a fallback credential.

- [ ] **Step 3: Implement restore verification in a separate database**

The script validates the supplied dump hash, copies it into the container, drops only `ultimate_odycer_restore_check`, recreates that verification database, restores with `pg_restore`, queries at least the migration/version table and one application table selected from the release schema contract, then drops only the verification database and removes the container temporary file in `finally`.

- [ ] **Step 4: Include helpers in customer archives**

Add both filenames to `DEPLOY_FILES`. Extend unit/E2E assertions so they are present, checksummed, and free of hard-coded passwords.

- [ ] **Step 5: Run script syntax and contract tests**

Run:

```text
rtk proxy powershell -NoProfile -File deploy/backup-postgres.ps1 -WhatIf
rtk proxy powershell -NoProfile -File deploy/test-restore-postgres.ps1 -WhatIf
rtk python -m unittest tests.test_customer_deploy_contract tests.test_package_customer_release -v
```

Expected: `-WhatIf` validates prerequisites and planned bounded paths without mutating PostgreSQL; all Python tests pass.

- [ ] **Step 6: Commit persistence helpers**

```text
rtk git commit -m "feat(deploy): add verified PostgreSQL backup workflow"
```

### Task 5: Align the release-local quickstart

**Files:**
- Modify: `deploy/QUICKSTART.md`
- Modify: `tests/test_customer_deploy_contract.py`

**Interfaces:**
- Consumes: archive layout from Tasks 2 and 4.
- Produces: concise path into `docs/index.html`, server-only versus optional Tools Suite explanation, and mandatory persistence gate.

- [ ] **Step 1: Add failing quickstart assertions**

Require the guide to mention `docs/index.html`, `backup-postgres.ps1`, `test-restore-postgres.ps1`, the named volume, the official releases URL, and Tools Suite status `en construction`. Reject the claim that all editors are present in the server archive.

- [ ] **Step 2: Rewrite contradictory release claims**

State that the server archive contains the server, WebAdmin files already listed by its verified bundle, deployment helpers, and version-matched offline docs. State that dungeon, city, architecture, monster, avatar, Asset Factory/ComfyUI, and other Tools Suite modules are optional and unavailable until a compatible public package exists.

- [ ] **Step 3: Add the beginner persistence gate**

Require PostgreSQL health, absence of SQLite fallback, host backup, digest verification, restore-check database success, restart persistence, and local-only listeners before local setup is complete.

- [ ] **Step 4: Run documentation and deploy contract tests**

Run `rtk python -m unittest tests.test_customer_deploy_contract -v` and `rtk git diff --check -- deploy/QUICKSTART.md deploy/docker-compose.yml deploy/*.ps1`.

- [ ] **Step 5: Commit quickstart alignment**

```text
rtk git commit -m "docs(release): align quickstart with local setup contract"
```

### Task 6: Isolated archive proof without publication

**Files:**
- Modify only earlier task files if a scoped test exposes a defect.

**Interfaces:**
- Consumes: real docs build, current customer-release fixture inputs, cached PostgreSQL 16 image when available.
- Produces: local archive proof and explicit negative/partial evidence.

- [ ] **Step 1: Run all focused unit tests**

Run:

```text
rtk python -m unittest tests.test_package_customer_release tests.test_customer_deploy_contract -v
rtk python -m py_compile scripts/package_customer_release.py tests/e2e/customer_release_archive_e2e.py
rtk git diff --check -- Development/Backend/Servers/zig-server-v2
```

- [ ] **Step 2: Build into a new temporary directory**

Invoke the packager with `--documentation-dir` pointing to the real docs artifact and `--verify-extract`. Never write output inside the source tree and never overwrite an existing archive.

- [ ] **Step 3: Run the extracted-archive E2E when prerequisites exist**

Use only an already cached PostgreSQL 16 image; do not pull an image or stop an existing server. Record whether the proof used fixture binaries or current compiled binaries, and keep those proof layers separate.

- [ ] **Step 4: Inspect the archive contract**

Verify `docs/index.html`, docs manifest, backup helpers, release manifest linkage, and `SHA256SUMS.txt`. Open the docs from the extracted directory with network disabled.

- [ ] **Step 5: Report boundaries and leave publication untouched**

Report exact test counts, archive path, hashes, PostgreSQL mode, and any blocked gate. Do not edit `web_portal/src/data/releases.json`, upload the ZIP, tag Git, create a GitHub release, or call the result public.
