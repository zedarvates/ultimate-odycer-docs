# Vue d'ensemble de l'écosystème Ultimate Odycer

Ce dépôt est le hub de documentation publique d'Ultimate Odycer. Il explique
comment les pièces publiques s'assemblent, ce qu'elles couvrent, et ce
qu'elles ne couvrent pas.

Il ne remplace pas un serveur publié, un client jouable ou un protocole
certifié. Ces éléments restent des portes de publication séparées.

## Ce que ce dépôt couvre

- les tutoriels bilingues de capacité PNJ et les guides matériel home lab ;
- la philosophie de conception publique et la frontière serveur / LLM / ESP32 ;
- l'architecture publique de l'écosystème ouvert ;
- les contrats utilisables sans code propriétaire : modèles JSON, limites des
  starters clients, autorité réseau et conventions d'authoring.

## Ce que ce dépôt ne couvre pas

- le code source du serveur Zig propriétaire, les API privées ou les points
  de production ;
- un client Godot, Three.js ou FoveaCore jouable ;
- les identifiants canoniques de messages, le cadrage ou la sérialisation ;
- l'infrastructure hébergée, la facturation, la modération ou les données joueur ;
- une compatibilité certifiée entre une version client nommée et une version
  serveur nommée.

Une preuve manquante est `unavailable`, pas un support impliqué.

## Dépôts publics officiels

| Dépôt | Rôle | Maturité | Compatibilité |
|---|---|---|---|
| [ultimate-odycer-docs](https://github.com/zedarvates/ultimate-odycer-docs) | Hub de documentation publique | Public, bilingue, validé pour la structure | Documentation seulement |
| [ultod-json-template-registry](https://github.com/zedarvates/ultod-json-template-registry) | Modèles et schémas JSON versionnés | Instantanés expérimentaux en `0.1.0` | Listes de compatibilité vides tant qu'elles ne sont pas prouvées |
| [ultod-client-godot-vr-mmorpg-template](https://github.com/zedarvates/ultod-client-godot-vr-mmorpg-template) | Starter Godot VR MMORPG | Shell de présentation minimal (OpenXR) | Alignement serveur bloqué |
| [ultod-client-godot-classic-3d-mmorpg-template](https://github.com/zedarvates/ultod-client-godot-classic-3d-mmorpg-template) | Starter Godot Classic 3D | Shell de présentation minimal (Desktop 3D) | Alignement serveur bloqué |
| [ultod-client-threejs-2-5d-mmorpg-template](https://github.com/zedarvates/ultod-client-threejs-2-5d-mmorpg-template) | Starter Three.js 2.5D | Shell de présentation Web minimal (Isométrique) | Alignement serveur bloqué |
| [ultod-client-foveacore-fps-rpg-template](https://github.com/zedarvates/ultod-client-foveacore-fps-rpg-template) | Starter FoveaCore FPS-RPG | Shell de présentation minimal (FPS Dual-mode) | Alignement serveur bloqué |
| [ultimate-odycer-feedback](https://github.com/zedarvates/ultimate-odycer-feedback) | Suivi public des bugs et idées | Issues publiques, sans code | Pas un composant runtime |

Les composants privés ou non publiés, dont le serveur Zig canonique, les
clients de jeu existants, WebAdmin et les services commerciaux, restent hors
de cette carte publique.

## Comment les pièces s'assemblent

```text
créateurs et joueurs
        |
        v
docs publiques (ce dépôt)
        |
        +--> registre JSON ----------- contrats de contenu versionnés
        |
        +--> starters clients -------- documentation jusqu'à extraction
        |         Godot VR / Godot Classic 3D / Three.js / FoveaCore
        |
        +--> voie PNJ home lab ------ inférence locale, expression ESP32
        |
        v
serveur de jeu autoritaire (propriétaire, non publié)
        |
        +--> valide identité, déplacement, combat, inventaire, économie
        +--> émet présentation et paquets d'expression PNJ bornés
        +--> persiste l'état du monde et des personnages
```

Un modèle JSON ne donne jamais or, objets, dégâts, vitesse ou permissions.
Un client n'est jamais autoritaire. Un LLM local n'est jamais un moteur de
règles.

## Par où commencer

| Objectif | Commencer ici |
|---|---|
| Comprendre la carte publique | cette page |
| Comprendre autorité, zones et réplication | [Vue d'architecture](architecture-overview.md) |
| Comprendre le comportement PNJ / LLM | [Pipeline d'agents PNJ](npc-agent-pipeline.md) |
| Comprendre les futurs clients | [Architecture client](client-architecture.md) |
| Comprendre la frontière serveur non publiée | [Architecture serveur](server-architecture.md) |
| Lire le contrat réseau public | [Contrat réseau](../reference/network-contract.md) |
| Utiliser ou créer des modèles JSON | [Utiliser les modèles JSON](../how-to/use-json-templates.md) |
| Créer un monde, un biome, un PNJ ou un objet | [Créer du contenu](../how-to/author-world-content.md) |
| Dimensionner un home lab PNJ | [Premier banc PNJ](../tutorials/first-npc-benchmark.md) |
| Signaler un problème public | [ultimate-odycer-feedback](https://github.com/zedarvates/ultimate-odycer-feedback) |
| Contribuer ou tester les pièces publiques | [Contribuer et tester](../how-to/contribute-and-test.md) |

Poursuivez avec la [vue d'architecture](architecture-overview.md) pour les
diagrammes et le [tutoriel de démarrage](../tutorials/start-an-ultimate-odycer-project.md)
pour un premier chemin qui reste dans le matériel public.
