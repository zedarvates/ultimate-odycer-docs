# Gameplay systems

Status: public authoring conventions. These systems are how a creator
describes a world; they are not a published ruleset, balance sheet, or
loot table from the proprietary game.

Authoritative resolution always stays on the server. Templates from the
[JSON registry](https://github.com/zedarvates/ultod-json-template-registry)
may describe presentation and data, not grants.

## System map

| System | Creator describes | Server validates | Template families to inspect |
|---|---|---|---|
| Identity | races, classes, appearances | stats, slots, permissions | avatars, names, styles |
| Progression | skills, professions, paragons | XP, ranks, unlocks | professions, paragons, abilities |
| Combat | abilities, bosses, encounters | damage, resources, immunities | abilities, bosses, creatures |
| World | biomes, locations, dungeons, rifts | access, instances, travel | biomes, locations, dungeons, rifts |
| Quests | goals, prologues, generated content | flags, rewards, failure | quests, prologues, generated-content |
| Economy | recipes, loot intent, houses | funds, crafts, ownership | recipes, houses, masterpieces |
| Social | factions, guilds, reputation, events | standing, invites, mail | guilds, events, social-events, marriage, mentorship, party |
| Divine / extra | gods, energy, RTS-style overlays | never from client claims | gods, energy, rts, divine-system, blueprints |

A family present in the registry is an experimental snapshot. An empty
compatibility list means no certified client or server version.

## Authoring rules

- describe data, not live player state;
- keep identifiers stable and in `snake_case`;
- use explicit units;
- never put secrets, production URLs, or admin overrides in a template;
- leave `compatibility` empty without evidence;
- treat `enabled: true` as declarative, not as a permission;
- pin versions and SHA-256 hashes before a client reads them.

Worked path: [author world content](../how-to/author-world-content.md).

## What remains unpublished

Numeric combat curves, live loot tables, production economy sinks, and
canonical class balance are not public. Do not invent them from this page.
