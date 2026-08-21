# Vue d'architecture

Statut : `decision`. Cette page décrit l'architecture publique d'Ultimate
Odycer. Ce n'est pas un dump du serveur Zig non publié et elle ne certifié
aucun déploiement en cours.

## Modèle d'autorité

```text
intention du joueur
    |
    v
couche de présentation client
    |  la prédiction locale est optionnelle et jetable
    |  jamais autoritaire pour PV, or, inventaire, vitesse ou accès
    v
transport (TLS attendu hors boucle locale)
    v
serveur autoritaire
    |  authentifie l'identité
    |  valide l'intention contre règles, cooldowns et état du monde
    |  applique les conséquences
    |  persiste ce qui doit survivre à une reconnexion
    v
diff d'état / mise à jour de présentation
    v
clients intéressés, nœuds d'expression PNJ et outils
```

Le serveur reste autoritaire pour l'identité, le déplacement, le combat,
l'inventaire, la progression et l'économie. Cette règle est déjà acceptée
dans les starters clients publics. Un client, un modèle JSON ou une sortie
LLM qui contredit le serveur est refusé.

## Réplication, zones et shards

```text
                +------------------ royaume / monde ----------------+
                |                                                   |
   login / auth |   zone A          zone B          instance I      |
   et handoff   |  (intérêt)       (intérêt)       (copie bornée)   |
                |                                                   |
                +------------------ persistance --------------------+
```

Règles publiques :

- un joueur se connecte par authentification et handoff de royaume, pas en
  écrivant l'état du monde en local ;
- une zone ou un ensemble d'intérêt limite ce qu'un client peut voir ou
  toucher ;
- une instance est une copie bornée de contenu, pas une seconde source de
  vérité ;
- le sharding, s'il existe, est une décision de capacité. Il ne déplace pas
  l'autorité vers le client ;
- les cartes de shards, rayons d'intérêt et budgets d'instance restent
  `unavailable` tant qu'une version de protocole publique n'est pas publiée.

## Pipelines

### Pipeline réseau

Voir le [contrat réseau](../reference/network-contract.md). Les intentions
vont du client vers le serveur. Les diffs autoritaires vont du serveur vers
les clients intéressés. Les retries et timeouts ne rejouent jamais une
mutation non validée.

### Pipeline PNJ / LLM

Voir le [pipeline d'agents PNJ](npc-agent-pipeline.md) et
[l'architecture hybride](hybrid-architecture.md). Le serveur valide d'abord
l'intention. Le modèle n'exprime qu'un paquet déjà accepté.

### Pipeline client VR / rendu

Voir [l'architecture client](client-architecture.md). Le chargement de
scènes, le LOD, l'entrée OpenXR et la physique locale sont de la
présentation. Une collision qui donne du loot, des dégâts ou de la vitesse
ne l'est pas.

### Pipeline assets / modèles

Voir [utiliser les modèles JSON](../how-to/use-json-templates.md). Les
créateurs versionnent le contenu dans le registre public. Les consommateurs
épinglent un SHA-256. Le serveur valide encore les valeurs de gameplay.

## Home lab versus production

| Couche | Home lab | Staging auto-hébergé | Production |
|---|---|---|---|
| Public | un opérateur, données synthétiques | opérateurs isolés, joueurs synthétiques | frontière commerciale non publiée |
| Autorité | toujours côté serveur | toujours côté serveur | toujours côté serveur |
| LLM | boucle locale, budgété, fail-closed | identique, plus rate limits | non publié |
| Supervision | journaux locaux et métriques PNJ | journaux structurés, notes de capacité | non publié |
| Preuve | validation docs et bancs locaux | fixtures nommées, sans données de production | non revendiquée ici |

Un banc home lab réussi ne prouvé ni le CCU de production, ni le confort VR,
ni le failover multi-serveurs. Ces éléments restent `unavailable` ici.

## Pages liées

- [Vue d'ensemble de l'écosystème](ecosystem-overview.md)
- [Architecture serveur](server-architecture.md)
- [Architecture client](client-architecture.md)
- [Pipeline d'agents PNJ](npc-agent-pipeline.md)
- [Systèmes de gameplay](../reference/gameplay-systems.md)
