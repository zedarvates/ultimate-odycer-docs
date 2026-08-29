# Matrice des moteurs, templates et formes de monde

Cette référence aide un humain ou un LM à recommander un point de départ sans
transformer une préférence en promesse de compatibilité.

## Moteurs

| Moteur | Place dans le parcours | Limite actuelle |
|---|---|---|
| Godot | Chemin recommandé principal pour client 3D/VR | Shells publics présents ; interopérabilité Zig réelle encore à prouver via les gates P0 |
| Three.js | Client Web léger et banc de protocole de référence | Shell public + fixture locale disponibles ; connexion au Zig canonique exact encore à prouver |
| Unity | Legacy uniquement | Ancienne architecture abandonnée pour le développement actif Ultimate Odycer |
| Unreal Engine | Alternative externe | Aucun template Ultimate Odycer validé |
| FoveaCore | Chemin spécialisé FPS/RPG | Fondation en construction |

## Échelle de maturité

| État | Signification |
|---|---|
| `PROVEN` | preuve reproductible contre une révision serveur/client nommée |
| `IMPLEMENTED` | implémenté mais pas encore entièrement prouvé |
| `PARTIAL` | implémentation incomplète |
| `MOCK` | simulation ou données factices |
| `SCAFFOLD` | structure/coque seulement |
| `DECLARED` | documentation ou données déclaratives uniquement |
| `LEGACY` | ancienne architecture conservée seulement pour historique/récupération ciblée |
| `BLOCKED` | preuve requise inaccessible ou dépendance non résolue |
| `WAITING` | travail identifié, condition précédente non satisfaite |
| `FAKE-GREEN` | test vert qui ne couvre pas le système réel annoncé |

## Matrice client / serveur actuelle

| Dépôt / composant | Présentation locale | Fixture synthétique | Zig canonique live | Sécurité négative | Statut global |
|---|---:|---:|---:|---:|---|
| `ultod-client-threejs-2-5d-mmorpg-template` | oui | oui | `WAITING` sur baseline exacte + preuve E2E | `WAITING` | `IMPLEMENTED/PARTIAL` |
| `ultod-client-godot-classic-3d-mmorpg-template` | oui | `WAITING` | `BLOCKED/WAITING` | `WAITING` | `SCAFFOLD/PARTIAL` |
| `ultod-client-godot-vr-mmorpg-template` | oui | `WAITING` | `BLOCKED` ; ancien contrat VR = `LEGACY` | `WAITING` | `SCAFFOLD/PARTIAL` |
| serveur Zig canonique privé | non public | preuves partielles documentées | source de vérité cible | à auditer | `BLOCKED` pour preuve publique directe tant que SHA exact non récupéré |

Programme P0 suivi dans `zedarvates/ultimate-odycer-feedback` :

- `#5` — figer la révision Zig canonique, framing, version negotiation et matrice de compatibilité ;
- `#6` — prouver le round-trip Zig ↔ Three.js réel ;
- `#7` — rejouer la même fixture dans Godot Classic et Godot VR ;
- `#8` — sécurité parano, fuzzing, anti-replay et anti-duplication ;
- `#9` — persistance crash-safe, snapshot et restauration ;
- `#10` — simulation sociale déterministe et AI LOD après fermeture des fondations P0 ;
- `#11` — frontière de licence privé commercial ↔ public open source.

Aucun statut `PROVEN` ne doit être attribué sans révisions exactes et preuve reproductible. Une fixture synthétique seule ne prouve pas la compatibilité avec le serveur canonique.

## Templates prévus ou en construction

