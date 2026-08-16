# Run your first NPC capacity benchmark

This tutorial shows how to turn one reply duration into a scheduling capacity.
You do not need an Ultimate Odycer server or an LLM: the first run uses a
synthetic scenario.

## Expected outcome

You will produce JSON that distinguishes theoretical throughput, reserved
headroom, planned active NPCs, and actual inference streams.

## Prerequisites

- Python 3.11 or newer;
- a local copy of this repository;
- a terminal opened at the repository root.

## 1. Validate the documentation

In PowerShell:

```powershell
rtk python scripts/validate_docs.py
```

The command must finish with `validation: ok`.

## 2. Define the scenario

Use these assumptions:

- one short reply takes 1.7 seconds;
- one NPC speaks at most once every 120 seconds;
- one inference stream is available;
- the scheduler uses only 50% of theoretical capacity.

These values are `estimated`. Passing them to the calculator does not make them
`observed`.

## 3. Calculate capacity

```powershell
rtk python scripts/npc_capacity_estimator.py `
  --reply-seconds 1.7 `
  --npc-interval-seconds 120 `
  --utilization 0.5 `
  --streams 1 `
  --basis scenario
```

The result must include:

```json
{
  "basis": "scenario",
  "planned_replies_per_minute": 17.647,
  "supported_active_npcs": 35,
  "queue_policy": "serialize_per_stream"
}
```

This means 35 NPCs may request one short reply every two minutes in this
scenario. It does not mean that 35 models run in parallel.

## 4. Try your own gameplay rhythm

For a monster that growls at most every five minutes, replace
`--npc-interval-seconds 120` with `300`. For an NPC that takes a turn every
30 seconds, use `30`.

Keep `--basis scenario` until reply duration comes from a reproducible hardware
benchmark.

## 5. Check success

The tutorial is complete when the command returns valid JSON, `basis` is
`scenario`, streams match your actual assumption, and you can explain why
capacity falls when NPCs speak more often.

Continue with [Measure NPC capacity](../how-to/measure-npc-capacity.md) to replace
the scenario with observations.
