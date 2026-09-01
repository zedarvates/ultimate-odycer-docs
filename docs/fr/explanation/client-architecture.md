# Architecture client

Statut : `decision` pour les frontières d'autorité et `evidence-tracked` pour la maturité des starters publics. Les sockets vers le serveur Zig canonique restent **non prouvées** tant qu'une baseline serveur exacte et une preuve E2E réelle ne sont pas enregistrées.

## État actuel des clients

| Profil | Dépôt public | État vérifiable actuel |
|---|---|---|
| Godot VR MMORPG | `ultod-client-godot-vr-mmorpg-template` | shell OpenXR ; métadonnées projet historiques Godot 4.3 ; cible 4.7.2 non encore prouvée ; ancien réseau `LEGACY_QUARANTINED` ; contrat d'intention + adaptateur de transport abstrait sans socket présents sur PR P0 |
| Godot Classic 3D | `ultod-client-godot-classic-3d-mmorpg-template` | shell 3D ; métadonnées projet historiques Godot 4.3 ; cible 4.7.2 non encore prouvée ; contrat d'intention + adaptateur de transport abstrait sans socket présents sur PR P0 |
| Three.js 2.5D | `ultod-client-threejs-2-5d-mmorpg-template` | application Vite/TypeScript ; `NetworkClient` fail-closed ; fixture synthétique et tests transport validés ; niveau de preuve `SYNTHETIC_FIXTURE_ONLY`, compatibilité Zig réelle `NOT_PROVEN` |
| FoveaCore FPS-RPG | `ultod-client-foveacore-fps-rpg-template` | fondation spécialisée en construction ; ne pas inférer la compatibilité Zig |
| NetherCore ARPG (Three.js) | `ultod-client-threejs-nethercore-arpg-template` | présentation ARPG Web ; ne pas inférer la compatibilité Zig depuis le client Three.js 2.5D |

Unity est **LEGACY** et n'est plus une cible de développement active Ultimate Odycer.

Le code client ou serveur propriétaire Ultimate Odycer ne doit pas être importé dans ces dépôts publics sans revue de provenance et de licence fichier par fichier.

## Structure réseau publique actuelle

Les starters Godot P0 séparent désormais explicitement :

```text
input / OpenXR / desktop
        |
        v
net/intent_contract.gd
  validation client bornée
  familles : session / move / interact / talk
        |
        v
net/transport_adapter.gd
  cycle abstrait : disconnected / connecting / authenticating / online
  aucun socket, endpoint, opcode ou framing Zig privé
        |
        v
futur adaptateur de transport réel
  BLOQUÉ jusqu'à baseline Zig exacte + preuve E2E
```

Cette couche publique refuse notamment les champs d'autorité client tels que dégâts, monnaie, inventaire, permissions, téléportation arbitraire ou position serveur. Cette défense côté client ne remplace jamais la validation Zig.

Three.js dispose déjà d'un transport synthétique testable. Cela ne signifie pas qu'un navigateur peut parler directement au serveur de jeu Zig actuel.

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
serveur autoritaire
        v
diff d'état / événement accepté ou refusé
        v
présentation, interpolation, LOD, audio, haptique
```

Le client ne décide jamais des dégâts, de l'or, de l'inventaire, des récompenses, des permissions ou de l'état persistant du monde.

## Niveaux de preuve à ne pas confondre

- `DOCUMENTED` / `DECLARED` : documentation ou métadonnées seulement ;
- `SYNTHETIC_FIXTURE_ONLY` : fixture locale contrôlée, sans serveur Zig canonique ;
- `ENGINE_LOAD_PROVEN` : le projet charge avec le moteur nommé ; ne prouve pas le réseau ;
- `OPENXR_INIT_PROVEN` : runtime OpenXR nommé initialisé ; ne prouve pas le casque ni le réseau ;
- `HEADSET_RUNTIME_PROVEN` : scénario casque/contrôleurs nommé ; ne prouve pas le serveur ;
- `REAL_SERVER_E2E` : client et serveur exacts, révisions nommées, scénario reproductible ;
- `FAKE-GREEN` : un test vert utilisé pour revendiquer plus que ce qu'il exerce réellement.

## Chemin de connexion

La documentation publique possède deux niveaux qu'un agent doit distinguer :

1. `network-intent-v1` est un contrat public synthétique et transport-indépendant ;
2. `server-network-contract.md` décrit un état de transport serveur issu de décisions d'implémentation, mais **ne constitue pas une preuve de compatibilité client** et doit être revalidé contre la baseline Zig exacte avant toute promotion.

En particulier, le client Web Three.js ne doit pas supposer qu'un endpoint WebSocket joueur existe. Le serveur décrit actuellement un transport jeu TCP binaire ; un client navigateur exige donc un pont/passerelle ou un endpoint officiel séparé, tous deux encore à prouver.

## Règle pour les agents

Avant de modifier un client :

1. lire cette page ;
2. lire `../reference/network-contract.md` ;
3. lire `../reference/server-network-contract.md` en conservant son statut non validé ;
4. lire la matrice moteurs/templates ;
5. lire les proof-levels et compatibility manifests du dépôt client concerné ;
6. ne jamais promouvoir `zig_compatibility`, Godot 4.7.2, OpenXR ou casque à `PROVEN` sans le reçu exécutable correspondant.

## Pages liées

- [Vue d'ensemble de l'écosystème](ecosystem-overview.md)
- [Contrat réseau public](../reference/network-contract.md)
- [Contrat réseau serveur documenté](../reference/server-network-contract.md)
- [Matrice moteurs, templates et mondes](../reference/engine-template-world-matrix.md)