| Dépôt | Nom affiché | Expérience | Statut |
|---|---|---|---|
| `ultod-client-godot-classic-3d-mmorpg-template` | Godot Classic 3D MMORPG | MMORPG 3D classique | `partial / P0 interoperability waiting` |
| `ultod-client-godot-vr-mmorpg-template` | Godot VR MMORPG | MMORPG en réalité virtuelle | `partial / Zig alignment blocked` |
| `ultod-client-threejs-2-5d-mmorpg-template` | Three.js 2.5D MMORPG | MMORPG Web isométrique | `implemented presentation / canonical E2E waiting` |
| `ultod-client-foveacore-fps-rpg-template` | FoveaCore FPS-RPG Online | FPS/RPG en ligne | `under_construction` |
| `ultod-client-godot-open-city-crime-rpg-template` | Prêt à tout faire pour de l'argent | RPG urbain multijoueur ouvert | `planned` |

Un dépôt documentaire ou une coque de présentation ne constitue pas un client MMO compatible tant que le chemin réseau autoritaire n'est pas prouvé.

## Frontière de licence

Les templates publics ne doivent contenir que du code original explicitement publié sous leur licence publique et des dépendances compatibles. Le serveur canonique privé, le gameplay propriétaire, la configuration de production, les assets/lore privés et les composants commerciaux restent propriétaires/commerciaux, tous droits réservés sauf licence explicite contraire. L'accès à un dépôt privé ne vaut pas autorisation de copier son implémentation dans un dépôt public. Toute extraction privé → public exige revue de provenance et de licence fichier par fichier ; préférer des adaptateurs réécrits contre les contrats publics et fixtures synthétiques approuvés.

## Formes de monde

| Topologie | Choisissez-la pour | Coût de départ |
|---|---|---|
| `flat_map` | villes, régions, arènes, donjons, jeux urbains | le plus faible |
| `planet` | exploration continue d'une planète | élevé |
| `mega_planet` | planète de très grande taille | très élevé |
| `solar_system` | voyages entre plusieurs corps | le plus élevé |

## Entrées dessinées et conversion

| Entrée | Traitement | Sortie | Intégration |
|---|---|---|---|
| Papier, PNG, JPEG ou SVG avec légende | Analyse humaine/LM avec incertitudes | `uo.map-intent/v1` | `reference_only` puis `conversion_required` |
| GeoJSON ou couches QGIS | Contrôle d'échelle, projection et attribution | proposition de monde versionnée | `conversion_required` |
| Blockout Blender ou GLB | Revue unités, collisions, LOD et licence | candidat 3D | `conversion_required` |
| CityConfig Lite | City Editor Lite | proposition ville bornée | `direct` vers le contrat Lite, pas vers le runtime |
| HouseBlueprint Lite | Architecture Editor Lite | proposition bâtiment | `direct` vers le contrat Lite, pas vers le runtime |
| XenoGenome Lite | Creature Editor Lite | proposition créature | `direct` vers le contrat Lite, statistiques serveur inchangées |

Les éditeurs Lite cités sont `executable_public` pour leurs contrats et tests
publics. Leurs aperçus restent `[Scaffolding / Proxy]` et ne prouvent ni Godot,
ni Zig, ni VR, ni publication serveur.

## Règles de recommandation

1. Choisissez la boucle de jeu avant la taille du monde.
2. Utilisez Godot en l'absence de contrainte contraire.
3. Utilisez Three.js comme client Web léger et banc de protocole rapide lorsque cela réduit le temps de validation.
4. Commencez par `flat_map` pour un jeu urbain, une arène ou un donjon.
5. Ne choisissez `planet` que si la continuité sphérique apporte une fonction indispensable au premier prototype.
6. Traitez `mega_planet` et `solar_system` comme des étapes avancées qui exigent des preuves de streaming, partitionnement, persistance et capacité.
7. Un LM recommande ; l'utilisateur décide et conserve la décision dans sa fiche de projet.

## Choix intrinsèques, pas automatiques

Un GTA-like conduit généralement à une carte plate, mais ce n'est pas une loi.
Un jeu spatial peut commencer sur une station représentée par une carte plate
avant d'ajouter un système solaire. Le guide doit expliquer le compromis plutôt
que choisir une architecture spectaculaire par défaut.
