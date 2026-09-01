# Matrice des moteurs, templates et formes de monde

Cette référence aide un humain ou un LM à recommander un point de départ sans transformer une préférence en promesse de compatibilité.

## Moteurs

| Moteur | Place dans le parcours | Limite actuelle |
|---|---|---|
| Godot | chemin principal 3D/VR | cible 4.7.2 ; chargement moteur réel encore à prouver ; réseau Zig live non prouvé |
| Three.js | client Web léger + banc de protocole | fixture synthétique réellement validée ; navigateur ↔ Zig canonique live non prouvé |
| Unity | `LEGACY` uniquement | architecture abandonnée pour le développement actif |
| FoveaCore | chemin FPS/RPG spécialisé | fondation en construction |
| Unreal Engine | alternative externe | aucun template Ultimate Odycer validé |

## Échelle de maturité

| État | Signification |
|---|---|
| `PROVEN` | preuve reproductible contre des révisions nommées |
| `IMPLEMENTED` | implémenté mais pas entièrement prouvé |
| `PARTIAL` | implémentation incomplète |
| `MOCK` | simulation/données factices |
| `SCAFFOLD` | structure ou coque seulement |
| `DECLARED` | documentation/métadonnées uniquement |
| `LEGACY` | ancienne architecture, réutilisation ciblée seulement |
| `BLOCKED` | preuve requise inaccessible |
| `WAITING` | travail identifié derrière un prérequis |
| `FAKE-GREEN` | test vert qui ne couvre pas le système annoncé |

## Matrice client / serveur — état P0 courant

| Composant | Présentation | Contrat d'intention | Transport abstrait/synthétique | Zig canonique live | Statut |
|---|---:|---:|---:|---:|---|
| Three.js 2.5D | oui | oui | **fixture synthétique + NetworkClient validés** | `NOT_PROVEN` | `IMPLEMENTED/PARTIAL` |
| Godot Classic | oui | oui, sans socket | adaptateur abstrait sans socket ; fixture synthétique suivante | `NOT_PROVEN` | `PARTIAL` |
| Godot VR | oui | oui, sans socket | adaptateur abstrait sans socket ; ancien réseau `LEGACY_QUARANTINED` | `NOT_PROVEN` | `PARTIAL` |
| serveur Zig privé | n/a public | source d'autorité cible | transport documenté mais baseline exacte à recapturer | source de vérité cible | `BLOCKED` pour promotion de preuve |
| WebAdmin privé | oui | n/a | HTTP/WS admin séparé du canal joueur | audit P0 fail-closed en cours | `PARTIAL / evidence-tracked` |

### Godot 4.7.2 / VR

Les PR P0 Godot contiennent des validateurs locaux qui peuvent produire des reçus JSON dans `.evidence/` :

- Classic : import + bootstrap headless avec **Godot 4.7.2-stable** ;
- VR : même preuve avec `--xr-mode off` ; ce reçu laisse explicitement `openxr_runtime_proven=false`, `headset_runtime_proven=false` et `network_compatibility_proven=false`.

Tant que ces commandes n'ont pas été exécutées avec le binaire exact, `project.godot` reste historiquement déclaré 4.3 et la cible 4.7.2 reste `NOT_PROVEN`.

### Three.js

Le gate synthétique actuel valide le client construit, les contrôles de transport et les fixtures négatives. Son niveau reste `SYNTHETIC_FIXTURE_ONLY`. Il ne prouve pas un round-trip avec `zig-server-v2`.

### Transport serveur

`server-network-contract.md` décrit actuellement le jeu/login comme **TCP binaire brut**. Un navigateur ne doit donc pas supposer un WebSocket joueur : Three.js exige un pont/passerelle documenté ou un endpoint officiel séparé avant toute preuve live. Cette description doit elle-même être rattachée à une baseline Zig exacte avant d'être promue comme contrat canonique vérifié.

## Programme P0

Tracker public `ultimate-odycer-feedback` :

- `#5` baseline Zig exacte et version/protocole ;
- `#6` Zig ↔ Three.js réel ;
- `#7` même preuve dans Godot Classic/VR ;
- `#8` fuzzing, anti-replay, anti-duplication ;
- `#9` crash-safe persistence/snapshot/restore ;
- `#10` simulation sociale déterministe + AI LOD ;
- `#11` frontière licence public/open-source ↔ privé/commercial.

WebAdmin privé suit en plus ses propres gates de provenance Zig, contrats read-only et mutations quarantainées.

## Règle pour agents

Avant toute modification client/réseau :

1. ne jamais utiliser la date d'un document comme preuve technique ;
2. lire les `proof levels` et `compatibility manifest` du dépôt concerné ;
3. traiter les données synthétiques comme synthétiques ;
4. ne pas copier l'ancien réseau VR ;
5. ne pas inventer de WebSocket joueur pour Three.js ;
6. ne pas promouvoir Godot 4.7.2, OpenXR, casque ou Zig sans reçu exécutable ;
7. préserver la frontière de licence : public = licence publique explicite ; serveur/gameplay/configuration privée = propriétaire/commercial, tous droits réservés sauf mention contraire.

## Templates

| Dépôt | Expérience | Statut actuel |
|---|---|---|
| `ultod-client-godot-classic-3d-mmorpg-template` | MMORPG 3D classique | `PARTIAL / engine+network proof pending` |
| `ultod-client-godot-vr-mmorpg-template` | MMORPG VR | `PARTIAL / legacy network quarantined` |
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
