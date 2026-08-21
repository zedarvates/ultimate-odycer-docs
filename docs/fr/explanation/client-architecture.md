# Architecture client

Statut : `decision` pour les starters publics visés ; aucun client jouable
n'est publié. Les dépôts Godot VR, Godot Classic 3D, Three.js 2.5D et
FoveaCore contiennent aujourd'hui périmètre, feuille de route et portes de
compatibilité, pas des projets de jeu.

## Coques clientes visées

| Profil | Dépôt public | Contenu actuel |
|---|---|---|
| Godot VR MMORPG | [ultod-client-godot-vr-mmorpg-template](https://github.com/zedarvates/ultod-client-godot-vr-mmorpg-template) | documentation seulement |
| Godot Classic 3D | [ultod-client-godot-classic-3d-mmorpg-template](https://github.com/zedarvates/ultod-client-godot-classic-3d-mmorpg-template) | documentation seulement |
| Three.js 2.5D | [ultod-client-threejs-2-5d-mmorpg-template](https://github.com/zedarvates/ultod-client-threejs-2-5d-mmorpg-template) | documentation seulement |
| FoveaCore FPS-RPG | [ultod-client-foveacore-fps-rpg-template](https://github.com/zedarvates/ultod-client-foveacore-fps-rpg-template) | documentation seulement |

Le code client Ultimate Odycer existant ne doit pas être importé sans audit
d'extraction publique fichier par fichier.

## Structure de projet cible

Un futur starter original DEVRAIT ressembler à ceci, sans copier de scènes
ou d'assets propriétaires :

```text
client-starter/
  fichiers de projet du moteur choisi
  scenes/
    bootstrap           moteur, plateforme et contrôles qualité
    login               aucun secret dans la scène
    realm-handoff       rejoint un espace assigné par le serveur
    player              présentation locale d'une entité autoritaire
    npc                 présentation et invites d'interaction seulement
    zone                géométrie streamée et objets d'intérêt
    ui                  HUD, menus, panneaux VR
  input/
    abstractions desktop ou OpenXR
  net/
    client de protocole, une fois un contrat public existant
  content/
    instantanés du registre JSON épinglés
```

Des dossiers manquants dans les dépôts publics signifient que le starter
n'est pas publié, pas qu'un projet caché est impliqué.

## Présentation versus autorité

```text
entrée OpenXR / desktop
        |
        v
pose locale, locomotion confort, prédiction
        |  jetée si le serveur refuse
        v
intention : bouger, interagir, parler, utiliser, crafter
        v
serveur autoritaire
        v
diff d'état, indices d'animation, expression PNJ
        v
streaming de scènes, LOD, audio, haptique
```

La physique et les collisions locales peuvent garder un casque confortable.
Elles ne doivent pas donner de loot, appliquer des dégâts, changer
l'inventaire ou accepter un speed hack. Les réglages de confort VR sont
côté client ; les règles du monde ne le sont pas.

## Chemin de connexion

Tant qu'une version de protocole publique n'est pas approuvée, un client
peut seulement :

1. documenter la séquence visée de login et de handoff ;
2. consommer des modèles JSON épinglés pour labels et fixtures synthétiques ;
3. mener des expériences de présentation locales, hors réseau ;
4. refuser points de production, identifiants et dumps de protocole.

Une fixture de boucle locale synthétique est la première preuve réseau
autorisée. Une exécution desktop isolée ne prouvé pas l'interopérabilité VR.

## Pages liées

- [Vue d'ensemble de l'écosystème](ecosystem-overview.md)
- [Contrat réseau](../reference/network-contract.md)
- [Utiliser les modèles JSON](../how-to/use-json-templates.md)
- [Démarrer un projet](../tutorials/start-an-ultimate-odycer-project.md)
