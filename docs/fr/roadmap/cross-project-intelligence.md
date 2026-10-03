# Plateforme d’intelligence inter-projets

Statut : architecture EXPÉRIMENTALE / expériences bornées.

## Objectif
Réutiliser les capacités éprouvées au moyen de petits contrats sans fusionner les projets en monolithe.

## Établi et expérimental
ÉTABLI : Botte Secrète fournit des mécanismes orientés exécution, fiabilité et preuves dans son périmètre démontré.
EXPÉRIMENTAL : routage Capability Graph, routage Parcimonia, ShadowGraph et fédération SYSTAI inter-projets. Ne pas les présenter comme le comportement d’un plan de contrôle en production.

## Composition cible
Humain -> SYSTAI (interface de projet progressive) -> état/contrats propres au projet -> sélection de capacités candidates -> projet/outil spécialisé -> validation/preuves.

Botte Secrète peut fournir des primitives d’exécution et de preuve. Parcimonia peut fournir des recommandations de coût/calcul lorsqu’elles sont démontrées. Le vocabulaire seul n’élargit aucun de ces rôles.

## Règle ShadowGraph
Ne pas construire un cadre universel par hypothèse. Ne promouvoir des primitives partagées qu’après des preuves inter-domaines.

## Invariants
L’autorité d’un domaine reste dans ce domaine ; les modèles/outils externes utilisent des capacités/politiques déclarées ; les mutations à forte conséquence exigent une approbation ; la provenance et les preuves suivent les sorties ; les contrats partagés emploient des migrations versionnées ; l’historique propre à un produit ne définit pas le périmètre inter-projets.
