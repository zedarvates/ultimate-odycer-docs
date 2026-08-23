# Local Setup Web Publication Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish the exact validated offline documentation bundle under the Ultimate Odycer Web site without maintaining a second HTML copy.

**Architecture:** The portal does not render a separate version of the guide. Its static Hostinger export consumes a previously validated `ultimate-odycer.docs-build.v1` directory, copies it byte-for-byte to `docs/local-setup/`, and records the documentation manifest digest in the portal export manifest.

**Tech Stack:** Astro 7, Node.js 24, TypeScript 6, Vitest 4, Node standard library

**Spec:** `artifacts/github-prep/ultimate-odycer-docs/docs/superpowers/specs/2026-08-23-local-setup-documentation-design.md`

## Global Constraints

- The docs Markdown repository remains the only authored source.
- The portal copies only a validated `ultimate-odycer.docs-build.v1` artifact.
- No deploy, upload, Hostinger mutation, DNS change, or live-site publication is authorized by this plan.
- Existing uncommitted portal changes belong to concurrent work. Before each edit, inspect the scoped diff and preserve it; never reset, stash, rebase, clean, bulk-stage, or reformat.
- `web_portal/src/pages/releases/index.astro`, `web_portal/scripts/export-hostinger-static.mjs`, and related tests already contain uncommitted work. Execution must patch the current content rather than replace it.
- External runtime assets are forbidden in the imported documentation tree.
- An absent, malformed, symlinked, path-traversing, or checksum-invalid docs artifact fails the publication build closed.
- All shell commands run with the `rtk` prefix.

---

## File Structure

- `web_portal/scripts/public-docs-bundle.mjs`: validate and copy the docs artifact.
- `web_portal/tests/public-docs-bundle.test.mjs`: path, schema, hash, and copy tests.
- `web_portal/scripts/export-hostinger-static.mjs`: invoke docs copy during static export.
- `web_portal/scripts/verify-hostinger-static.mjs`: verify exported docs and manifest linkage.
- `web_portal/src/pages/wiki/index.astro`: link the local-setup guide.
- `web_portal/tests/hostinger-static-contract.test.mjs`: require the published docs entry.
- `web_portal/package.json`: focused verification script.

### Task 0: Concurrent-work ownership gate

**Files:**
- Inspect only: every file named by Tasks 1-4.

**Interfaces:**
- Consumes: scoped Git status and diff for `web_portal/`.
- Produces: a safe go/no-go decision before any portal edit.

- [ ] **Step 1: Inspect exact portal paths**

Run `rtk git status --short -- web_portal` and scoped diffs for every existing file named below.

- [ ] **Step 2: Enforce the ownership gate**

If an existing target is staged, untracked, `MM`, or otherwise contains concurrent work, do not edit or commit it until its owner has committed it or the user explicitly authorizes inclusion of the complete existing file. New non-overlapping files may be prepared, but Tasks 2-4 remain blocked. Record the exact status lines as evidence.

- [ ] **Step 3: Continue only on a stable baseline**

Re-run the scoped status. Continue when every existing target is clean or when the current commit already contains the baseline implementation being extended.

### Task 1: Fail-closed docs bundle importer

**Files:**
- Create: `web_portal/scripts/public-docs-bundle.mjs`
- Create: `web_portal/tests/public-docs-bundle.test.mjs`

**Interfaces:**
- Consumes: directory with `docs-build-manifest.json` schema `ultimate-odycer.docs-build.v1`.
- Produces: `copyPublicDocsBundle({ sourceDir, targetDir }) -> Promise<{ manifestSha256, fileCount, documentationVersion, serverCompatibility }>`.

- [ ] **Step 1: Write failing importer tests**

Test a valid fixture and rejection of: missing manifest, wrong schema, missing `index.html`, unknown file, digest mismatch, symlink, source equal to target, and target outside its allowed output root.

```javascript
const result = await copyPublicDocsBundle({ sourceDir, targetDir, allowedOutputRoot });
expect(result.fileCount).toBe(3);
expect(result.serverCompatibility).toBe('unavailable');
expect(await readFile(join(targetDir, 'index.html'), 'utf8')).toContain('<!doctype html>');
```

- [ ] **Step 2: Run the focused test**

Run: `rtk npm test -- tests/public-docs-bundle.test.mjs`  
Expected: module-not-found failure.

- [ ] **Step 3: Implement manifest verification and bounded copy**

Use `realpath`, `lstat`, `relative`, and SHA-256. Require the actual file set to equal `Object.keys(manifest.files) + docs-build-manifest.json`; refuse symlinks and any normalized path containing `..`; copy to a newly created target only after all input hashes pass.

- [ ] **Step 4: Run the focused test**

Run: `rtk npm test -- tests/public-docs-bundle.test.mjs`  
Expected: all importer cases pass.

- [ ] **Step 5: Commit the importer**

