# Référence du catalogue des outils créatifs

La source machine est
[creative-tools-catalog.json](../../../examples/creative-tools-catalog.json),
validée par le
[schéma JSON](../../../schemas/creative-tools-catalog-v1.schema.json).

## Lire une fiche outil

| Champ | Signification |
|---|---|
| `maturity` | preuve publique réelle, prototype, proxy, prévu ou externe |
| `execution` | local, cloud, hybride ou non applicable |
| `pricing_model` | gratuit, achat, abonnement, crédits ou limites, sans prix exact |
| `commercial_use` | autorisé, conditionnel, dépendant du plan/asset/modèle |
| `privacy` | lieu de traitement et frontière des données |
| `ai_training_terms` | conditions d'entraînement applicables ou à vérifier |
| `integration` | direct, conversion nécessaire ou référence uniquement |
| `verified_on` | date de la dernière vérification officielle |

## Statuts Ultimate Odycer

- `executable_public` : source et tests publics disponibles ;
- `prototype_local` : fonction bornée locale ;
- `scaffolding_proxy` : aperçu ou contrat sans chaîne runtime ;
- `planned` : conception sans outil utilisable ;
- `verification_required` : preuve actuelle insuffisante.

Creature, City et Architecture Editor Lite sont `executable_public`, mais leurs
aperçus restent `[Scaffolding / Proxy]`. Les éditeurs complets ne récupèrent pas
ce statut par association.

## Choisir sans se tromper

1. Utilisez `recommendations` pour le domaine visé.
2. Commencez par `default_tool`.
3. Vérifiez plateforme, formats et conversion.
4. Ouvrez le lien officiel de licence ou tarification.
5. Vérifiez aussi chaque asset, modèle et plug-in.
6. Passez au cloud seulement après l'audit confidentialité.

Un lien valide ne prouve pas que les conditions juridiques n'ont pas changé.
Une fiche obsolète doit passer à `verification_required`.
