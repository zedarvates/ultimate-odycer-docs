# Plateforme OpenAI — Plan d’exécution

Début : 2026-10-01

## Semaine 1 — fondations
- Aligner tous les contrats sur SYSTAI comme orchestrateur tourné vers les créateurs ; ne pas créer de super-agent concurrent.
- Inventorier les contrats existants de World Compiler et Tools Suite avant d’ajouter des schémas.
- Ébaucher le Game DNA/Design Graph, l’extension Universal Entity et le Tool Capability Registry à partir des travaux existants sur les modèles et Protobuf.
- Définir les liens du Knowledge Graph, les budgets, la provenance et les migrations.

### Fondations propres à OpenAI
- Définir l’enveloppe de capacité de l’Agent Gateway : identifiant, schéma d’entrée/sortie, périmètre d’autorisation, plafond de coût, classe de latence, conséquence, preuve et repli.
- Inventorier les interfaces Zig/Tools/Web/NeuroCore existantes.
- Ébaucher le vocabulaire d’événements et les permissions en lecture seule.
- Ajouter des feature flags indépendants du fournisseur.
- Définir la télémétrie : fournisseur, jetons/calcul, latence, succès du cache, repli, confiance et résultat.

Preuve de sortie : les schémas et exemples se valident sans affirmation d’exécution.

## Semaine 2 — prototypes bornés
- Pont d’événements : rejouer des événements synthétiques de serveur/monde.
- Three.js : outils d’agent en lecture seule pour les métadonnées d’état et de navigation.
- Maquette d’intégration ChatGPT : requêtes de personnages/serveurs à partir de fixtures.
- Banc d’essai de routage Parcimonia : niveaux déterministe/kNN/micro/local/hébergé.

Preuve de sortie : tests hors ligne et rapport coût/latence.

## Semaine 3 — expérience NeuroCore
- Ajouter un adaptateur fantôme Game Master/World Director.
- Fournir des événements et résumés du monde, recevoir des propositions typées.
- Ne jamais modifier l’état faisant autorité.
- Comparer qualité et coût des propositions hébergées à une référence locale.
- Consigner conséquences, abstentions et replis.

Preuve de sortie : benchmark fantôme reproductible.

## Jalons ultérieurs
Les travaux d’identité, de commerce et de place de marché ne commencent qu’après stabilisation suffisante des API/conditions publiques et validation des revues de sécurité et de confidentialité.

## Ordre Kanban
READY : OAI-01 contrats de passerelle ; OAI-02 vocabulaire d’événements.
NEXT : OAI-03 outils web en lecture seule ; OAI-04 prototype ChatGPT sur fixtures.
EXPERIMENT : OAI-05 Game Master fantôme.
WATCH : OAI-06 identité ; OAI-07 commerce/place de marché.

## Kanban de la plateforme créateur
READY : CREATOR-01 Game DNA/Design Graph ; inventaire CREATOR-03 Tool Capability Registry.
NEXT : extension CREATOR-02 Universal Entity ; CREATOR-04 Knowledge Graph ; CREATOR-05 Constraint/Budget Engine.
THEN : CREATOR-06 Provenance/Rights Ledger ; CREATOR-08 Build Evidence Graph ; migrations CREATOR-09.
EXPERIMENT : CREATOR-07 Synthetic Playtest Lab.
UX : CREATOR-10 explicabilité SYSTAI/revue des hypothèses.
