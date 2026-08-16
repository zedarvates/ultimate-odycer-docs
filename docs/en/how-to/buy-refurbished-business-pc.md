# Buy a refurbished business PC for NPC workloads

Use this guide to evaluate a Lenovo ThinkCentre Tiny, Dell OptiPlex Micro, HP
EliteDesk/ProDesk Mini, or an equivalent SFF listing. The goal is a repairable
local LLM host without turning a bargain into an expensive series of upgrades.

## 1. Choose the form factor

| Form factor | Strength | Check before purchase |
|---|---|---|
| Tiny/Micro/Mini, roughly one litre | Compact, documented business parts | Proprietary power adapter and tight cooling |
| SFF | RAM, storage, and cooling are often easier to access | Larger; measure wall power |

Product families are search examples, not seller endorsements. Check the exact
model specification and machine type.

## 2. Set a minimum configuration

- at least 16 GB RAM; use 32 GB when the model, context, STT/TTS, and other
  services must coexist;
- at least a 256 GB SSD, preferably NVMe, with inspectable SMART health;
- an AVX2-capable CPU; six physical cores are a practical used CPU target, not
  a throughput guarantee;
- Gigabit Ethernet, included power adapter, and working cooling;
- at least one upgradeable RAM or storage slot where possible.

The Core i5-8500T found in systems such as the OptiPlex 7060 Micro and
ThinkCentre M720 Tiny has six cores and six threads. Its stated 35 W TDP is not
whole-system wall consumption. The N100 has four cores and four threads with a
stated 6 W processor base power. These official specifications describe the
processors; they do not prove which system runs your LLM workload faster.

## 3. Calculate complete cost

Add:

```text
listing price
+ required RAM
+ required SSD
+ missing power adapter
+ additional Wi-Fi or networking
+ delivery and possible return costs
+ electricity measured over the intended period
```

Record the actual listing price as `observed`, additions as `estimated`, and the
final choice as a decision. Do not treat a general range as evidence of the
price available in your region.

## 4. Inspect within the return period

1. Open the BIOS and check for an administrator password or enterprise asset
   lock.
2. Confirm the received CPU, RAM amount and module count, and SSD.
3. Inspect SMART health, then run a memory test.
4. Load the CPU for 20 to 30 minutes and record temperature, noise, throttling,
   errors, and wall power.
5. Test Ethernet, USB, display outputs, reboot, and recovery after power loss.
6. If keeping Windows, verify a supported release and the machine's actual
   eligibility. Windows 10 has been out of support since October 14, 2025,
   outside an extended security update arrangement.

Erase the previous storage and reinstall from a known source before adding home
lab data or credentials.

## 5. Choose between refurbished, N100, and Raspberry Pi

Prefer the refurbished business PC when its complete 16/256 or 32/512
configuration, power adapter, and return policy cost less than an N100 upgraded
to the same level, and its size and measured power are acceptable. Prefer the
N100 for a new, quiet, low-power system when RAM and storage will not block
future use. Prefer Raspberry Pi when GPIO, HAT, or sensor integration is the
main requirement.

In every case, supported NPC capacity remains `unavailable` before a
reproducible benchmark. Continue with [Measure NPC capacity](measure-npc-capacity.md).

## Technical sources

- [Dell OptiPlex 7060 Micro — supported processors](https://www.dell.com/support/manuals/en-us/optiplex-7060-micro/opti_7060_mff_setup_specs_manual/processor?guid=guid-e178c653-4f96-4d67-8c6e-0d7e87454d21&lang=en-us)
- [Lenovo ThinkCentre M720 Tiny — PSREF specifications](https://psref.lenovo.com/syspool/Sys/PDF/ThinkCentre/ThinkCentre_M720_Tiny/ThinkCentre_M720_Tiny_Spec.html)
- [Intel — official N-series processor presentation](https://download.intel.com/newsroom/2023/client-computing/Intel-N-series-Processors-Media_Presentation.pdf)
- [Microsoft — Windows 10 end of support](https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/windows-10-support-has-ended-on-october-14-2025)

Sources accessed August 16, 2026. Recheck prices, stock, and warranties at
purchase time.
