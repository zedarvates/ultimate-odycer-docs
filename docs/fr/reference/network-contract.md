# Contrat réseau

Statut : contrat d'autorité public. Les identifiants canoniques de messages,
les layouts binaires et les numeros de version sont `unavailable` tant qu'une
porte de publication de protocole n'est pas passee. Cette page suffit pour
concevoir un client ou un outil sans cloner le serveur non publié.

## Modèle de tick et de coherence

```text
tick client                 tick serveur
  échantillonner l'entrée     consommer les intentions
  envoyer l'intention         valider / simuler
  appliquer le dernier ack    persister l'état requis
  prédire en local            répliquer les diffs
  réconcilier sur diff        jeter les champs non autorisés
```

Règles publiques :

- le tick serveur est autoritaire ;
- les clients peuvent prédire le déplacement pour le confort et doivent
  réconcilier ;
- la réplication est basée sur l'intérêt : un client reçoit ce qu'il a le
  droit de voir ;
- diffs d'état et compression delta sont des optimisations côté serveur, pas
  une licence d'envoyer des snapshots monde complets depuis le client ;
- les cadences exactes restent `unavailable`.

## Familles d'intentions

Un futur protocole DEVRAIT grouper les intentions client vers serveur par
famille plutôt que par moteur :

| Famille | Intention typique | Le serveur doit valider |
|---|---|---|
| Session | login, logout, handoff, reconnect | identité, expiration, appartenance |
| Déplacement | marcher, stopper, sauter, téléport | vitesse, collision, zone, anti-triche |
| Interaction | utiliser, parler, ramasser, échange | portée, propriété, cooldowns |
| Combat | attaquer, lancer, bloquér, annuler | ressources, règles, immunités |
| Parôle | dire, emote, choix de dialogue PNJ | mute, longueur, disponibilité PNJ |
| Inventaire | équiper, déplacer, jeter, consommer | propriété, poids, liaisons |
| Craft / économie | crafter, acheter, vendre, courrier | recettes, fonds, fraude |
| Sync | ack, ping, cible de vue | timing seulement, aucune mutation d'état |

Les noms ci-dessus sont des familles de documentation. Ce ne sont pas des
opcodes publiés. Inventer un paquet binaire à partir de ce tableau serait
incorrect.

## Règles de charge utile

- les modèles JSON peuvent décrire du contenu ; le transport live peut être
  JSON, binaire, ou les deux. L'implémentation non publiée n'est pas impliquée ;
- les nombres de gameplay doivent être typés et à unités explicites dans les
  modèles : `duration_ms`, `distance_m`, `cooldown_seconds` ;
- les clients envoient des intentions et des indices de présentation, jamais
  PV, or ou dons ;
- les champs inconnus doivent etre ignores pour la présentation et refusés
  pour la sécurité ;
- les exemples de documentation n'utilisent que des noms synthétiques.

## Fixture de documentation versionné

La source structurée est
[`schemas/network-intent-v1.schema.json`](../../../schemas/network-intent-v1.schema.json).
Un exemple synthétique se trouve dans
[`examples/network/synthetic-talk-intent.json`](../../../examples/network/synthetic-talk-intent.json).

Ce fixture est `estimated`. Il enregistre la famille, l'intention, des
identifiants d'acteurs synthétiques, une séquence client et une clé
d'idempotence. Ce n'est pas un paquet capturé ni un opcode publié.

Les consommateurs doivent :

- refuser une `schema_version` inconnue ;
- refuser `hp`, `gold`, `damage`, `speed`, dons, opcodes, hôtes et ports ;
- n'utiliser que des identifiants `*_demo_*` ;
- traiter une forme JSON identique comme de la documentation, pas comme une
  compatibilité serveur.

Validez l'exemple avec les contrôles du dépôt. L'assistant dédié est
`scripts/network_intent.py`.

JSON illustratif, désormais appuyé par le fixture v1 :

```json
{
  "schema_version": "network-intent-v1",
  "family": "talk",
  "intent": "talk",
  "actor_id": "player_demo_01",
  "target_id": "npc_demo_gatekeeper_01",
  "client_seq": 42
}
```

Le serveur peut repondre par un événement accepté, une intention refusée ou
un diff d'état. Le client ne doit pas réessayer une mutation refusée comme
si elle avait réussi.

## Timeouts, retries et anti-triche

- un ack manquant n'autorise pas à figer la prédiction locale ;
- les retries doivent être idempotents par séquence client ou identifiant
  serveur ;
- des intentions dupliquées ne doivent pas dupliquer or, objets ou dégâts ;
- un déplacement trop rapide, qui ignore la collision ou montre une entropie
  impossible est refusé ;
- des limites de débit s'appliquent par session et par famille ;
- le TLS est attendu hors boucle locale. Les fixtures locales utilisent
  encore des identifiants synthétiques.

Les seuils exacts, fenêtres d'entropie et épingles de certificats restent
`unavailable`.

## Porte de compatibilité

Les starters clients publics marquent actuellement l'alignement serveur Zig
comme bloqué. Un client tiers est non supporté tant que la preuve listée
dans ces dépôts n'existe pas. Voir
[l'architecture serveur](../explanation/server-architecture.md).
