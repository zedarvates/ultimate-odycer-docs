# Foundry — clôture du travail et des conversations

Statut : orientation DECIDED / implémentation EXPERIMENTAL.

## Principe
L'achèvement du travail et l'archivage du chat ou de l'interface sont distincts.

Machine à états :
ACTIVE -> LIKELY_FINISHED -> CLOSURE_CHECK -> ARCHIVE_READY -> ARCHIVED
Un élément clos ou archivé peut devenir REOPENED.

L'inactivité seule n'implique jamais l'achèvement.

## Conditions de clôture
Avant ARCHIVE_READY :
- l'objectif ou le résultat du travail est achevé ou intentionnellement abandonné ;
- les preuves et le point de reprise sont capturés ;
- une Closure Capsule existe ;
- aucune décision humaine ni aucun conflit ne reste non résolu ;
- aucune attente de renouvellement, différée, externe, liée au runner, au fournisseur ou à une surveillance ne reste cachée dans la conversation ;
- chaque tâche résiduelle est transférée vers Work Graph, Kanban, une file de renouvellement ou une surveillance ;
- les preuves critiques périmées sont résolues ou bloquent explicitement la clôture.

## Closure Capsule
Elle conserve l'objectif, le résultat, les décisions, les changements, les preuves, les coûts, les artefacts, les enseignements, les références canoniques, le travail résiduel transféré et les instructions exactes de reprise.

## Conservation
Prévoir un délai de grâce, un état épinglé ou « ne jamais archiver automatiquement » et des motifs explicites de conservation. Le silence n'est qu'un signal faible.

## Trois niveaux d'automatisation
1. **Clôture automatique** — Foundry peut clore son propre Work Graph lorsque les conditions sont prouvées.
2. **Prêt à archiver** — la conversation peut être archivée sans perdre de travail.
3. **Archivage automatique de l'interface** — uniquement via un adaptateur officiellement disponible, explicitement activé par l'utilisateur et permis par les autorisations effectives.

Aucune émulation de l'interface ou du navigateur ne sert à contourner des commandes d'archivage indisponibles.

## Réouverture
Reconstruire le contexte depuis la Closure Capsule et les sources et preuves canoniques actuelles ; marquer les anciennes hypothèses et preuves comme périmées lorsque nécessaire, plutôt que de traiter le contexte archivé comme une vérité actuelle.
