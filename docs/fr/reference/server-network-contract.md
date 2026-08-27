# Vue d'ensemble du contrat réseau du serveur

Statut : **documenté à partir des décisions d'implémentation, compatibilité
non validée**.

Cette page décrit la surface réseau du serveur Zig canonique telle qu'elle est
réellement implémentée dans son code source actuel. Elle existe pour que les
templates de client, y compris les templates web, puissent documenter ce
qu'ils doivent prendre en charge avant de revendiquer une interopérabilité.
Décrire le format filaire ne valide **ni** un client, **ni** un moteur,
**ni** un déploiement.

## Réalité du transport

Les services canoniques parlent **TCP binaire brut**, pas WebSocket ni
WebTransport :

- Service de login : TCP, port configuré 2106 par défaut.
- Service de jeu : TCP, port configuré 7777 par défaut.
- WebAdmin : HTTP plus WebSocket sur son propre port, 8082 par défaut,
  uniquement pour les tableaux d'administration. Ce n'est pas le canal de jeu
  des joueurs.

Un navigateur ne peut pas se connecter directement aux points TCP du login ou
du jeu. Tout client web exige donc soit un pont/passerelle documenté, soit un
nouveau point de terminaison WebSocket officiel. Tant que l'un des deux
n'existe pas et n'est pas documenté, un template MMORPG basé navigateur n'est
**pas compatible** avec le serveur canonique. Cela correspond à la règle
fail-closed du périmètre du template Three.js.

## Format de trame

Tous les entiers sont en gros-boutiste (big-endian). Chaque message utilise la
même enveloppe :

```text
[4B longueur_totale][2B opcode][payload]
```

- `longueur_totale` compte tout ce qui la suit : 2 octets d'opcode plus le
  payload.
- Les opcodes sont des valeurs u16 issues du registre partagé des messages.
- La boucle d'événements de jeu rejette les trames dont la longueur déclarée
  dépasse 256 Kio.
- Les opcodes inconnus reçus sur le socket de jeu sont journalisés puis
  ignorés sans fermer la connexion.

## Flux de session

1. Création de compte ou enregistrement invité facultatifs sur le service de
   login.
2. Le login sur le service de login renvoie un jeton de session JWT.
3. Liste des royaumes, puis sélection de royaume, qui renvoie l'hôte et le
   port de jeu annoncés.
4. Connexion au service de jeu avec un handshake portant le jeton JWT.
5. Listing des personnages, création, puis sélection.
6. Sélection du spawn dans le monde, puis jeu normal.

### Opcodes clés

| Opcode | Nom | Direction | Rôle |
|---|---|---|---|
| 1 / 2 | handshake requête/réponse | C<->S | Vérification de version, admission JWT |
| 9 | time sync | C<->S | Écho des millis client sur 8 octets, retour millis serveur |
| 10 / 11 | login requête/réponse | C<->S | Identifiants entrants, JWT sortant |
| 20 | character create | C->S | Nom, race, classe de départ |
| 22 / 23 | character select/list | C->S | Sélection par identifiant base ; résumés bornés |
| 30 | position update | C->S | 12 octets : trois coordonnées float32 |
| 80 | entity update | S->C | Lot de réplication delta |
| 205-208 | realm list/select | C<->S | Découverte de shard et cible de handoff |
| 253 / 254 | heartbeat | C<->S | Keepalive avec heure serveur et intervalle de tick |
| 255 | error message | S->C | Erreur lisible encadrée |
| 575 / 576 | guest register | C<->S | Création de compte d'essai sans e-mail |
| 580 | world spawn select | C<->S | Allowlist de spawn vérifiée par nonce par monde |

Le registre complet contient plusieurs centaines d'opcodes couvrant combat,
inventaire, échange, guildes, quêtes, logement, enchères, poses VR, etc. Un
nouveau travail client doit commencer par le sous-ensemble ci-dessus ; le reste
suit les mêmes règles d'enveloppe.

## Détail du handshake

Payload de requête pour l'authentification JWT (type 2) :

```text
[1B version_len][chaîne de version][1B capabilities]
[1B tls_required][1B auth_type][2B token_len][jeton JWT]
[32B hash de manifeste d'assets, seulement si le serveur l'attend]
```

- Les versions antérieures à 1.0.0 sont rejetées.
- Le type 0 (sans authentification) est toujours refusé.
- Le type 1 (mot de passe sur le socket de jeu) est déprécié ; le client doit
  dabord passer par le service de login.
- Quand le serveur exige TLS, une connexion en clair échoue au handshake.
- Réponse de succès : [1B success=1][8B player_id][2B token_len=0].
- Réponse d'échec : [1B success=0][4B error_len][texte d'erreur].

Après un handshake réussi, le serveur pousse un jeton de reprise de session
(opcode 95) sous forme de 64 caractères hexadécimaux, utilisable une seule fois
pour reprendre une session interrompue.

## Payloads de login et de comptes

- Requête de création de compte (opcode 5) :
  `[1B username_len][username][1B password_len][password]` suivie, en réponse à
  un défi CAPTCHA, de
  `[1B challenge_len][challenge][1B answer_len][answer]`.
- Le serveur peut répondre avec le code de statut 2 signifiant qu'un CAPTCHA
  mathématique est requis ; l'identifiant et la question du défi voyagent dans
  la réponse.
- Requête de login (opcode 10) :
  `[1B username_len][username][1B password_len][password]`.
- Réponse de succès de login :
  `[1B success=1][8B player_id][2B token_len][jeton JWT]`.
- L'enregistrement invité (opcode 575) ajoute une valeur de jours d'essai sur
  4 octets et n'exige jamais de CAPTCHA ni de licence ; les comptes sont
  plafonnés (plafond de niveau, expiration).

Les mots de passe sont hachés côté serveur avec Argon2id ; ils n'apparaissent
jamais dans les réponses. La possession de licence est vérifiée en base avant
l'émission d'un jeton, et le mode maintenance bloque à la fois le login et le
handshake.

## Lot de réplication (opcode 80)

```text
[2B nombre_entités]
répété nombre_entités fois :
    [4B taille_delta][delta]
delta :
    [8B entity_id][1B nb_champs]
    répété nb_champs fois :
        [1B id_champ][4B valeur gros-boutiste]
```

Les identifiants de champs actuellement émis comprennent la position X/Y/Z
(1-3), la vélocité X/Z (4, 6), la rotation Y (7) et la santé (10). Les valeurs
de position et de rotation sont des float32 reinterpretés ; la santé est un
compteur entier non signé. Un client interpole entre les lots ; il ne doit
jamais extrapoler l'autorité.

## Règles d'autorité

L'identité, le rôle, l'état de licence, l'inventaire, l'or, la santé, la
vitesse et les résultats de mouvement sont décidés uniquement côté serveur.
- Les rôles envoyés par le client sont traités comme des indications non
  fiables et remplacés par la valeur en base.
- Les mises à jour de position sont validées contre les bornes du monde et des
  contrôles anti-triche avant acceptation.
- Le placement au spawn provient des tables de spawn côté serveur ; les clients
  choisissent parmi des mondes allowlistés avec un nonce, jamais des
  coordonnées arbitraires.

## Preuves de compatibilité encore manquantes

- Aucun point de terminaison WebSocket ou WebTransport officiel n'existe
  aujourd'hui dans le serveur canonique.
- Aucune spécification de pont/passerelle n'a été publiée.
- Aucun client navigateur n'a réalisé de fixture loopback contre ces binaires.

Tant que ces trois points n'évoluent pas avec des preuves nommées, cette page
reste une description du serveur, pas la preuve d'une compatibilité client.
