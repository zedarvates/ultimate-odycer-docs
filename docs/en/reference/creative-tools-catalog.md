# Creative tools catalog reference

The machine-readable source of truth is
[creative-tools-catalog.json](../../../examples/creative-tools-catalog.json),
validated by its
[JSON Schema](../../../schemas/creative-tools-catalog-v1.schema.json).

## Reading a tool entry

| Field | Meaning |
|---|---|
| `maturity` | real public proof, prototype, proxy, planned, or external |
| `execution` | local, cloud, hybrid, or not applicable |
| `pricing_model` | free, purchase, subscription, credits, or limits (no exact prices) |
| `commercial_use` | permitted, conditional, plan/asset/model dependent |
| `privacy` | processing location and data privacy boundary |
| `ai_training_terms` | applicable training terms or verification status |
| `integration` | direct, conversion required, or reference only |
| `verified_on` | date of last official verification |

## Ultimate Odycer tool status values

- `executable_public`: source code and automated public tests available;
- `prototype_local`: bounded local functionality;
- `scaffolding_proxy`: preview or schema contract without runtime pipeline;
- `planned`: architectural design without a usable tool;
- `verification_required`: insufficient current proof.

Creature, City, Architecture, Dungeon, and Avatar Editor Lite are
`executable_public`, but their visual previews remain `[Scaffolding / Proxy]`.
Full editors do not inherit this status by association.

## Choosing the right tool

1. Check `recommendations` for the target production domain.
2. Start with `default_tool` (local/free first).
3. Verify platform compatibility, formats, and conversion requirements.
4. Open the official pricing or license link.
5. Audit every imported asset, third-party model, and plug-in individually.
6. Switch to cloud tools only after completing the privacy audit.

A valid link does not guarantee that legal terms have remained unchanged. An
outdated entry must be flagged as `verification_required`.
