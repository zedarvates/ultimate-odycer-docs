# Créer un monde, un biome, un PNJ ou un objet

Utilisez le registre JSON public comme atelier de contenu, puis gardez
l'autorité sur le serveur non publié. Ce guide ne publié pas de contenu de
production.

## 1. Choisir une famille

| Vous voulez créer | Commencer dans la famille | Lire aussi |
|---|---|---|
| un biome ou une ambiance extérieure | `biomes` | locations |
| une ville, un donjon ou une rift | `locations`, `dungeons`, `rifts` | events |
| un PNJ ou une créature | `créatures`, `ai` | names, styles, abilities |
| un objet ou une recette | `recipes`, `masterpieces` | houses |
| une quête | `quests`, `prologues` | generated-content |
| une classe, compétence ou capacité | `abilities`, `professions`, `paragons` | avatars |

Voir [systèmes de gameplay](../reference/gameplay-systems.md) pour la carte
complete.

## 2. Décrire des données, pas un état live

Un modèle de biome peut nommer climat, tags de voyage et identifiants de
créatures. Il ne fait pas apparaître ces créatures tout seul. Un modèle PNJ
peut nommer un style de dialogue et une réplique de repli. Il ne donne pas
réputation ni or.

## 3. Garder des références logiques

Pointez d'autres modèles par des identifiants stables tels que
`location_town_square` ou `créature_gatekeeper`. N'embarquez ni chemins
absolus, ni URL de production, ni noms d'assets non publiés.

## 4. Versionner et valider

Suivez [utiliser les modèles JSON](use-json-templates.md) :

- nouveau dossier SemVer a chaque changement ;
- SHA-256 dans le catalogue ;
- `compatibility` vide tant qu'un consommateur réel n'est pas prouvé ;
- aucun secret, override admin ou donnée personnelle.

## 5. Intégrer plus tard, échouer ferme maintenant

Un futur client ou serveur pourra épingler l'instantané. Tant que cette
preuve n'existe pas, traitez le modèle comme documentation et fixture
synthétique. Hashes manquants, versions inconnues ou compatibilité non
supportée doivent échouer de manière fermée.

## Pages liées

- [Utiliser les modèles JSON](use-json-templates.md)
- [Pipeline d'agents PNJ](../explanation/npc-agent-pipeline.md)
- [Démarrer un projet](../tutorials/start-an-ultimate-odycer-project.md)
