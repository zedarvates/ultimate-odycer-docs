# Connecter le template Three.js 2.5D à un serveur local

Statut : **fixture synthétique validée ; compatibilité Zig live non prouvée**.

Le client Three.js possède maintenant un `NetworkClient` fail-closed et un gate synthétique vert. Cette preuve reste `SYNTHETIC_FIXTURE_ONLY`.

## Réalité du transport

La documentation serveur actuelle décrit login/jeu en **TCP binaire brut**. Cette description doit encore être rattachée à une baseline Zig exacte avant d'être appelée contrat canonique vérifié.

Un navigateur ne doit donc pas supposer l'existence d'un WebSocket joueur. Deux chemins seulement sont acceptables avant un vrai E2E :

1. pont/passerelle WebSocket ↔ TCP documenté et audité ;
2. endpoint WebSocket officiel distinct, ajouté et prouvé côté serveur.

Le WebSocket WebAdmin n'est pas un canal gameplay.

## Ce qui est déjà prouvé

La fixture synthétique valide notamment :

- lifecycle de connexion ;
- handshake/auth synthétiques ;
- mouvement borné ;
- trames invalides et surdimensionnées ;
- NaN/Infinity/overflow ;
- état fail-closed ;
- réception de positions autoritaires synthétiques.

Cela ne prouve ni TCP Zig, ni bridge, ni endpoint joueur, ni auth production.

## Prochaine preuve

Avant `REAL_SERVER_E2E`, capturer :

- SHA/tree/toolchain exacts de `zig-server-v2` ;
- contrat de transport réellement présent à cette révision ;
- bridge/endpoint exact si navigateur ;
- révision Three.js exacte.

Le scénario live minimal sera : auth → realm/handoff → spawn → movement intent → update autoritaire → second client observe → disconnect/reconnect, avec tests négatifs.

Ne copiez jamais les opcodes/framing documentés dans le client public comme s'ils étaient vérifiés tant que la baseline Zig P0 n'est pas épinglée.
