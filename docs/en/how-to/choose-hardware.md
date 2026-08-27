# Choose NPC hardware on a limited budget

Use this guide to choose between an ESP32 board, a Raspberry Pi, a new N100 mini
PC, and a refurbished business PC. The best purchase may be no purchase at all.

## 1. Define the dialogue level

| Need | Starting hardware |
|---|---|
| Sounds, growls, patterns, and a closed vocabulary | An ESP32 you already own |
| Short generated variations in a narrow domain | ESP32-S3 with PSRAM |
| A shared local 1–3B model at low acquisition cost | Refurbished x86 business PC with at least 16 GB RAM |
| A small, new, quiet, low-power server | N100 mini PC after checking RAM and SSD |
| Required GPIO, HAT, camera, or Linux sensors | Raspberry Pi 5 |

A microSD card adds storage, not RAM or compute throughput.

## 2. Compare the pricing model and complete system

Exact prices age quickly and are intentionally omitted. Open the official
product page, then record the dated price of the actual seller listing as
`observed`.

| Option | Pricing model | Official starting point | Main limit |
|---|---|---|---|
| Existing classic ESP32 plus SD/audio | reuse plus one-time accessory purchase | [Espressif products](https://www.espressif.com/en/products/socs) | Not suitable for a multi-million-parameter LLM |
| ESP32-S3 N16R8 plus SD/audio | one-time hardware purchase | [ESP32-S3](https://www.espressif.com/en/products/socs/esp32-s3) | Very constrained model and vocabulary |
| Refurbished business Tiny/Micro/Mini or SFF PC | second-hand one-time purchase | Manufacturer support page for the exact service tag | Condition, CPU generation, firmware locks, and power adapter must be checked |
| New N100 mini PC | one-time system purchase | [Intel Processor N100](https://www.intel.com/content/www/us/en/products/sku/231803/intel-processor-n100-6m-cache-up-to-3-40-ghz/specifications.html) | RAM may be soldered; cooling and SSD vary by system vendor |
| Complete Raspberry Pi 5 | one-time board and accessory purchase | [Raspberry Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/) | Limited RAM and separate accessory costs |

Compare the complete system: power adapter, cooling, storage, cables, warranty,
upgrades, shipping, taxes, and locally measured electricity. A bare board is
not a complete system and an official processor page is not a seller quote.

## 3. Apply the purchase rule

Buy nothing when existing hardware already meets quality, latency, and throughput
requirements. Buy only after a benchmark shows a blocking gap.

For a home-lab mini PC or refurbished business PC, check for at least 16 GB RAM,
a 256 GB SSD, documented cooling, an AVX2-capable CPU, the included power
adapter, no BIOS or enterprise asset lock, a clear operating-system offer,
identifiable warranty, and network speed stated in Gb/s rather than ambiguous
Wi-Fi wording.

Common families include Lenovo ThinkCentre Tiny, Dell OptiPlex Micro, and HP
EliteDesk/ProDesk Mini. Larger SFF systems may cost less and be easier to cool or
expand. These are search families, not seller endorsements or performance proof.

Follow [Buy a refurbished business PC](buy-refurbished-business-pc.md) before
comparing a listing with a new N100 system.

## 4. Reject shortcuts

- A model fitting in RAM does not prove usable latency.
- “Dual network 2.5 GHz” does not prove two 2.5 Gb/s Ethernet ports.
- Stored profiles do not prove active conversation capacity.
- CPU TDP is neither whole-system wall power nor an LLM benchmark.
- “Refurbished” does not guarantee a fresh CMOS battery, a healthy SSD, or an
  unlocked BIOS.
- An ESP32-S3 demonstration does not prove classic ESP32 compatibility.

Measure the selected device with [Measure NPC capacity](measure-npc-capacity.md)
before publishing a supported-NPC number.
