# Architecture Decision & Drift Guardrails

Purpose: prevent proposals, historical context and experiments from silently becoming project truth.

## Epistemic labels
Every architectural statement SHOULD be classed as one of:
- **ESTABLISHED** — existing verified boundary or explicit human decision.
- **HISTORICAL** — true about project origin/past intent; not automatically current scope.
- **DECIDED** — explicitly accepted direction; implementation may still be pending.
- **PROPOSED** — assistant/team idea awaiting validation.
- **EXPERIMENTAL** — bounded implementation/proof; not production architecture.
- **DEPRECATED/CORRECTED** — previous interpretation that must not guide new work.

## Corrections from 2026-09-30 discussion
1. **CORRECTED:** Obolune is not the JSON/template registry or its authority. GitHub/UltOd JSON Template Registry remain canonical. Obolune is studio/publisher/showcase/platform-facing experience.
2. **CORRECTED:** Historical Ultimate Odycer planetary-life/high-customization/MMORPG/science-mode context must not be generalized into Obolune or the multi-game creation core. Obolune supports multiple game styles/genres.
3. **CORRECTED:** Creator tooling/platform work is a cross-game Obolune/Odycer-ecosystem capability, not a redefinition of Ultimate Odycer's product identity.
4. **CORRECTED:** Do not invent a competing Flora Editor. Reuse/locate existing Plant Editor work before naming/creating a new editor.
5. **CORRECTED:** Do not recreate the existing World Compiler or mature JSON Template Registry. Extend through adapters/contracts only when justified.
6. **CORRECTED:** Botte Secrète is established as an execution/reliability/evidence layer. Capability routing/orchestration extensions are EXPERIMENTAL until separately proven; do not describe them as established production behavior.
7. **CORRECTED:** SYSTAI's expanded studio/creator orchestration role is a DECIDED direction in this discussion, but implementation remains staged/experimental. ChatGPT/Dots/local models are candidate providers/executors, not SYSTAI itself.
8. **CORRECTED:** OpenAI Dots/Work integrations must use official availability/permissions. No local adapter may emulate unavailable provider features to bypass restrictions.
9. **DECIDED:** Creator workflows are not AI-generation-first. Manual, local, cloud, subscription, collaborator and hybrid production are peers; human editable masters can be protected.
10. **DECIDED:** Human supervision remains intentional. Automation should maximize useful work between human decisions, not remove product/creative/business authority.

## Anti-drift rules
- Historical context never changes current scope without an explicit new decision.
- A proposed component does not become “existing” because a schema/issue was created.
- A draft PR proves only its bounded contents/tests, not adoption or production integration.
- Names do not establish identity: search existing projects/tools before creating a new named component.
- Cross-project abstractions require evidence from multiple domains before promotion.
- Genre-specific features belong in composable modules, not the genre-neutral core.
- Keep product identity, studio identity, creator platform, infrastructure and open-source registry as separate concepts.
- When user correction conflicts with assistant architecture, record the correction and update downstream docs rather than rationalizing the old proposal.
