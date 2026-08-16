# Measure home-lab NPC capacity

Use this guide to turn a real benchmark into a conservative scheduling capacity.

## 1. Freeze the workload

Record hardware, RAM, cooling, operating system, model, quantization, runtime,
context length, maximum output, whether STT and TTS are included, concurrent
streams, and a reproducible prompt or seed.

Do not compare devices under different workloads.

## 2. Measure end-to-end duration

Run at least 100 short replies after warm-up. Keep every duration and calculate
the median and p95. Include audio preparation when it is part of the player
experience.

Use p95 as `reply-seconds` for conservative planning. If p95 is missing, mark it
`unavailable`; do not silently replace it with an average or zero.

## 3. Calculate capacity

Use only the number of streams that the benchmark actually exercised:

```powershell
rtk python scripts/npc_capacity_estimator.py `
  --reply-seconds <end-to-end-p95> `
  --npc-interval-seconds <minimum-interval-per-NPC> `
  --utilization 0.5 `
  --streams <proven-streams> `
  --basis measured
```

```text
planned replies/minute = streams × 60 / duration × utilization
active NPCs = planned replies/minute × NPC interval / 60
```

## 4. Record the result

Store data in a document matching
[`npc-benchmark-v1.schema.json`](../../../schemas/npc-benchmark-v1.schema.json).
Use [`estimated-esp32-s3.json`](../../../examples/benchmark-results/estimated-esp32-s3.json)
as a structural example, not hardware evidence.

## 5. Validate the decision

Accept a device only when p95 meets the experience limit, quality passes
predefined checks, deterministic fallbacks and errors are counted, capacity keeps
headroom, and complete cost beats keeping existing hardware.

Throughput alone does not prove dialogue quality, security, or production-server
capacity.
