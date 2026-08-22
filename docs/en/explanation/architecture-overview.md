# Architecture overview

Status: `decision`. This page describes the public Ultimate Odycer architecture.
It is not a dump of the unpublished Zig server and does not certify a running
deployment.

## Authority model

```text
player intent
    |
    v
client presentation layer
    |  local prediction is optional and disposable
    |  never authoritative for HP, gold, inventory, speed, or access
    v
transport (TLS expected for any non-loopback path)
    v
authoritative server
    |  authenticates identity
    |  validates intent against rules, cooldowns, and world state
    |  applies consequences
    |  persists what must survive a reconnect
    v
state diff / presentation update
    v
interested clients, NPC expression nodes, and tools
```

The server remains authoritative for identity, movement, combat, inventory,
progression, and economy. That rule is already accepted in the public client
starter repositories. A client, JSON template, or LLM output that disagrees
with the server is rejected.

## Replication, zones, and shards

```text
                +------------------ realm / world ------------------+
                |                                                   |
   login / auth |   zone A          zone B          instance I      |
   and handoff  |  (interest set)  (interest set)  (bounded copy)   |
                |                                                   |
                +------------------ persistence --------------------+
```

Public rules:

- a player connects through authentication and a realm handoff, not by writing
  world state locally;
- a zone or interest set limits which entities a client may see or interact
  with;
- an instance is a bounded copy of content, not a second source of truth;
- sharding, if used, is a capacity decision. It does not move authority to the
  client;
- exact shard maps, interest radii, and instance budgets remain `unavailable`
  until a public protocol version is published.

## Pipelines

### Network pipeline

See the [network contract](../reference/network-contract.md). Intents travel
client to server. Authoritative diffs travel server to interested clients.
Retries and timeouts never replay an unvalidated mutation.

### NPC / LLM pipeline

See the [NPC agent pipeline](npc-agent-pipeline.md) and
[hybrid architecture](hybrid-architecture.md). The server validates intent
first. The model only expresses an already accepted packet.

### Client VR / rendering pipeline

See [client architecture](client-architecture.md). Scene loading, LOD, OpenXR
input, and local physics are presentation. Collision that grants loot, damage,
or movement speed is not.

### Asset / template pipeline

See [use JSON templates](../how-to/use-json-templates.md). Creators version
content in the public registry. Consumers pin a SHA-256. The server still
validates gameplay values.

## Home lab versus production

| Layer | Home lab | Self-hosted staging | Production |
|---|---|---|---|
| Audience | one operator, synthetic data | isolated operators, synthetic players | unpublished commercial boundary |
| Authority | still server-side | still server-side | still server-side |
| LLM | loopback, budgeted, fail-closed | same, plus rate limits | unpublished |
| Monitoring | local logs and NPC metrics | structured logs, capacity notes | unpublished |
| Proof | docs validation and local benchmarks | named fixtures, no production data | not claimed here |

A successful home-lab benchmark does not prove production CCU, VR comfort, or
multi-server failover. Those remain `unavailable` in this repository.

## Related pages

- [Ecosystem overview](ecosystem-overview.md)
- [Server architecture](server-architecture.md)
- [Client architecture](client-architecture.md)
- [NPC agent pipeline](npc-agent-pipeline.md)
- [Gameplay systems](../reference/gameplay-systems.md)
