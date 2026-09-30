# Cross-Project Intelligence Platform

Status: architecture / bounded experiments.

## Goal
Make each project improve the others through small shared contracts, without merging projects into a monolith.

## Common control plane
Human -> SYSTAI -> project DNA/state -> Botte Secrète capability/evidence routing -> Parcimonia compute/cost routing -> specialized project/tool -> validation/evidence.

## XP-01 Capability Graph
Extend Botte Secrète capability metadata so skills, CLI, MCP, workflows and agents expose prerequisites, exclusions, cost/latency class, likely consequences and evidence.

## XP-02 Story DNA
StoryCore owns a versioned narrative graph: characters, places, chronology, relationships, motivations, secrets, arcs and events. Export adapters may target comics/video/games, but Story DNA remains media-neutral.

## XP-03 Universal Asset Foundry
Coordinate Asset Factory, Bellium-AI, AIMesher/FreeCAD, ComfyUI and external editors through canonical asset jobs: concept -> geometry/media -> optimization -> metadata -> provenance -> validation -> target exports.

## XP-04 Physical Intelligence
Shared perception/state/prediction/action/evidence contracts for Nomad Farmbot and robotic-workbench experiments. ShardJEPA is an experimental representation/prediction component, not an assumed controller. VR teleoperation demonstrations are recorded as evidence-bearing datasets.

## XP-05 Living Digital Shadow
Aquaponics is the first living-system pilot: fish/water/plants/weather/energy/pumps/feeding/growth represented as observed state, predictions, recommendations and bounded actions. No autonomous physical actuation is implied.

## XP-06 ShadowGraph experiment
Do NOT build a universal framework yet. Test a minimal shared envelope across three deliberately different pilots:
1. Ultimate Odycer entity/NPC/world object
2. aquaponics entity/system
3. Nomad Farmbot entity/action

Candidate primitives:
- entity_id / type / schema_version
- observed_state + timestamp
- desired/constraint state
- event/history refs
- available capabilities/actions
- provenance/source
- confidence/uncertainty
- consequence class
- evidence refs
- prediction refs
- parent/relationship refs
- migration/version refs

Promote a primitive to the shared contract only if at least two pilots need it and the third can represent it without distortion.

## XP-07 SYSTAI federation
SYSTAI presents one human interface but loads project-specific DNA, permissions, terminology and tools. It must not collapse project memories or permissions into one unrestricted context.

## Safety / architecture invariants
- Domain authority stays in the domain system (Zig for authoritative game state; physical controllers for machines).
- External models propose through capabilities.
- High-consequence mutations require explicit policy/approval.
- Provenance and evidence travel with generated artifacts/actions.
- Shared contracts evolve through versioned migrations.
