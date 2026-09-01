# Matrice des moteurs, templates et formes de monde

Cette référence aide un humain ou un LM à recommander un point de départ sans transformer une préférence en promesse de compatibilité.

## Moteurs

| Moteur | Place dans le parcours | Limite actuelle |
|---|---|---|
| Godot | chemin principal 3D/VR | cible 4.7.2 ; exécution moteur en attente ; fixture synthétique préparée/gardée par CI mais runtime non prouvé ; réseau Zig live non prouvé |
| Three.js | client Web léger + banc de protocole | fixture synthétique réellement exécutée/validée ; navigateur ↔ Zig canonique live non prouvé |
| Unity | `LEGACY` uniquement | plus une cible de développement active |
| FoveaCore | chemin FPS/RPG spécialisé | fondation en construction |
| Unreal Engine | alternative externe | aucun template Ultimate Odycer validé |

## Échelle de maturité

`PROVEN` signifie preuve reproductible contre des révisions nommées. `IMPLEMENTED` = code sans preuve complète. `PARTIAL` = incomplet. `MOCK` = simulé. `SCAFFOLD` = structure seulement. `DECLARED` = documentation/métadonnées. `PREPARED_CI_GUARDED` = implémentation présente et gates structurels verts mais runtime non exécuté. `LEGACY` = historique/réutilisation ciblée. `BLOCKED` = preuve requise inaccessible. `WAITING` = prérequis ouvert. `FAKE-GREEN` = test vert utilisé pour revendiquer plus qu'il n'exerce.

## Matrice client / serveur — état P0 courant

| Composant | Présentation | Contrat d'intention | Transport abstrait/synthétique | Zig canonique live | Statut |
|---|---:|---:|---:|---:|---|
| Three.js 2.5D | oui | oui | **fixture synthétique + NetworkClient exécutés et validés** | `NOT_PROVEN` | `IMPLEMENTED/PARTIAL` |
| Godot Classic | oui | oui, sans socket | adaptateur abstrait + fixture déterministe `PREPARED_CI_GUARDED`; runtime `NOT_YET_EXECUTED` | `NOT_PROVEN` | `PARTIAL` |
| Godot VR | oui | oui, sans socket | même fixture préparée avec XR off ; ancien réseau `LEGACY_QUARANTINED` ; runtime `NOT_YET_EXECUTED` | `NOT_PROVEN` | `PARTIAL` |
| serveur Zig privé | n/a public | source d'autorité cible | baseline exacte transport/protocole courante non épinglée | source de vérité cible | `BLOCKED` pour promotion de preuve |
| WebAdmin privé | oui | n/a | surface admin séparée ; audit P0 fail-closed | preuve contrat Zig exacte en attente | `PARTIAL / evidence-tracked` |

### Préparation de la preuve synthétique Godot

Les deux branches P0 Godot contiennent maintenant :

- validation bornée des intentions de base ;
- cycle de transport abstrait sans socket ;
- autorité synthétique déterministe sans socket ;
- scénario GDScript couvrant offline/auth/erreur/champs d'autorité/mouvement/drop/reprise/fermeture ;
- lanceur Python exigeant Godot 4.7.2 exact et écrivant un reçu JSON dans `.evidence/`.

La CI hébergée valide uniquement structure, marqueurs de non-promotion et syntaxe Python. Elle **n'exécute pas Godot** : le runtime reste `NOT_YET_EXECUTED` et ne peut devenir `SYNTHETIC_FIXTURE_ONLY` qu'après succès réel du lanceur.

Pour VR, ce lanceur préparé utilise `--xr-mode off` ; preuves OpenXR/casque restent séparées et fausses.

### Godot 4.7.2 / VR

Les validateurs moteur peuvent produire des reçus indépendants :

- Classic : import + bootstrap headless sous Godot 4.7.2-stable ;
- VR : même preuve avec `--xr-mode off`, en conservant explicitement OpenXR/casque/réseau à false.

Tant que ces commandes n'ont pas réellement réussi avec le binaire exact, les métadonnées projet restent historiquement 4.3 et 4.7.2 reste `NOT_PROVEN`.

### Three.js

Three.js possède un gate synthétique réellement exécuté. Son niveau reste `SYNTHETIC_FIXTURE_ONLY` ; il ne prouve pas de round-trip avec `zig-server-v2`.

### Transport serveur

`server-network-contract.md` est désormais un **snapshot d'implémentation non épinglé**. Un snapshot historique décrivait du TCP binaire brut, mais le transport/protocole courant n'est pas vérifié tant qu'il n'est pas rattaché à un SHA/tree/toolchain Zig courant exact. Un navigateur ne doit donc jamais supposer un WebSocket joueur ; tout pont/passerelle ou endpoint officiel exige une preuve séparée.

## Programme P0

Tracker public `ultimate-odycer-feedback` :

- `#5` baseline Zig exacte et version/protocole ;
- `#6` Zig ↔ Three.js réel ;
- `#7` même preuve dans Godot Classic/VR ;
- `#8` fuzzing, anti-replay, anti-duplication ;
- `#9` crash-safe persistence/snapshot/restore ;
- `#10` simulation sociale déterministe + AI LOD ;
- `#11` frontière licence public/open-source ↔ privé/commercial.

## Règles agents

Avant de modifier client/réseau :

1. ne pas utiliser la fraîcheur d'un document comme preuve ;
2. lire proof levels et compatibility manifest du dépôt cible ;
3. distinguer fixture préparée/gardée statiquement et preuve runtime exécutée ;
4. garder le synthétique explicitement synthétique ;
5. ne jamais copier l'ancien réseau VR sans revue provenance/licence/sécurité ;
6. ne jamais inventer de WebSocket joueur pour Three.js ;
7. ne jamais promouvoir Godot 4.7.2, runtime synthétique, OpenXR, casque ou Zig sans reçu exécutable correspondant ;
8. préserver la frontière licence publique ↔ privé propriétaire/commercial.

## Templates

| Dépôt | Expérience | Statut actuel |
|---|---|---|
| `ultod-client-godot-classic-3d-mmorpg-template` | MMORPG 3D classique | `PARTIAL / synthetic fixture PREPARED_CI_GUARDED / runtime pending` |
| `ultod-client-godot-vr-mmorpg-template` | MMORPG VR | `PARTIAL / synthetic fixture PREPARED_CI_GUARDED / legacy network quarantined` |
| `ultod-client-threejs-2-5d-mmorpg-template` | MMORPG Web 2.5D | `IMPLEMENTED presentation / SYNTHETIC_FIXTURE_ONLY` |
| `ultod-client-foveacore-fps-rpg-template` | FPS/RPG | `under_construction` |
| `ultod-client-threejs-nethercore-arpg-template` | ARPG Web | présentation distincte ; aucune compatibilité héritée |

## Formes de monde

| Topologie | Choisissez-la pour | Coût de départ |
|---|---|---|
| `flat_map` | villes, régions, arènes, donjons | faible |
| `planet` | exploration continue d'une planète | élevé |
| `mega_planet` | planète très vaste | très élevé |
| `solar_system` | plusieurs corps et voyages | maximal |

Les choix de monde ne modifient pas les gates de preuve réseau, persistance ou sécurité.
