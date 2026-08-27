# Matrice des moteurs, templates et formes de monde

Cette référence aide un humain ou un LM à recommander un point de départ sans
transformer une préférence en promesse de compatibilité.

## Moteurs

| Moteur | Place dans le parcours | Limite actuelle |
|---|---|---|
| Godot | Chemin recommandé et détaillé | Les templates publics restent en construction |
| Three.js | Alternative Web | Adaptation réseau et expérience 2.5D à valider |
| Unity | Alternative | Aucun template Ultimate Odycer validé |
| Unreal Engine | Alternative | Aucun template Ultimate Odycer validé |
| FoveaCore | Chemin spécialisé FPS/RPG | Fondation en construction |

## Templates prévus ou en construction

| Dépôt | Nom affiché | Expérience | Statut |
|---|---|---|---|
| `ultod-client-godot-classic-3d-mmorpg-template` | Godot Classic 3D MMORPG | MMORPG 3D classique | `under_construction` |
| `ultod-client-godot-vr-mmorpg-template` | Godot VR MMORPG | MMORPG en réalité virtuelle | `under_construction` |
| `ultod-client-threejs-2-5d-mmorpg-template` | Three.js 2.5D MMORPG | MMORPG Web isométrique | `under_construction` |
| `ultod-client-foveacore-fps-rpg-template` | FoveaCore FPS-RPG Online | FPS/RPG en ligne | `under_construction` |
| `ultod-client-godot-open-city-crime-rpg-template` | Prêt à tout faire pour de l'argent | RPG urbain multijoueur ouvert | `planned` |

Un dépôt documentaire sans code client est une direction de conception, pas un
client jouable.

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
3. Commencez par `flat_map` pour un jeu urbain, une arène ou un donjon.
4. Ne choisissez `planet` que si la continuité sphérique apporte une fonction
   indispensable au premier prototype.
5. Traitez `mega_planet` et `solar_system` comme des étapes avancées qui exigent
   des preuves de streaming, partitionnement, persistance et capacité.
6. Un LM recommande ; l'utilisateur décide et conserve la décision dans sa
   fiche de projet.

## Choix intrinsèques, pas automatiques

Un GTA-like conduit généralement à une carte plate, mais ce n'est pas une loi.
Un jeu spatial peut commencer sur une station représentée par une carte plate
avant d'ajouter un système solaire. Le guide doit expliquer le compromis plutôt
que choisir une architecture spectaculaire par défaut.
