# Ultimate Odycer Home Lab Docs

Documentation bilingue, locale d'abord, destinée aux développeurs indépendants,
makers et hobbyistes qui construisent un home lab avec un budget limité.

Bilingual, local-first documentation for independent developers, makers, and
home-lab hobbyists working with limited budgets.

**Statut / Status:** local publication candidate, not published.

## Français

Commencez par le [tutoriel du premier banc PNJ](docs/fr/tutorials/first-npc-benchmark.md).

- Tutoriel : [réaliser un premier banc PNJ](docs/fr/tutorials/first-npc-benchmark.md)
- Guide : [choisir le matériel](docs/fr/how-to/choose-hardware.md)
- Guide : [mesurer la capacité PNJ](docs/fr/how-to/measure-npc-capacity.md)
- Référence : [schéma des métriques](docs/fr/reference/metrics-schema.md)
- Explication : [architecture hybride](docs/fr/explanation/hybrid-architecture.md)

## English

Start with the [first NPC benchmark tutorial](docs/en/tutorials/first-npc-benchmark.md).

- Tutorial: [run your first NPC benchmark](docs/en/tutorials/first-npc-benchmark.md)
- How-to: [choose hardware](docs/en/how-to/choose-hardware.md)
- How-to: [measure NPC capacity](docs/en/how-to/measure-npc-capacity.md)
- Reference: [metrics schema](docs/en/reference/metrics-schema.md)
- Explanation: [hybrid architecture](docs/en/explanation/hybrid-architecture.md)

## Principles

- Use hardware you already own before buying another board or computer.
- Keep measured results, calculated scenarios, and project decisions separate.
- Treat missing data as `unavailable`, never as zero.
- Keep gameplay authority and safety rules outside the LLM.
- Bind experimental inference services to loopback unless a documented,
  authenticated private-network deployment is explicitly intended.
- Never paste production secrets, client data, or private firmware backups into
  examples or benchmark results.

## Repository boundaries

This candidate contains documentation, synthetic examples, schemas, and a small
capacity calculator. It does not contain the proprietary Zig server, hosted
infrastructure, production data, commercial components, credentials, or rights
to operate any Ultimate Odycer service.

See [PUBLICATION_STATUS.md](PUBLICATION_STATUS.md), [SECURITY.md](SECURITY.md),
[LICENSE.md](LICENSE.md), and [NOTICE.md](NOTICE.md) before reuse or publication.

Documentation is licensed under `CC-BY-4.0`. Scripts, schemas, and examples are
licensed under `MIT`; the file mapping in `LICENSE.md` is authoritative.
