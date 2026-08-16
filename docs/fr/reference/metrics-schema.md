# Référence des métriques PNJ

La source structurée est
[`schemas/npc-benchmark-v1.schema.json`](../../../schemas/npc-benchmark-v1.schema.json).

## Statut d'une information

| Valeur | Signification |
|---|---|
| `observed` | Résultat réellement mesuré avec l'environnement décrit |
| `estimated` | Scénario calculé à partir d'hypothèses explicites |
| `decision` | Choix de projet séparé des données qui le motivent |
| `unavailable` | Valeur non mesurée ou inconnue |

## Groupes obligatoires

| Groupe | Contenu |
|---|---|
| `hardware` | Appareil, CPU, RAM, stockage et refroidissement utiles |
| `software` | Outil, version, modèle, quantification et runtime |
| `workload` | Contexte, sortie, audio, flux et cadence PNJ |
| `measurements` | Échantillons, médiane, p95, débit et erreurs |
| `capacity` | Marge, réponses/minute, PNJ actifs et politique de file |
| `limitations` | Éléments non prouvés par le résultat |

## Règles

- `supported_active_npcs` est un calcul de planification.
- `streams` est le nombre de flux effectivement testés, pas le nombre de PNJ.
- `sample_count` doit être présent pour un résultat `observed`.
- Une métrique absente utilise la chaîne `unavailable` lorsqu'elle est autorisée.
- Les durées sont en secondes et les tailles en octets.
- La date et la version doivent permettre de distinguer deux campagnes.
- Aucun champ libre ne doit contenir de secret ou de donnée client.

## Compatibilité

Les consommateurs doivent refuser une version de schéma inconnue. Une extension
ne doit pas modifier la signification d'un champ existant.
