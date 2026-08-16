# Choose NPC hardware on a limited budget

Use this guide to choose between an ESP32 board, a Raspberry Pi, and a mini PC.
The best purchase may be no purchase at all.

## 1. Define the dialogue level

| Need | Starting hardware |
|---|---|
| Sounds, growls, patterns, and a closed vocabulary | An ESP32 you already own |
| Short generated variations in a narrow domain | ESP32-S3 with PSRAM |
| A shared local 1–3B dialogue model | x86 mini PC with 16 GB RAM |
| Required GPIO, HAT, camera, or Linux sensors | Raspberry Pi 5 |

A microSD card adds storage, not RAM or compute throughput.

## 2. Compare complete cost

The following values are `estimated`, dated August 2026, and are not quotations:

| Option | Indicative complete cost | Main limit |
|---|---:|---|
| Existing classic ESP32 plus SD/audio | €5–15 extra | Not suitable for a multi-million-parameter LLM |
| ESP32-S3 N16R8 plus SD/audio | €15–40 | Very constrained model and vocabulary |
| Refurbished professional mini PC, 16/256 | €140–220 | Throughput must be measured per CPU and model |
| Complete Raspberry Pi 5 4 GB | €170–200 | Limited RAM and accessory cost |

Include power supply, cooling, storage, cables, warranty, and locally measured
electricity. A bare board is not a complete system.

## 3. Apply the purchase rule

Buy nothing when existing hardware already meets quality, latency, and throughput
requirements. Buy only after a benchmark shows a blocking gap.

For a home-lab mini PC, check for at least 16 GB RAM, a 256 GB SSD, documented
cooling, AVX2-capable CPU, a clear operating-system offer, identifiable warranty,
and network speed stated in Gb/s rather than ambiguous Wi-Fi wording.

## 4. Reject shortcuts

- A model fitting in RAM does not prove usable latency.
- “Dual network 2.5 GHz” does not prove two 2.5 Gb/s Ethernet ports.
- Stored profiles do not prove active conversation capacity.
- An ESP32-S3 demonstration does not prove classic ESP32 compatibility.

Measure the selected device with [Measure NPC capacity](measure-npc-capacity.md)
before publishing a supported-NPC number.
