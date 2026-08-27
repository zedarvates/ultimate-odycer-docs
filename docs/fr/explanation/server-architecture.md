# Architecture serveur

Statut : `decision` pour les frontières publiques ; les détails
d'implémentation sont `unavailable` car le serveur Zig canonique n'est pas
publié.

Un developpeur indépendant peut concevoir contre le contrat public. Il ne
peut pas cloner un serveur de production à partir de cette page.

## Frontière publique

Le serveur est la seule source de vérité pour :

- l'identite de compte, de personnage et de session ;
- le déplacement, le combat, l'inventaire, l'artisanat et l'économie ;
- l'appartenance aux zones, instances et la visibilité ;
- les decisions PNJ qui changent l'état du monde ;
- la persistance et la reprise après reconnexion.

Les starters clients publics enregistrent déjà cette règle comme décision
d'architecture acceptée. Une page de documentation ne peut pas l'affaiblir.

## Modules logiques

```text
                +------------- serveur autoritaire ----------------+
auth / session | identité, jetons, handoff de royaume             |
monde          | zones, instances, intérêt, réplication           |
simulation     | déplacement, combat, inventaire, craft, quêtes   |
pnj            | perception, comportement, expression validée     |
persistance    | personnages, monde, économie, audit              |
sûreté         | validation, rate limits, anti-triche, TLS        |
                +-------------------------------------------------+
```

Ces noms sont logiques. Ils ne forment ni une liste de crates publiée, ni un
layout binaire, ni une surface d'API. Les noms de modules des dépôts privés
ne doivent pas être copiés ici comme un SDK public.

## Ce qu'un futur protocole public doit exposer

Avant qu'un client tiers puisse se connecter, un contrat publié doit nommer :

- la version de protocole et la négociation ;
- la séquence d'authentification et de handoff de royaume ;
- les identifiants de messages, le cadrage et la sérialisation ;
- les règles autoritaires d'identité, déplacement, combat et inventaire ;
- les attentes de sécurité transport et de certificats ;
- une fixture de boucle locale synthétique sans point de production.

Cette preuve est actuellement bloquée dans les dépôts clients publics.
Tant qu'elle n'existe pas, la compatibilité serveur est non supportée.

## Opérations encore non publiées

Les éléments suivants sont nécessaires à un vrai MMO, mais ils ne sont pas
documentés comme runbook public dans ce dépôt :

- déploiement multi-serveurs et répartition de charge ;
- affectation de shards et failover ;
- TLS de production, secrets et rotation de certificats ;
- Prometheus, Grafana, ou toute pile hébergée nommée ;
- sauvegarde et restauration de données de production ;
- CI/CD d'un monde vivant.

Un opérateur home lab peut quand même conserver des journaux locaux, des
métriques PNJ et des services en boucle locale fail-closed. Voir
[exploiter un home lab](../how-to/operate-a-home-lab.md).

## Pages liées

- [Vue d'architecture](architecture-overview.md)
- [Contrat réseau](../reference/network-contract.md)
- [Pipeline d'agents PNJ](npc-agent-pipeline.md)
