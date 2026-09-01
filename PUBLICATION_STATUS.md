# Publication status

Status: **public documentation repository**.

This status applies only to `zedarvates/ultimate-odycer-docs`. It does not publish or license the proprietary canonical Zig server, hosted infrastructure, production configuration/data, private assets/lore, credentials, or commercial implementation.

## Current proof snapshot

- Documentation authority remains `documentation_only`.
- `docs/llm/current-proof-state.json` is the current machine-readable maturity overlay for agents.
- Three.js 2.5D: presentation + fail-closed `NetworkClient` + synthetic transport gate validated; proof remains `SYNTHETIC_FIXTURE_ONLY`; canonical Zig live = `NOT_PROVEN`.
- Godot Classic: project + public intent contract + abstract socket-free transport adapter exist on P0; Godot 4.7.2 executable receipt = `NOT_PROVEN`; Zig live = `NOT_PROVEN`.
- Godot VR: same foundation; historical networking = `LEGACY_QUARANTINED`; Godot 4.7.2, OpenXR runtime, headset runtime and Zig live are separate unproven gates.
- Unity: `LEGACY`, no longer an active development target.
- Private WebAdmin: corrective P0 audit is fail-closed; sensitive mutations remain quarantined pending exact Zig auth/RBAC/re-auth/idempotence/transaction/audit evidence.
- Canonical Zig server baseline: exact current SHA/tree/toolchain still must be captured by the P0 provenance gate before compatibility claims are promoted.

## Network documentation status

`network-intent-v1` is public synthetic, transport-independent documentation/fixture material.

`server-network-contract.md` currently describes implementation decisions including raw binary TCP and detailed message semantics. It is classified **decision-documented / compatibility-not-validated** until those claims are tied to an exact canonical Zig revision and reproducible evidence. It must not be treated as a client compatibility certificate.

A browser client must not assume a player WebSocket endpoint exists. Live Three.js interoperability requires a proven gateway/bridge or separately proven official endpoint.

## Validation snapshot

The repository validation covers, as applicable:

- bilingual structure and internal links;
- public-boundary checks;
- schemas/examples and deterministic tests;
- SHA-256 source manifest;
- fresh-copy/static-doc generation checks;
- documented license mapping and secret-scanning gates.

A green documentation workflow proves only those documentation/repository checks. It does **not** prove a production server, playable MMO client, Godot/OpenXR/headset runtime, Zig interoperability, PostgreSQL runtime behavior, Tools Suite production readiness, or hardware performance.

## Public release boundary

- Public server archive: `unavailable` unless an official release gate explicitly publishes one.
- Public client starters: evidence-tracked and incomplete; see the engine/template matrix and client proof files.
- Lite editors: only bounded public contracts/tests explicitly marked executable may be called `executable_public`; previews remain scaffolding/proxy where documented.
- Full Tools Suite, Asset Factory and optional creation modules remain individually classified; no blanket production-ready claim is implied.

## Licensing boundary

Documentation and scripts/schemas/examples follow their explicit repository licenses. Public client repositories retain their explicit public licenses.

The private server, proprietary gameplay, production configuration, private assets/lore and commercial components remain proprietary/commercial, **all rights reserved unless an explicit component license states otherwise**. Private repository access is not a license grant and does not authorize private → public copying.

Future publication changes must pass repository validation, manifest regeneration, boundary/license review, and any applicable secret/provenance checks before merge/publication.
