# Use and version JSON templates

Use this guide to consume or propose templates in
[ultod-json-template-registry](https://github.com/zedarvates/ultod-json-template-registry)
without treating the registry as a live game database.

## 1. Read the contract

The registry defines:

- file layout: `templates/<family>/<name>/v<MAJOR>.<MINOR>.<PATCH>/`;
- required fields for new templates: `id`, `template_type`, `version`;
- catalogue fields, including SHA-256 and `compatibility`;
- statuses: `draft`, `experimental`, `stable`, `deprecated`.

Follow the registry [TEMPLATE-SPEC.md](https://github.com/zedarvates/ultod-json-template-registry/blob/main/TEMPLATE-SPEC.md)
and [VERSIONING.md](https://github.com/zedarvates/ultod-json-template-registry/blob/main/VERSIONING.md).
Do not copy those files into this repository.

## 2. Consume a template

1. Resolve the entry through `templates/catalog.json`.
2. Pin the exact version. Never assume that latest is compatible.
3. Verify the SHA-256 before use.
4. Vendor a reviewed snapshot for deterministic builds.
5. Treat experimental status as unstable.
6. Treat an empty compatibility list as no certified compatibility.
7. Validate gameplay values on the server. Templates do not grant gold,
   items, damage, or movement speed.

Clients must not download or activate templates automatically at runtime.

## 3. Create a new template

Use kebab-case ASCII for family and name, snake_case for identifiers, and a
new SemVer directory for every change. A published version is immutable.

Minimal shape:

```json
{
  "id": "community_festival",
  "template_type": "event",
  "version": "1.0.0",
  "name": "Community Festival",
  "description": "A small recurring social event.",
  "enabled": true,
  "tags": ["social", "seasonal"],
  "duration_ms": 3600000,
  "dependencies": ["location_town_square"]
}
```

Leave `compatibility` empty until a named consumer, version, date, and
evidence exist.

## 4. Validate before proposing

- JSON must be strict UTF-8, with no comments;
- units must be explicit;
- references must be logical ids, never absolute paths;
- no secrets, production URLs, personal data, or admin overrides;
- document limits in the version README;
- compute the real SHA-256 before publication.

A template in the registry is not proof of server or client integration.

## Related pages

- [Author world content](author-world-content.md)
- [Gameplay systems](../reference/gameplay-systems.md)
- [Ecosystem overview](../explanation/ecosystem-overview.md)
