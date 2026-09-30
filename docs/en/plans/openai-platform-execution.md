# OpenAI Platform — Execution Plan

Start: 2026-10-01

## Week 1 — foundations
- Define Agent Gateway capability envelope: id, input/output schema, auth scope, cost ceiling, latency class, consequence, evidence, fallback.
- Inventory existing Zig/Tools/Web/NeuroCore interfaces.
- Draft event vocabulary and read-only permissions.
- Add provider-neutral feature flags.
- Define telemetry: provider, tokens/compute, latency, cache hit, fallback, confidence, outcome.

Exit proof: schemas + examples validate without runtime claims.

## Week 2 — bounded prototypes
- Event bridge: replay synthetic server/world events.
- Three.js: read-only agent tools for status/navigation metadata.
- ChatGPT integration mock: character/server queries using fixtures.
- Parcimonia routing benchmark: deterministic/kNN/micro/local/hosted decision tiers.

Exit proof: offline tests and cost/latency report.

## Week 3 — NeuroCore experiment
- Add Game Master/World Director shadow adapter.
- Feed events and world summaries, receive typed proposals.
- Never mutate authoritative state.
- Compare hosted proposal quality/cost against local baseline.
- Record consequences, abstentions and fallbacks.

Exit proof: reproducible shadow benchmark.

## Later gates
Identity, commerce and marketplace work starts only after public APIs/terms are sufficiently stable and security/privacy review passes.

## Kanban order
READY: OAI-01 gateway contracts; OAI-02 event vocabulary.
NEXT: OAI-03 read-only web tools; OAI-04 ChatGPT fixture prototype.
EXPERIMENT: OAI-05 Game Master shadow.
WATCH: OAI-06 identity; OAI-07 commerce/marketplace.
