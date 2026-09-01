# Ultimate Odycer Docs

Bilingual public documentation for the Ultimate Odycer ecosystem: server-authoritative architecture, client proof gates, NPC pipelines, JSON/content contracts, creative tooling and local deployment guidance.

**Repository status:** public documentation. This repository does not publish the proprietary canonical Zig server, production configuration, credentials, private assets/lore, or commercial implementation.

## Start here

### English
- [Ecosystem overview](docs/en/explanation/ecosystem-overview.md)
- [Client architecture and current proof state](docs/en/explanation/client-architecture.md)
- [Server architecture](docs/en/explanation/server-architecture.md)
- [Public network-intent contract](docs/en/reference/network-contract.md)
- [Unpinned server network snapshot — compatibility not validated](docs/en/reference/server-network-contract.md)
- [Engine/template/world matrix](docs/en/reference/engine-template-world-matrix.md)

### Français
- [Vue d'ensemble de l'écosystème](docs/fr/explanation/ecosystem-overview.md)
- [Architecture client et état actuel des preuves](docs/fr/explanation/client-architecture.md)
- [Architecture serveur](docs/fr/explanation/server-architecture.md)
- [Contrat public network-intent](docs/fr/reference/network-contract.md)
- [Snapshot réseau serveur non épinglé — compatibilité non validée](docs/fr/reference/server-network-contract.md)
- [Matrice moteurs/templates/mondes](docs/fr/reference/engine-template-world-matrix.md)

### Coding agents / LLMs
Read [docs/llm/README.md](docs/llm/README.md) and [docs/llm/current-proof-state.json](docs/llm/current-proof-state.json) before implementation work. They define proof hierarchy, current maturity and the mandatory network-document reading order.

## Current component status

- Canonical Zig server: **private/proprietary-commercial**; exact current SHA/tree/toolchain baseline must be captured before client compatibility can be marked `PROVEN`.
- Three.js 2.5D: presentation + fail-closed `NetworkClient` + genuinely executed synthetic transport fixture; proof remains `SYNTHETIC_FIXTURE_ONLY`, not real Zig interoperability.
- Godot Classic: public intent/abstract transport foundation plus deterministic socket-free synthetic fixture **PREPARED / CI-GUARDED**; runtime fixture and Godot 4.7.2 engine proof are still `NOT_YET_EXECUTED` / `NOT_PROVEN`.
- Godot VR: same prepared synthetic fixture with XR explicitly off; historical network `LEGACY_QUARANTINED`; Godot 4.7.2, synthetic runtime, OpenXR runtime, headset/controllers and Zig interoperability remain separate unproven gates.
- Unity: `LEGACY`, no longer an active Ultimate Odycer development target.
- FoveaCore and NetherCore: separate specialized starters; never inherit compatibility claims from another client.
- WebAdmin: private P0 corrective audit is fail-closed; sensitive mutations remain quarantined until exact Zig auth/RBAC/re-auth/transaction/audit evidence exists.
- Public server archive: `unavailable` unless the official release gate explicitly says otherwise.
- Lite editors: only their bounded public contracts/tests may be called executable; previews remain scaffolding/proxy where documented.

## Critical proof rule

A green test proves only what it actually exercised. In particular, a **CI structural gate is not a runtime Godot test**. Documentation, metadata, TypeScript/GDScript types, prepared fixture code, an HTTP 2xx response, or a literal endpoint found in source is not enough to claim production compatibility.

Useful distinctions:
- `PREPARED_CI_GUARDED`: implementation exists and static/structural guards pass, runtime not executed;
- `SYNTHETIC_FIXTURE_ONLY`: a controlled synthetic scenario actually executed successfully;
- `REAL_SERVER_E2E`: exact client/server revisions exercised together;
- `FAKE-GREEN`: evidence presented as stronger than what was actually tested.

## Network clarification

The public `network-intent-v1` material is transport-independent. Separately, `server-network-contract.md` is now explicitly an **unpinned implementation snapshot**, not a verified current protocol. A historical snapshot described raw binary TCP, but current transport details must be revalidated against the exact Zig baseline before use as canonical implementation evidence.

Therefore a browser client must not invent or assume a player WebSocket endpoint. A proven bridge/gateway or official endpoint is required for live browser interoperability.

## Licensing boundary

Documentation follows this repository's documented license. Scripts/schemas/examples retain their explicit licenses. Public client repositories retain their explicit public licenses.

The canonical private server, proprietary gameplay, production configuration, private assets/lore and commercial components remain proprietary/commercial, **all rights reserved unless an explicit component license states otherwise**. Access to a private repository is not permission to copy its implementation into a public repository.

## Public repositories

- `zedarvates/ultimate-odycer-docs`
- `zedarvates/ultimate-odycer-feedback`
- `zedarvates/ultod-json-template-registry`
- `zedarvates/ultod-client-godot-classic-3d-mmorpg-template`
- `zedarvates/ultod-client-godot-vr-mmorpg-template`
- `zedarvates/ultod-client-threejs-2-5d-mmorpg-template`
- `zedarvates/ultod-client-foveacore-fps-rpg-template`
- `zedarvates/ultod-client-threejs-nethercore-arpg-template`
