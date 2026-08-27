# Author a world, biome, NPC, or item

Use the public JSON registry as a content workshop, then keep authority on
the unpublished server. This guide does not publish production content.

## 1. Choose a family

| You want to create | Start in the registry family | Also read |
|---|---|---|
| a biome or outdoor mood | `biomes` | locations |
| a town, dungeon, or rift | `locations`, `dungeons`, `rifts` | events |
| an NPC or creature | `creatures`, `ai` | names, styles, abilities |
| an item or recipe | `recipes`, `masterpieces` | houses |
| a quest | `quests`, `prologues` | generated-content |
| a class, skill, or ability | `abilities`, `professions`, `paragons` | avatars |

See [gameplay systems](../reference/gameplay-systems.md) for the full map.

## 2. Describe data, not live state

A biome template may name climate, travel tags, and creature ids. It may not
spawn those creatures in a running world by itself. An NPC template may name
a dialogue style and fallback line. It may not grant reputation or gold.

## 3. Keep references logical

Point to other templates by stable ids such as `location_town_square` or
`creature_gatekeeper`. Do not embed absolute paths, production URLs, or
unpublished asset filenames.

## 4. Version and validate

Follow [use JSON templates](use-json-templates.md):

- new SemVer directory for every change;
- SHA-256 in the catalogue;
- empty `compatibility` until a real consumer is proven;
- no secrets, admin overrides, or personal data.

## 5. Integrate later, fail closed now

A future client or server may pin the snapshot. Until that evidence exists,
treat the template as documentation and synthetic fixture material. Missing
hashes, unknown versions, or unsupported compatibility must fail closed.

## Related pages

- [Use JSON templates](use-json-templates.md)
- [NPC agent pipeline](../explanation/npc-agent-pipeline.md)
- [Start a project](../tutorials/start-an-ultimate-odycer-project.md)
