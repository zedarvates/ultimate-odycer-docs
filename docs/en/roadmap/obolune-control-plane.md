# Obolune — Game & Template Control Plane

Status: roadmap. Obolune is a catalog/control plane, not the authority for runtime game data.

## Roles
- GitHub repositories: immutable/versioned source of truth for code, templates and documentation.
- UltOd JSON Template Registry: canonical declarative template/schema registry.
- Game repositories: project-specific source, assets and runtime adapters.
- Obolune: discovery, composition, lifecycle, compatibility/evidence views, documentation portal and SYSTAI entry point.

## Obolune objects
1. Game — identity, Game DNA, Story DNA, status, owners, targets and releases.
2. Game Project Manifest — exact dependency graph for a game build.
3. Template — projection of canonical registry entries, never a silent copy.
4. Game Starter/Template Pack — compatible pinned set of client/server/content contracts.
5. Tool/Editor — capability-registry projection.
6. Asset Pack — provenance/licence plus compatible entity/schema targets.
7. Build/Release — evidence graph, compatibility, artifacts and rollback refs.
8. Documentation — generated human/agent views from canonical contracts.
9. Migration — version-to-version upgrade path and validation requirements.

## Proposed UX
Explore -> describe game to SYSTAI -> select/derive Game DNA -> choose starter/template pack -> resolve exact versions -> create project lock -> generate wiki/docs -> scaffold adapters -> validate -> build/playtest -> publish release evidence.

## Registry rules
- Never claim compatibility from presence.
- Pin exact versions in manifests/lockfiles.
- Published strict templates stay immutable.
- Obolune caches/searches projections; canonical refs point back to registry/repositories.
- Deprecation never deletes historical versions.
- Every generated game records the exact template/tool/model versions used.

## Useful views
- Games library
- Template/schema explorer
- Starter game templates
- Compatibility matrix
- Dependency graph
- Migration center
- Editor/tool catalog
- Asset provenance/license center
- Build and release evidence
- SYSTAI creator workspace
- Public docs and machine-readable agent catalog

## Future commercial boundary
Marketplace/distribution can be added as an adapter. Entitlements, pricing and payment are separate from the technical registry so the ecosystem remains usable without one marketplace provider.
