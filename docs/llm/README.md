# LLM documentation entry point

This directory helps documentation and coding assistants locate human-authored sources. It is not an agent prompt, API credential, authorization layer, or substitute for executable evidence.

## Rules for LLM/agent use

1. Select a document matching language, Diátaxis type, audience, and goal.
2. Preserve `observed`, `estimated`, `decision`, `declared`, `unavailable`, `blocked`, `legacy`, and proof-level labels.
3. Cite the source path and its limitations.
4. Read `PUBLICATION_STATUS.md`; never infer that a server, service, model, firmware, or commercial component is public.
5. Do not turn documentation into permission to mutate a device/server or publish material.
6. Never infer runtime compatibility from TypeScript/GDScript types, UI presence, a README claim, or a green synthetic test.
7. Treat `SYNTHETIC_FIXTURE_ONLY` as synthetic. It is never `REAL_SERVER_E2E`.
8. For Godot, keep engine load, OpenXR initialization, headset runtime, and Zig interoperability as **independent proof gates**.
9. For Three.js, do not invent a player WebSocket endpoint. The current server transport description says raw binary TCP; browser interoperability requires a proven bridge/gateway or official endpoint.
10. Treat `docs/*/reference/server-network-contract.md` as **decision-documented / compatibility-not-validated** until its claims are tied to an exact canonical Zig SHA/tree/toolchain baseline.
11. Before network work, read the target client's `NETWORK-PROOF-LEVELS`, compatibility manifest, and legacy quarantine (VR) where present.
12. Never copy private Zig implementation, production configuration, private assets/lore, or historical client networking into public MIT starters without file-level provenance/license review and explicit authorization.
13. Private Ultimate Odycer server/game code is proprietary/commercial, all rights reserved unless an explicit component license states otherwise. Public repositories retain their explicit public licenses.
14. Do not use a document's freshness/date as proof. Prefer executable receipts tied to exact revisions.
15. Do not reactivate WebAdmin mutations merely because an endpoint exists or returns HTTP 2xx; exact Zig auth/RBAC/re-auth/idempotence/transaction/audit evidence is required.
16. Ask the operator before an action requires credentials, external network exposure, deployment, firmware writing, deletion, purchase, or publication unless an existing explicit authorization covers that exact action.
17. Never ask the operator to reveal passwords, JWT secrets, private keys, database dumps, or player data.
18. Prefer free/open-source/local tools before cloud services and never upload confidential or unlicensed content to third parties.
19. Treat Kanboard as a visible human source of truth where the project uses it; routing automation must not silently rewrite human priorities.
20. When two documents conflict, prefer the one with the stronger named evidence and narrower scope; if neither has executable evidence, keep the state `UNVERIFIED` and surface the conflict instead of choosing the more convenient claim.

## Mandatory network reading order

For client/server work, read in this order:

1. `../en|fr/explanation/client-architecture.md`;
2. `../en|fr/reference/network-contract.md`;
3. `../en|fr/reference/server-network-contract.md` with its non-validated status preserved;
4. `../en|fr/reference/engine-template-world-matrix.md`;
5. the target repository's proof-level/compatibility files;
6. only then implementation code.

The canonical machine-readable documentation list is [context-index.json](context-index.json).
