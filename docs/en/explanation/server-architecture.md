# Server architecture

Status: `decision` for public boundaries; implementation details are
`unavailable` because the canonical Zig server is not published.

Independent developers can still design against the public contract. They
cannot clone a production server from this page.

## Public boundary

The server is the only source of truth for:

- account, character, and session identity;
- movement, combat, inventory, crafting, and economy;
- zone membership, instance membership, and visibility;
- NPC decisions that change world state;
- persistence and reconnect recovery.

The public client starters already record this as an accepted architecture
decision. A documentation page cannot weaken it.

## Logical modules

```text
                +------------- authoritative server --------------+
auth / session | identity, tokens, realm handoff                 |
world          | zones, instances, interest, replication         |
simulation     | movement, combat, inventory, crafting, quests   |
npc            | perception, behaviour, validated expression     |
persistence    | characters, world, economy, audit               |
safety         | validation, rate limits, anti-cheat, TLS        |
                +------------------------------------------------+
```

These names are logical. They are not a published crate list, binary layout,
or API surface. Module names from private repositories must not be copied
here as if they were a public SDK.

## What a future public protocol must expose

Before a third-party client can connect, a published contract must name:

- protocol version and negotiation;
- authentication and realm-handoff sequence;
- message identifiers, framing, and serialization;
- authoritative rules for identity, movement, combat, and inventory;
- transport security and certificate expectations;
- a synthetic loopback fixture with no production endpoint.

That evidence is currently blocked in the public client repositories. Until
it exists, treat server compatibility as unsupported.

## Operations that remain unpublished

The following are required for a real MMO, but they are not documented as a
public runbook in this repository:

- multi-server deployment and load balancing;
- shard assignment and failover;
- production TLS, secrets, and certificate rotation;
- Prometheus, Grafana, or any named hosted stack;
- backup and restore of production data;
- CI/CD for a live world.

A home-lab operator can still keep local logs, NPC metrics, and fail-closed
loopback services. See [operate a home lab](../how-to/operate-a-home-lab.md).

## Related pages

- [Architecture overview](architecture-overview.md)
- [Network contract](../reference/network-contract.md)
- [NPC agent pipeline](npc-agent-pipeline.md)
