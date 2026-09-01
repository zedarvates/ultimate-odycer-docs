# Vue d'ensemble du contrat réseau serveur

Statut : **snapshot d'implémentation non épinglé — compatibilité non validée**.

Cette page ne doit plus être lue comme « le protocole canonique courant ». Les détails de transport/opcodes historiquement documentés doivent être **revalidés contre une baseline exacte `zig-server-v2`** avant toute réutilisation dans un client, un SDK, une passerelle ou une documentation de compatibilité.

## Ce qui reste une décision publique stable

- Le serveur est autoritaire pour identité/session, déplacement, combat, inventaire, économie, permissions et persistance.
- Le client envoie des intentions ; il ne décide jamais des dégâts, de l'or, de l'inventaire ou des résultats persistants.
- Authentification, handoff, versioning, framing, réplication, reconnexion et transport doivent être bornés et testés.
- TLS est attendu hors boucle locale selon la configuration approuvée.
- Les entrées invalides, inconnues, surdimensionnées ou rejouées ne doivent ni muter l'état ni faire tomber un shard.

## État du transport historiquement documenté

Une révision précédente de cette documentation décrivait les services login/jeu comme **TCP binaire brut** et WebAdmin comme HTTP/WebSocket séparé du canal joueur. Cette information est conservée uniquement comme **indice de baseline à vérifier**.

Elle ne permet pas de conclure aujourd'hui que :

- les ports historiques sont encore identiques ;
- les opcodes historiques sont encore valides ;
- le framing historique est encore canonique ;
- le handshake/JWT/reprise historique sont inchangés ;
- un bridge ou endpoint WebSocket joueur existe ;
- un client public est compatible.

## Baseline obligatoire avant promotion

La promotion vers `VERIFIED_SERVER_CONTRACT` exige un reçu privé contenant au minimum :

- SHA Git exact du monorepo ;
- tree object exact de `zig-server-v2` ;
- état clean du sous-arbre ;
- version/toolchain Zig ;
- inventaire des handlers/messages à la même révision ;
- tests reproductibles correspondant aux claims publiés.

Les détails sensibles ou propriétaires n'ont pas à être publiés pour fournir cette preuve. Une documentation publique peut exposer seulement le sous-ensemble explicitement approuvé.

## Three.js

Tant qu'aucun endpoint navigateur n'est prouvé, le client Three.js doit rester fail-closed. Il ne doit jamais réutiliser le WebSocket WebAdmin comme canal gameplay ni inventer un endpoint joueur.

## Godot

Classic et VR doivent conserver leur adaptateur de transport abstrait sans socket jusqu'à ce que la baseline Zig exacte soit capturée et le contrat approuvé. L'ancien réseau VR reste `LEGACY_QUARANTINED`.

## Référence publique utilisable aujourd'hui

Pour développer sans dépendre du protocole propriétaire/non épinglé, utilisez [`network-contract.md`](network-contract.md) et `network-intent-v1`, qui définissent l'autorité et des fixtures synthétiques transport-indépendantes sans revendiquer l'interopérabilité live.
