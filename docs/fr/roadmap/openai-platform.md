# Intégration de la plateforme OpenAI — Feuille de route expérimentale

Statut : EXPÉRIMENTAL / planification. Aucune dépendance de production ni disponibilité actuelle d’un fournisseur n’est sous-entendue.

## Périmètre
Adaptateurs optionnels vers OpenAI pour des cas d’usage choisis de l’écosystème Obolune/Ultimate Odycer. Ils ne définissent pas le cœur multi-jeux et ne rendent pas OpenAI obligatoire.

## Règle d’architecture
DÉCIDÉ : les intégrations propres à un fournisseur restent remplaçables et ne peuvent devenir une autorité de domaine irréversible. La disponibilité officielle, les permissions et les contrôles de sécurité du fournisseur sont respectés.

## Expérience cible
Créateur/joueur -> interface de projet SYSTAI (progressive) -> contrats de transfert/capacité indépendants du fournisseur -> services spécialisés de jeu/création.
ChatGPT, Work, les futurs Dots lorsqu’ils sont officiellement disponibles, les modèles locaux et autres exécuteurs autorisés sont des fournisseurs/adaptateurs candidats.

Le routage des capacités/coûts via Botte Secrète/Parcimonia est EXPÉRIMENTAL et non un comportement de production établi.

## Chantiers
OAI-01 contrats de passerelle indépendants du fournisseur ; OAI-02 pont d’événements ; OAI-03 surface d’agent web bornée ; OAI-04 fixture d’intégration ChatGPT ; OAI-05 expérience fantôme Game Master/World Director ; OAI-06 expérience d’identité optionnelle ; OAI-07 adaptateurs commerciaux optionnels ; OAI-08 pont de services créateur.

## Précision OAI-05
PROPOSÉ/EXPÉRIMENTAL : un Game Master/World Director de haut niveau peut être évalué pour la planification et coordination narrative clairsemées. Cela n’établit ni que ONE/NeuroCore possède actuellement toutes les actions rapides des PNJ, ni que l’architecture d’agents hébergés est adoptée.

## Hors périmètre
Pas de remplacement de l’autorité du domaine ; pas d’écriture LLM directe dans l’état faisant autorité ; pas de connexion OpenAI obligatoire ; pas d’achat ou publication automatique ; pas de contournement de fonctions fournisseur indisponibles ; pas d’hypothèse que les prototypes sont intégrés.
