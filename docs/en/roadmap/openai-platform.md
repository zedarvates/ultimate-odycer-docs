# OpenAI Platform Integration — Experimental Roadmap

Status: EXPERIMENTAL / planning. No production dependency or current provider availability is implied.

## Scope
Optional OpenAI-facing adapters for selected Obolune/Ultimate Odycer ecosystem use cases. This does not define the multi-game core and does not make OpenAI mandatory.

## Architectural rule
DECIDED: provider-specific integrations remain replaceable and may not become irreversible domain authority. Official provider availability, permissions and safety controls are respected.

## Target experiment
Creator/player -> SYSTAI project interface (staged) -> provider-neutral handoff/capability contracts -> specialized game/creator services.
ChatGPT, Work, future Dots where officially available, local models and other authorized executors are candidate providers/adapters.

Capability/cost routing through Botte Secrète/Parcimonia is EXPERIMENTAL, not established production behavior.

## Workstreams
OAI-01 provider-neutral gateway contracts; OAI-02 event bridge; OAI-03 bounded web agent surface; OAI-04 ChatGPT integration fixture; OAI-05 Game Master/World Director shadow experiment; OAI-06 optional identity experiment; OAI-07 optional commerce adapters; OAI-08 creator-service bridge.

## OAI-05 clarification
PROPOSED/EXPERIMENTAL: a high-level Game Master/World Director may be benchmarked for sparse planning/narrative coordination. This does not establish that ONE/NeuroCore currently owns all fast NPC actions, nor that the hosted-agent architecture is adopted.

## Non-goals
No replacement of domain authority; no direct LLM authoritative world writes; no mandatory OpenAI login; no automatic purchase/publishing; no bypass of unavailable provider features; no assumption that prototypes are integrated.
