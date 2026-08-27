# NPC agent pipeline

Status: `decision` for the public local-first design; runtime wiring of a
production NPC stack remains unpublished. This page extends
[hybrid architecture](hybrid-architecture.md) without turning a home-lab
benchmark into a gameplay AI claim.

## Pipeline

```text
world event or player talk
        |
        v
server perception and rule check
        |  distance, faction, cooldowns, permissions, safety
        v
behaviour selector
        |  deterministic first: FSM, behaviour tree, cached reply,
        |  k-NN / micro-model, or a validated script
        v
optional bounded LLM expression
        |  pre-prompt: role, memory slice, style, token budget
        |  post-prompt: schema, banned actions, length, safety
        v
output validation
        |  accept, repair, or replace with deterministic fallback
        v
player presentation and optional ESP32 expression
```

The LLM never decides damage, rewards, inventory, movement, or access. It
expresses an already validated intent. Invalid output never becomes a game
action directly.

## Behaviour layers

| Layer | Role | Authority |
|---|---|---|
| Rules and perception | Can this NPC act, see, or speak? | server |
| FSM / behaviour tree | What kind of act is legal now? | server or server-validated data |
| Memory / RAG | Which notes may flavour the reply? | retrieved, then filtered |
| Local model (GGUF / ONNX / TensorRT) | How is the line phrased? | expression only |
| Cloud model | Same as local, with higher cost and privacy cost | expression only, optional |
| Cache | Reuse a validated reply for the same packet | never skips validation forever |
| Deterministic fallback | Keep the world alive when inference fails | required |

k-NN, micro-networks, and RAG are optional flavour. They do not outrank
server rules. A retrieved memory that requests gold, items, or access is
discarded.

## Local-first cost control

For a home lab:

- keep listeners on loopback unless a private-LAN design is explicit;
- share one local model across many NPCs instead of one process per NPC;
- budget tokens per packet: role, short memory, one intent, short output;
- cache identical expression packets;
- serialize inference streams and keep headroom, as in the NPC capacity
  guides;
- fail closed to a growl, gesture, or canned line when the model is slow.

Cloud models are optional overflow, not the default source of truth. They
inherit the same schema, bans, and validation. Cost, logs, and prompts must
stay free of player secrets.

## Memory and dialogue

NPC memory is a filtered slice, not a dump of the world database. A public
design SHOULD keep:

- identity and current activity;
- a short relationship summary;
- the last accepted player intent;
- no inventory, currency, or unpublished lore dump.

Dialogue is presentation. Quest flags, reputation changes, and item grants
stay in the [gameplay systems](../reference/gameplay-systems.md) owned by the
server.

## Related pages

- [Hybrid architecture](hybrid-architecture.md)
- [Measure NPC capacity](../how-to/measure-npc-capacity.md)
- [Operate a home lab](../how-to/operate-a-home-lab.md)
