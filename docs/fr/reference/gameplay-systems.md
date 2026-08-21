# Systèmes de gameplay

Statut : conventions d'authoring publiques. Ces systèmes décrivent comment
un créateur représente un monde ; ce n'est pas un recueil de règles, une
feuille d'équilibrage ou une table de loot du jeu propriétaire.

La résolution autoritaire reste toujours côté serveur. Les modèles du
[registre JSON](https://github.com/zedarvates/ultod-json-template-registry)
peuvent décrire présentation et données, pas des dons.

## Carte des systèmes

| Système | Le créateur décrit | Le serveur valide | Familles de modèles à inspecter |
|---|---|---|---|
| Identite | races, classes, apparences | stats, emplacements, permissions | avatars, names, styles |
| Progression | compétences, professions, paragons | XP, rangs, déverrouillages | professions, paragons, abilities |
| Combat | capacités, boss, rencontres | dégâts, ressources, immunités | abilities, bosses, créatures |
| Monde | biomes, lieux, donjons, rifts | accès, instances, voyage | biomes, locations, dungeons, rifts |
| Quêtes | objectifs, prologues, contenu généré | drapeaux, récompenses, échec | quests, prologues, generated-content |
| Économie | recettes, intention de loot, maisons | fonds, crafts, propriété | recipes, houses, masterpieces |
| Social | factions, guildes, réputation, événements | standing, invitations, courrier | guilds, events, social-events, marriage, mentorship, party |
| Divin / extra | dieux, énergie, calques RTS | jamais depuis des claims client | gods, energy, rts, divine-system, blueprints |

Une famille presente dans le registre est un instantané expérimental. Une
liste de compatibilité vide signifie aucune version client ou serveur
certifiée.

## Règles d'authoring

- décrire des données, pas un état joueur live ;
- garder des identifiants stables en `snake_case` ;
- utiliser des unités explicites ;
- ne jamais mettre secrets, URL de production ou overrides admin dans un modèle ;
- laisser `compatibility` vide sans preuve ;
- traiter `enabled: true` comme déclaratif, pas comme une permission ;
- épingler versions et empreintes SHA-256 avant lecture client.

Chemin pratique : [créer du contenu](../how-to/author-world-content.md).

## Ce qui reste non publié

Les courbes de combat numériques, tables de loot live, puits d'économie de
production et l'équilibrage canonique des classes ne sont pas publics. Ne
les inventez pas à partir de cette page.
