# Ultimate Odycer — OpenAI Platform Roadmap

Status: planning / experimental. No production dependency is implied.

## Architectural rule
OpenAI is an acceleration and distribution layer, never an irreversible dependency. Every capability must have an explicit provider boundary and, where practical, a deterministic/local fallback.

## Target architecture
Creator/player -> SYSTAI -> Odycer Agent Gateway -> game services, creator services and commerce.\nChatGPT / Dots / local LLMs are replaceable reasoning providers behind SYSTAI.
The gateway routes work through Botte Secrète / Parcimonia according to cost, latency, confidence, privacy and consequence:
deterministic -> cache/kNN -> nano/micro-NN -> local LLM -> hosted model/agent.

## Workstreams
### OAI-01 Agent Gateway
Stable capability IDs, provider adapters, budgets, audit trail, consequence/evidence envelope and fallback policy.

### OAI-02 Event bridge
Prototype game/server events such as server.alert, world.event.started, guild.raid.created and npc.story_event. Keep transport implementation replaceable; do not couple world state to one vendor protocol.

### OAI-03 Web agent surface
Expose a bounded, permissioned tool surface for the Three.js/web client. Start read-only; mutation requires explicit capability scopes.

### OAI-04 ChatGPT integration
Prototype a minimal Ultimate Odycer app/plugin surface: character summary, inventory/build consultation, guild/server status and creator assistance. No gameplay-critical dependency.

### OAI-05 Game Master / World Director agent
Experimental high-level orchestration only. Fast NPC actions remain in ONE/NeuroCore/local tiers. Agent output is proposal/event intent, not direct authoritative world mutation.

### OAI-06 Identity
Evaluate Sign in with ChatGPT behind an identity abstraction. Ultimate Odycer account identity remains provider-neutral.

### OAI-07 Commerce
Create a provider-neutral catalogue for private servers, creator services and digital assets. Commerce adapters are optional; entitlements remain authoritative inside Odycer.

### OAI-08 Creator bridge
Connect StoryCore, Asset Factory, AIMesher and ComfyUI through bounded jobs with provenance, cost budgets and human approval for publication.

## Phases
P0 — contracts and threat model.
P1 — read-only event + web prototypes.
P2 — minimal ChatGPT surface.
P3 — Game Master shadow mode.
P4 — identity/commerce experiments.
P5 — marketplace/distribution only after platform terms and economics are validated.

## Non-goals
No replacement of Zig authority, no direct LLM writes to authoritative world state, no mandatory OpenAI login, no automatic purchase/publishing, no migration of cheap reflex NPC actions to expensive hosted agents.

## Creator Platform dependency
OpenAI adapters consume the Odycer-owned Creator Platform contracts in `creator-platform.md`; they must not create parallel project memory, entity schemas or editor taxonomies.
