# Architecture client

Statut : `decision` pour les frontières d'autorité et `evidence-tracked` pour la maturité des starters publics. Les sockets vers le serveur Zig canonique restent **non prouvées** tant qu'une baseline serveur exacte et une preuve E2E réelle ne sont pas enregistrées.

## État actuel des clients

| Profil | Dépôt public | État vérifiable actuel |
|---|---|---|
| Godot VR MMORPG | `ultod-client-godot-vr-mmorpg-template` | shell OpenXR ; métadonnées historiques Godot 4.3 ; cible 4.7.2 non prouvée ; ancien réseau `LEGACY_QUARANTINED` ; couches intention/transport sans socket + transport synthétique déterministe **préparé et gardé par CI**, fixture runtime pas encore exécutée |
| Godot Classic 3D | `ultod-client-godot-classic-3d-mmorpg-template` | shell 3D ; métadonnées historiques Godot 4.3 ; cible 4.7.2 non prouvée ; couches intention/transport sans socket + transport synthétique déterministe **préparé et gardé par CI**, fixture runtime pas encore exécutée |
| Three.js 2.5D | `ultod-client-threejs-2-5d-mmorpg-template` | application Vite/TypeScript ; `NetworkClient` fail-closed ; fixture synthétique transport exécutée et validée ; niveau `SYNTHETIC_FIXTURE_ONLY`, compatibilité Zig réelle `NOT_PROVEN` |
| FoveaCore FPS-RPG | `ultod-client-foveacore-fps-rpg-template` | fondation spécialisée en construction ; ne pas inférer la compatibilité Zig |
| NetherCore ARPG (Three.js) | `ultod-client-threejs-nethercore-arpg-template` | présentation ARPG Web ; aucune compatibilité héritée du client 2.5D |

Unity est **LEGACY** et n'est plus une cible de développement active Ultimate Odycer.

Le code client ou serveur propriétaire Ultimate Odycer ne doit pas être importé dans les starters publics sans revue de provenance et de licence fichier par fichier.

## Structure réseau publique actuelle

Les starters Godot P0 séparent désormais :

```text
input / OpenXR / desktop
        |
        v
net/intent_contract.gd
  validation client bornée
  session / move / interact / talk
        |
        v
net/transport_adapter.gd
  cycle abstrait
  disconnected / connecting / authenticating / online
        |
        v
net/synthetic_transport.gd
  autorité de test déterministe sans socket
  PREPARED / CI-GUARDED
  exécution runtime encore en attente
        |
        v
futur adaptateur de transport réel
  BLOQUÉ jusqu'à baseline Zig exacte + preuve E2E réelle
```

La couche publique refuse les champs d'autorité client tels que dégâts, monnaie, inventaire, permissions, téléportation arbitraire ou position serveur. Cette défense côté client ne remplace jamais la validation Zig.

La fixture Godot préparée couvre explicitement : échec offline, gate d'authentification, rejet des entrées malformées/champs d'autorité, mouvement assaini, coupure explicite, reconnexion/reprise et fermeture. Son résultat maximal autorisé reste `SYNTHETIC_FIXTURE_ONLY`. La CI documentaire hébergée contrôle sa structure et ses frontières de preuve mais **n'exécute pas Godot**.

Pour VR, le lanceur synthétique préparé utilise `--xr-mode off` ; runtime OpenXR, casque/contrôleurs, réseau pose/grab/release et interopérabilité Zig restent des gates indépendants non prouvés.

## Présentation versus autorité

```text
entrée OpenXR / desktop / Web
        |
        v
pose locale, locomotion confort, prédiction
        |  jetée/réconciliée si le serveur refuse
        v
intention client bornée
        v
serveur autoritaire ou autorité de test explicitement synthétique
        v
diff d'état / événement accepté ou refusé
        v
présentation, interpolation, LOD, audio, haptique
```

Le client ne décide jamais des dégâts, de l'or, de l'inventaire, des récompenses, des permissions ou de l'état persistant du monde.

## Niveaux de preuve à ne pas confondre

- `DOCUMENTED` / `DECLARED` : documentation ou métadonnées seulement ;
- `PREPARED_CI_GUARDED` : implémentation présente et gates statiques/structurels verts, mais scénario runtime non exécuté ;
- `SYNTHETIC_FIXTURE_ONLY` : fixture contrôlée réellement exécutée, sans serveur Zig canonique ;
- `ENGINE_LOAD_PROVEN` : le projet charge avec le moteur nommé ; ne prouve pas le réseau ;
- `OPENXR_INIT_PROVEN` : runtime OpenXR nommé initialisé ; ne prouve pas casque/réseau ;
- `HEADSET_RUNTIME_PROVEN` : scénario casque/contrôleurs nommé ; ne prouve pas le serveur ;
- `REAL_SERVER_E2E` : client/serveur exacts, révisions nommées, scénario reproductible ;
- `FAKE-GREEN` : test vert utilisé pour revendiquer plus que ce qu'il exerce.

## Chemin de connexion

La documentation publique possède deux niveaux à distinguer :

1. `network-intent-v1` est un contrat public synthétique et transport-indépendant ;
2. `server-network-contract.md` est un **snapshot d'implémentation non épinglé**, ni protocole courant vérifié ni preuve de compatibilité client.

Le snapshot historique décrivait du TCP binaire brut pour login/jeu. Tant que ces détails ne sont pas rattachés à un SHA/tree/toolchain Zig courant exact, les agents doivent considérer le transport courant comme non vérifié. Un navigateur ne doit donc jamais inventer ou supposer un WebSocket joueur ; un pont/passerelle ou endpoint officiel séparé exige sa propre preuve nommée.

## Règle pour les agents

Avant de modifier un client :

1. lire cette page ;
2. lire `../reference/network-contract.md` ;
3. lire `../reference/server-network-contract.md` en conservant son statut non épinglé/non validé ;
4. lire la matrice moteurs/templates ;
5. lire proof-levels et compatibility manifests du dépôt concerné ;
6. distinguer fixture préparée/gardée par CI et reçu runtime réellement exécuté ;
7. ne jamais promouvoir `zig_compatibility`, Godot 4.7.2, OpenXR, casque ou runtime synthétique sans reçu exécutable correspondant.

## Pages liées

- [Vue d'ensemble de l'écosystème](ecosystem-overview.md)
- [Contrat réseau public](../reference/network-contract.md)
- [Snapshot réseau serveur non épinglé](../reference/server-network-contract.md)
- [Matrice moteurs, templates et mondes](../reference/engine-template-world-matrix.md)
