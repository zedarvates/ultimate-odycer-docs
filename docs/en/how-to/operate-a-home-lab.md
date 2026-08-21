# Operate a home-lab Ultimate Odycer stack

Use this guide to keep a private lab honest. It is not a production
deployment runbook, a load-balancer guide, or a public-internet checklist.

## 1. Stay inside the public boundary

- documentation and NPC capacity tools from this repository;
- experimental JSON templates from the public registry;
- documentation-only client starters;
- loopback inference and synthetic fixtures;
- no production endpoints, player data, or proprietary server copies.

## 2. Prefer loopback

Local LLM listeners should stay on loopback. A private-LAN listener needs
authentication, origin checks, firewall rules, and a rollback plan. Tutorials
do not authorize exposing a service.

## 3. Observe without claiming production

Useful local signals:

- NPC reply duration and queue policy from the capacity estimator;
- structured logs with synthetic names;
- fail-closed counts: rejected intents, replaced LLM output, timeouts.

Prometheus, Grafana, multi-server sharding, and backup of live worlds remain
unpublished. Do not paste real IPs, tokens, or logs into issues.

## 4. Scale only with evidence

| Stage | Allowed proof | Not proof |
|---|---|---|
| Home lab | docs validation, synthetic NPC metrics | CCU, VR comfort, production TLS |
| Isolated staging | named local fixtures, no player data | hosted multi-region failover |
| Production | unpublished | any page in this repository |

Continue with [choose hardware](choose-hardware.md) and
[measure NPC capacity](measure-npc-capacity.md).
