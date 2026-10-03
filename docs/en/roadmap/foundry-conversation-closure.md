# Foundry Conversation & Work Closure

Status: DECIDED direction / EXPERIMENTAL implementation.

## Principle
Work completion and chat/UI archival are separate.

State machine:
ACTIVE -> LIKELY_FINISHED -> CLOSURE_CHECK -> ARCHIVE_READY -> ARCHIVED
A closed/archived item may become REOPENED.

Inactivity alone never implies completion.

## Closure requirements
Before ARCHIVE_READY:
- goal/work outcome is complete or intentionally terminated;
- evidence/checkpoint is captured;
- Closure Capsule exists;
- no unresolved human decision/conflict;
- no renewal/deferred/external/runner/provider/watch wait remains hidden in the conversation;
- every residual task is transferred to Work Graph/Kanban/renewal queue/watch;
- critical stale evidence is resolved or explicitly blocks closure.

## Closure Capsule
Stores goal, outcome, decisions, changes, evidence, costs, artifacts, learnings, canonical refs, transferred residual work and exact resume instructions.

## Retention
Support grace window, pinned/never-auto-archive and explicit retention reasons. Silence is only a weak signal.

## Three automation levels
1. **Auto-close** — Foundry may close its own Work Graph when eligibility is proven.
2. **Archive-ready** — conversation is safe to archive without losing work.
3. **Auto-archive UI** — only through an officially available adapter, explicitly enabled by the user and allowed by effective permissions.

No UI/browser emulation is used to bypass unavailable archive controls.

## Reopen
Rebuild context from Closure Capsule + current canonical sources/evidence; mark old assumptions/proofs stale where appropriate rather than treating archived context as current truth.
