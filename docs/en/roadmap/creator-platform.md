# Ultimate Odycer Creator Platform — Roadmap Addendum

Status: architecture/planning. Extends existing Tools Suite and World Compiler; does not replace them.

## SYSTAI
SYSTAI is the creator-facing orchestrator: intent elicitation, unresolved questions, decisions, project state and delegation. ChatGPT/Dots/local LLMs are replaceable reasoning providers behind SYSTAI.

## Reuse before creation
Reuse the existing World Compiler; Creature, City, Architecture, Dungeon and Avatar editors; Asset/Audio Factory; StoryCore; AIMesher/FreeCAD; ComfyUI and external editors. Zig remains authoritative. Do not create a competing Flora Editor: locate and extend the existing Plant Editor work.

## Missing foundations
### CREATOR-01 Game DNA / Design Graph
Versioned requirements, decisions, constraints, dependencies, unknowns and rationale. Generate human wiki/GDD views from it.

### CREATOR-02 Universal Entity Contract
Canonical IDs/components for plants, creatures, items, buildings, factions, planets, etc. Extend existing template/Protobuf work first. Include provenance, gameplay semantics, simulation hooks and migrations.

### CREATOR-03 Editor & Tool Capability Registry
Capabilities, prerequisites, I/O, consequences, licence constraints and validation proof for internal/external tools. Selection is by capability/evidence, not name.

### CREATOR-04 Project Knowledge Graph
Links decisions -> entities -> assets -> code -> tests -> builds -> provenance and enables impact analysis.

### CREATOR-05 Constraint & Budget Engine
CPU/GPU/VRAM, network, tick, storage, geometry/texture/audio, AI cost/latency, target hardware, accessibility/platform budgets consumed by generators.

### CREATOR-06 Provenance / Rights Ledger
Source, author/generator, licence, transformations, tool/model version and publication eligibility for every asset/dataset.

### CREATOR-07 Simulation & Synthetic Playtest Lab
Headless/abstract personas for progression, economy, navigation, load and exploit testing.

### CREATOR-08 Build / Release Evidence Graph
Exact inputs, schemas, assets, tools/models, validations and compatibility targets per build; supports reproducibility, rollback and partial regeneration.

### CREATOR-09 Migration Engine
Versioned migrations for Game DNA, entities and compiled world data.

### CREATOR-10 SYSTAI Explainability UX
Show understood intent, assumptions, unresolved choices, planned consequences, estimated cost and proposed changes before consequential execution.

## Loop
Conversation -> SYSTAI -> Game DNA -> Knowledge Graph -> capability routing -> editors/services -> existing World Compiler/build -> validation -> synthetic playtest -> evidence -> approval -> release.

Generate -> validate -> simulate -> measure -> explain -> approve -> publish.
