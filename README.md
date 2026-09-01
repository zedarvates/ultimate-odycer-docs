# Ultimate Odycer Docs

Bilingual public documentation for the Ultimate Odycer ecosystem: server-authoritative architecture, client proof gates, NPC pipelines, JSON/content contracts, creative tooling and local deployment guidance.

**Repository status:** public documentation. This repository does not publish the proprietary canonical Zig server, production configuration, credentials, private assets/lore, or commercial implementation.

## Start here

### English
- [Ecosystem overview](docs/en/explanation/ecosystem-overview.md)
- [Client architecture and current proof state](docs/en/explanation/client-architecture.md)
- [Server architecture](docs/en/explanation/server-architecture.md)
- [Public network-intent contract](docs/en/reference/network-contract.md)
- [Documented server network contract — compatibility not validated](docs/en/reference/server-network-contract.md)
- [Engine/template/world matrix](docs/en/reference/engine-template-world-matrix.md)

### Français
- [Vue d'ensemble de l'écosystème](docs/fr/explanation/ecosystem-overview.md)
- [Architecture client et état actuel des preuves](docs/fr/explanation/client-architecture.md)
- [Architecture serveur](docs/fr/explanation/server-architecture.md)
- [Contrat public network-intent](docs/fr/reference/network-contract.md)
- [Contrat réseau serveur documenté — compatibilité non validée](docs/fr/reference/server-network-contract.md)
- [Matrice moteurs/templates/mondes](docs/fr/reference/engine-template-world-matrix.md)

### Coding agents / LLMs
Read [docs/llm/README.md](docs/llm/README.md) before implementation work. It defines the proof hierarchy and the mandatory network-document reading order.

## Current component status

- Canonical Zig server: **private/proprietary-commercial**; exact baseline must be captured before current client compatibility can be marked `PROVEN`.
- Three.js 2.5D client: presentation + fail-closed `NetworkClient` + validated synthetic transport fixture; proof level remains `SYNTHETIC_FIXTURE_ONLY`, not real Zig interoperability.
- Godot Classic: public shell plus transport-independent intent contract and abstract socket-free transport adapter on the P0 branch; target Godot 4.7.2 remains `NOT_PROVEN` until the executable receipt exists.
- Godot VR: same public intent/adapter foundation; historical network is `LEGACY_QUARANTINED`; Godot 4.7.2, OpenXR runtime, headset runtime and Zig interoperability are separate unproven gates.
- Unity: `LEGACY`, no longer an active Ultimate Odycer development target.
- FoveaCore and NetherCore: separate specialized starters; never inherit compatibility claims from another client.
- WebAdmin: private P0 corrective audit is fail-closed; sensitive mutations remain quarantined until exact Zig auth/RBAC/re-auth/transaction/audit evidence exists.
- Public server archive: `unavailable` unless the official release gate explicitly says otherwise.
- Lite editors: only their bounded public contracts/tests may be called executable; previews remain scaffolding/proxy where documented.

## Critical proof rule

A green test proves only what it actually exercised. Documentation, metadata, TypeScript/GDScript types, a synthetic fixture, an HTTP 2xx response, or a literal endpoint found in Zig source is **not** enough to claim production compatibility.

Current proof vocabulary includes `DECLARED`, `SCAFFOLD`, `PARTIAL`, `IMPLEMENTED`, `SYNTHETIC_FIXTURE_ONLY`, `LEGACY`, `BLOCKED`, `WAITING`, `PROVEN`, and `FAKE-GREEN`.

## Network clarification

The public `network-intent-v1` material is transport-independent documentation/fixture material. Separately, `server-network-contract.md` currently documents the game/login transport as raw binary TCP. That server description is **not a client compatibility certificate** and must be tied to an exact Zig revision before promotion.

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

See the bilingual documentation indexes for creative production, local setup, NPC capacity, hardware, maps and JSON content authoring.
