# NeuroCore for NPCs and creatures — experimental track

Status: **research / non-authoritative / no automatic promotion**.

## Intent

Explore a very small persistent spiking-inspired decision layer for high-frequency NPC and creature decisions: vigilance, pursuit, evade, flee, regroup, local attack and investigation.

The goal is not to replace LLMs everywhere. Expensive models remain reserved for dialogue, social reasoning, long-horizon planning, unusual-event interpretation and open-ended knowledge tasks.

## Target architecture

```text
game signals
    ↓
NeuroCore reflex layer
    ↓
candidate action
    ↓
server-authoritative validation
    ↓
combat / movement / animation

low confidence or complex event
    ↓
cognitive router
    ├─ small model
    └─ LLM/VLM
```

NeuroCore receives no direct authority over economy, inventory, damage, rewards, quest rules or canonical world state.

## Candidate internal state

Compact slow variables specific to the creature type: fear, pain, hunger, aggression, curiosity, pack cohesion, threat memory and optionally fatigue.

Later experiments may use some of these variables as neuromodulator-like signals analogous to dopamine, serotonin or octopamine, but only after the simpler core has been benchmarked.

## Experimental ladder

1. **F0 — deterministic SNN scaffold**: leaky neurons, thresholds, refractory period and slow state.
2. **F1 — sparsity / compression**: sparse graph, fixed-point, INT8/INT16 and connection ablations.
3. **F2 — open biological motifs**: import only selected subcircuits from open connectomes with verified provenance and licensing.
4. **F3 — chemical typing**: neurotransmitters represented as typed effects rather than only excitatory/inhibitory signs.
5. **F4 — neuromodulation / plasticity**: bounded slow signals and local adaptation.
6. **F5 — distillation**: reduce useful motifs into minimal game-specific controllers.

Every step must be compared with its predecessor. No biological mechanism is retained merely because it is biologically plausible.

## Required benchmark

Compare at minimum:

- deterministic logic / Behaviour Tree;
- floating NeuroCore;
- quantized NeuroCore;
- small dense NN where relevant;
- escalation to a small model/LLM for complex cases.

Loads: 1, 100, 1,000 and 10,000 simulated agents.

Metrics: CPU/GPU time, memory, decisions/s, quantization divergence, acceptable-action rate, dangerous false positives, behavioral diversity, escalation rate and temporal stability.

## Promotion gate

A version cannot reach a Godot/Three.js client or the server until exact-head tests are reproducible, a measurable benefit exists for a target workload, authoritative boundaries remain intact and a deterministic fallback is available.

The first executable prototype is tracked in `ultimate-odycer-tools-suite`, experimental PR #25.
