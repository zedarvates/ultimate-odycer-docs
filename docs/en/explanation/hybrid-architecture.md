# Why server, LLM, and ESP32 roles stay separate

An affordable home lab works best when every device receives a task that matches
its limits.

```text
game event
    ↓
authoritative server ── validates intent, rules, and consequences
    ↓
bounded expression packet ── emotion, intensity, archetype, seed
    ↓
shared x86 PC or ESP32 ── produces short text, variation, or sound
    ↓
output validation ── accepts or replaces with a deterministic pattern
    ↓
player presentation
```

## The server retains authority

The LLM does not decide damage, rewards, inventory, movement, or access rights.
It expresses an already validated intent. Invalid output never becomes a game
action directly.

## ESP32 is an expression node

A classic ESP32 suits patterns, growls, sounds, and tiny classifiers. An
ESP32-S3 with PSRAM can explore a tightly closed generative vocabulary. microSD
stores sounds and profiles but does not replace RAM.

## An x86 PC shares dialogue

A new N100 mini PC, a refurbished business Tiny/Micro/Mini PC, or a 16 GB x86
SFF system can host one local model shared by multiple NPCs. Refurbished systems
often offer more upgradeable RAM and CPU for the acquisition cost; N100 systems
may favour low power, silence, and a new warranty. These tendencies do not
replace complete-cost comparison or a benchmark of the actual configuration.
Identities and histories stay separate while generations use a common queue.
One computer per NPC would cost more without solving simultaneous conversation
pressure.

## Deterministic fallback protects the experience

Every important intent has a safe non-LLM response. The player still gets a
reaction when inference is slow, unavailable, or rejected. This separation lets
hobbyists experiment with low-cost hardware without assigning responsibilities
that the model cannot guarantee.
