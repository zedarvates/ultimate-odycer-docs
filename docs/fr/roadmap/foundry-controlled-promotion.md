# Foundry — amélioration et promotion contrôlées

Statut : orientation de gouvernance DECIDED / implémentation EXPERIMENTAL.

## Finalité
Permettre aux skills, outils, workflows, pipelines et candidats de routage de progresser par des expériences mesurées, sans laisser un candidat redéfinir ses propres critères de succès, affaiblir ses garde-fous ou se promouvoir lui-même.

## Cycle de vie
CANDIDATE -> BENCHMARKED -> REVIEW_READY -> APPROVED/REJECTED -> ADOPTED -> éventuellement ROLLED_BACK.

## Référence initiale
Toute affirmation d'amélioration exige une référence initiale exacte et comparable : versions, charge ou jeu de données, métriques, environnement et preuves. Les changements substantiels du benchmark invalident les comparaisons directes jusqu'à leur réconciliation.

## Preuves multidimensionnelles
Comparer qualité, erreurs à forte confiance, abstention, latence, coûts et calcul, maintenance et métriques de conséquences pertinentes. Aucun score pondéré universel ni vainqueur automatique parce qu'il est le moins cher ou le plus rapide.

## Séparation des responsabilités
Les changements de politique de sécurité, d'autorité ou d'autonomie exigent un proposant et un approbateur distincts. Les agents peuvent préparer les différences de politique et les tests ; ils ne peuvent pas approuver eux-mêmes l'affaiblissement des contrôles.

## Adoption
Privilégier le mode d'observation parallèle ou le déploiement progressif lorsque cela s'applique. Consigner la version précédente, la compatibilité et la migration, le retour arrière et les périmètres touchés. Une adoption sans retour arrière possible est explicitement à fortes conséquences.

## Après adoption
Mesurer le comportement réel après adoption. Les preuves de benchmark ne garantissent pas un comportement équivalent en production ; une dérive ou une régression rouvre la revue et peut déclencher une proposition de retour arrière.

## Rôle humain
Les compromis architecturaux, de politique et à conséquences restent arbitrés par l'humain au moyen de Decision Briefs.
