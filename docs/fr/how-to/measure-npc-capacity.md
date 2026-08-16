# Mesurer la capacité PNJ d'un home lab

Ce guide transforme un banc réel en capacité de planification prudente.

## 1. Figer la charge

Notez avant le test :

- matériel, RAM, refroidissement et système ;
- modèle, quantification, runtime et version ;
- longueur du contexte et longueur maximale de sortie ;
- inclusion ou exclusion de STT et TTS ;
- nombre de flux concurrents ;
- texte ou graine permettant de reproduire les requêtes.

Ne comparez pas deux appareils avec des charges différentes.

## 2. Mesurer la durée bout en bout

Exécutez au moins 100 courtes réponses après échauffement. Conservez chaque durée
et calculez la médiane et le p95. Si l'audio fait partie de l'expérience joueur,
incluez sa préparation dans la durée.

Utilisez le p95 comme `reply-seconds` pour une planification prudente. Si le p95
est indisponible, marquez-le `unavailable` et ne remplacez pas cette absence par
la moyenne ou par zéro.

## 3. Calculer la capacité

Lancez le calculateur uniquement avec le nombre de flux réellement testés :

```powershell
rtk python scripts/npc_capacity_estimator.py `
  --reply-seconds <p95-bout-en-bout> `
  --npc-interval-seconds <intervalle-minimal-par-PNJ> `
  --utilization 0.5 `
  --streams <flux-prouvés> `
  --basis measured
```

La formule est :

```text
réponses planifiées/minute = flux × 60 / durée × utilisation
PNJ actifs = réponses planifiées/minute × intervalle PNJ / 60
```

## 4. Enregistrer le résultat

Copiez les données dans un document conforme à
[`npc-benchmark-v1.schema.json`](../../../schemas/npc-benchmark-v1.schema.json).
Utilisez [`estimated-esp32-s3.json`](../../../examples/benchmark-results/estimated-esp32-s3.json)
comme exemple de structure, pas comme preuve matérielle.

## 5. Valider la décision

Un appareil est acceptable seulement si :

- le p95 reste sous la limite de l'expérience visée ;
- la qualité passe les contrôles définis avant le banc ;
- les erreurs et replis déterministes sont comptés ;
- la capacité garde une marge sous la charge attendue ;
- le coût complet est meilleur que conserver l'existant.

Une mesure de débit ne prouve ni la qualité du dialogue, ni la sécurité, ni la
capacité d'un serveur de production.
