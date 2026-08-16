# NPC metrics reference

The structured source is
[`schemas/npc-benchmark-v1.schema.json`](../../../schemas/npc-benchmark-v1.schema.json).

## Information status

| Value | Meaning |
|---|---|
| `observed` | Actually measured in the described environment |
| `estimated` | Calculated scenario with explicit assumptions |
| `decision` | Project choice kept separate from supporting data |
| `unavailable` | Unknown or unmeasured value |

## Required groups

| Group | Content |
|---|---|
| `hardware` | Device, CPU, useful RAM, storage, and cooling |
| `software` | Tool, version, model, quantization, and runtime |
| `workload` | Context, output, audio, streams, and NPC cadence |
| `measurements` | Samples, median, p95, throughput, and errors |
| `capacity` | Headroom, replies/minute, active NPCs, and queue policy |
| `limitations` | Claims not established by the result |

## Rules

- `supported_active_npcs` is a scheduling calculation.
- `streams` is the number actually tested, not the NPC count.
- `sample_count` must be present for an `observed` result.
- Missing metrics use `unavailable` where the schema permits it.
- Durations use seconds and sizes use bytes.
- Date and version must distinguish benchmark campaigns.
- Free-text fields must not contain secrets or client data.

Consumers must reject unknown schema versions. Extensions must not change the
meaning of existing fields.
