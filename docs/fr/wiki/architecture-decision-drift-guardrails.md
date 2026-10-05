# Garde-fous contre la dérive des décisions d’architecture

Objectif : empêcher les propositions, le contexte historique et les expériences de devenir silencieusement la vérité du projet.

## Libellés épistémiques
Chaque affirmation architecturale DEVRAIT appartenir à l’une de ces classes :
- **ÉTABLI** — frontière vérifiée existante ou décision humaine explicite.
- **HISTORIQUE** — vrai sur l’origine ou l’intention passée du projet ; pas automatiquement dans le périmètre actuel.
- **DÉCIDÉ** — direction explicitement acceptée ; l’implémentation peut rester à faire.
- **PROPOSÉ** — idée de l’assistant ou de l’équipe en attente de validation.
- **EXPÉRIMENTAL** — implémentation/preuve bornée ; pas une architecture de production.
- **DÉPRÉCIÉ/CORRIGÉ** — interprétation antérieure qui ne doit plus guider le travail.

## Corrections issues de la discussion du 2026-09-30
1. **CORRIGÉ :** Obolune n’est ni le registre JSON/modèles ni son autorité. GitHub/UltOd JSON Template Registry restent canoniques. Obolune est l’expérience tournée vers studio, édition, vitrine et plateforme.
2. **CORRIGÉ :** le contexte historique d’Ultimate Odycer (vie planétaire, forte personnalisation, MMORPG, mode scientifique) ne doit pas être généralisé à Obolune ni au cœur de création multi-jeux. Obolune accepte plusieurs styles et genres.
3. **CORRIGÉ :** les outils et la plateforme de création sont une capacité inter-jeux de l’écosystème Obolune/Odycer, pas une redéfinition de l’identité d’Ultimate Odycer.
4. **CORRIGÉ :** ne pas inventer un Flora Editor concurrent. Réutiliser/localiser le travail Plant Editor existant avant de nommer ou créer un nouvel éditeur.
5. **CORRIGÉ :** ne pas recréer World Compiler ni le JSON Template Registry mature. Étendre uniquement par adaptateurs/contrats lorsque cela est justifié.
6. **CORRIGÉ :** Botte Secrète est établie comme couche d’exécution, fiabilité et preuve. Les extensions de routage/orchestration restent EXPÉRIMENTALES jusqu’à preuve distincte ; ne pas les présenter comme production établie.
7. **CORRIGÉ :** le rôle élargi d’orchestration studio/créateur de SYSTAI est une direction DÉCIDÉE dans cette discussion, mais l’implémentation reste progressive/expérimentale. ChatGPT/Dots/les modèles locaux sont des fournisseurs ou exécuteurs candidats, pas SYSTAI.
8. **CORRIGÉ :** les intégrations OpenAI Dots/Work doivent suivre disponibilité et permissions officielles. Aucun adaptateur local ne peut simuler une fonction fournisseur indisponible pour contourner les restrictions.
9. **DÉCIDÉ :** les flux créateurs ne privilégient pas d’abord la génération IA. Les productions manuelle, locale, cloud, par abonnement, par collaborateur et hybride sont équivalentes ; les originaux humains modifiables peuvent être protégés.
10. **DÉCIDÉ :** la supervision humaine reste intentionnelle. L’automatisation doit maximiser le travail utile entre les décisions humaines, pas supprimer l’autorité produit, créative et commerciale.

## Règles anti-dérive
- Le contexte historique ne change jamais le périmètre actuel sans nouvelle décision explicite.
- Un composant proposé ne devient pas « existant » parce qu’un schéma ou une issue a été créé.
- Une PR en brouillon prouve uniquement son contenu et ses tests bornés, pas l’adoption ni l’intégration en production.
- Les noms n’établissent pas l’identité : rechercher les projets et outils existants avant de créer un nouveau composant nommé.
- Les abstractions inter-projets exigent des preuves issues de plusieurs domaines avant promotion.
- Les fonctions propres à un genre appartiennent à des modules composables, pas au cœur neutre.
- Séparer identité produit, identité studio, plateforme créateur, infrastructure et registre open source.
- Quand une correction utilisateur contredit l’architecture proposée par l’assistant, consigner la correction et mettre à jour les documents dépendants au lieu de rationaliser l’ancienne proposition.