```text
rtk git add web_portal/scripts/public-docs-bundle.mjs web_portal/tests/public-docs-bundle.test.mjs
rtk git commit -m "feat(portal): validate public docs bundles"
```

### Task 2: Static Hostinger export integration

**Files:**
- Modify: `web_portal/scripts/export-hostinger-static.mjs`
- Modify: `web_portal/scripts/verify-hostinger-static.mjs`
- Modify: `web_portal/tests/hostinger-static-contract.test.mjs`
- Modify: `web_portal/package.json`

**Interfaces:**
- Consumes: `ULTOD_PUBLIC_DOCS_DIR` pointing to a validated build from the docs repository.
- Produces: `dist-hostinger-static/docs/local-setup/index.html` and portal manifest `publicDocumentation` metadata.

- [ ] **Step 1: Add failing export-contract assertions**

Assert that `package.json` exposes `verify:public-docs`, the exporter reads `ULTOD_PUBLIC_DOCS_DIR`, and the Hostinger manifest includes:

```json
{
  "publicDocumentation": {
    "path": "docs/local-setup/index.html",
    "manifestSha256": "<64 lowercase hex>",
    "documentationVersion": "docs-2026.08",
    "serverCompatibility": "unavailable"
  }
}
```

- [ ] **Step 2: Run the contract test and observe failure**

Run: `rtk npm test -- tests/hostinger-static-contract.test.mjs`.

- [ ] **Step 3: Patch the exporter without replacing concurrent work**

After the normal portal routes and public client assets are written, resolve `ULTOD_PUBLIC_DOCS_DIR`, validate/copy it into `dist-hostinger-static/docs/local-setup`, hash its build manifest, and add the returned metadata to `hostinger-static-manifest.json`. Treat a missing environment variable as a build error for `build:hostinger-static`; ordinary `npm run build` remains unaffected.

- [ ] **Step 4: Extend static verification**

Require the docs entry, all docs manifest hashes, no symlinks, and no remote runtime asset references. Verify the portal manifest digest equals the copied docs manifest digest.

- [ ] **Step 5: Build against the actual docs artifact**

Set `ULTOD_PUBLIC_DOCS_DIR` to the absolute `build/local-setup-html` directory produced by the documentation plan, then run:

```text
rtk npm run build:hostinger-static
rtk npm run verify:hostinger-static
```

Expected: static export passes locally and contains the byte-identical docs tree. This is not a deployment proof.

- [ ] **Step 6: Commit only the scoped integration files**

```text
rtk git commit -m "feat(portal): include versioned local setup docs"
```

### Task 3: Discoverability from the Wiki and releases page

**Files:**
- Modify: `web_portal/src/pages/wiki/index.astro`
- Modify: `web_portal/src/pages/releases/index.astro`
- Modify: `web_portal/tests/basic.test.ts`
- Modify: `web_portal/tests/public-copy-integrity.test.ts`

**Interfaces:**
- Consumes: public URL `/docs/local-setup/index.html` and current empty `releases.json` contract.
- Produces: honest entry links without claiming a downloadable server.

- [ ] **Step 1: Add failing page-source assertions**

Assert the Wiki links to `/docs/local-setup/index.html`, labels it as a beginner local journey, and the empty releases branch links to the guide while retaining `No public release yet`.

- [ ] **Step 2: Patch the current pages surgically**

Add one Wiki card and one link in the empty release state. Preserve all current branding, release-source comments, and concurrent edits. Do not add a fake version, hash, download button, or compatibility claim.

- [ ] **Step 3: Run portal checks**

Run:

```text
rtk npm test -- tests/basic.test.ts tests/public-copy-integrity.test.ts
rtk npm run lint
rtk npm run build
```

Expected: all commands pass without contacting a production API.

- [ ] **Step 4: Commit the entry links**

```text
rtk git commit -m "docs(portal): link local setup journey"
```

### Task 4: Final local publication proof

**Files:**
- No source files beyond earlier tasks.

**Interfaces:**
- Consumes: clean docs artifact plus current portal tree.
- Produces: local Hostinger export evidence only.

- [ ] **Step 1: Run scoped diff checks**

Run `rtk git diff --check -- web_portal` and inspect `rtk git status --short -- web_portal`. Verify no unrelated path is staged.

- [ ] **Step 2: Run the portal test suite and static verifier**

Run `rtk npm test`, `rtk npm run lint`, `rtk npm run build:hostinger-static`, and `rtk npm run verify:hostinger-static` with the docs artifact environment variable set.

- [ ] **Step 3: Inspect the generated artifact**

Open `dist-hostinger-static/docs/local-setup/index.html` locally, navigate French and English pages, disconnect network access, and verify text, styles, images, and internal links remain usable.

- [ ] **Step 4: Record proof boundaries**

Report the local artifact path, docs manifest digest, portal manifest digest, and exact command results. State explicitly that no Hostinger upload or live-site verification occurred.
