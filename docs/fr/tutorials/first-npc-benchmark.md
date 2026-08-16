# Réaliser un premier banc de capacité PNJ

Ce tutoriel vous apprend à transformer une durée de réponse en capacité de
planification. Vous n'avez besoin ni d'un serveur Ultimate Odycer ni d'un LLM :
le premier passage utilise un scénario synthétique.

## Résultat attendu

À la fin, vous saurez produire un résultat JSON qui distingue :

- les réponses que le service peut calculer par minute ;
- la marge conservée pour les pointes de charge ;
- le nombre de PNJ actifs planifiables ;
- le nombre de flux réellement utilisé.

## Prérequis

- Python 3.11 ou plus récent ;
- une copie locale de ce dépôt ;
- un terminal ouvert à la racine du dépôt.

## 1. Vérifier la documentation

Sous PowerShell :

```powershell
rtk python scripts/validate_docs.py
```

La commande doit terminer par `validation: ok`.

## 2. Définir le scénario

Nous utiliserons les hypothèses suivantes :

- une courte réponse demande 1,7 seconde ;
- un PNJ parle au maximum une fois toutes les 120 secondes ;
- un seul flux d'inférence est disponible ;
- le planificateur ne consomme que 50 % de la capacité théorique.

Ces nombres sont `estimated`. Ils ne deviennent pas `observed` parce que le
calculateur les accepte.

## 3. Calculer la capacité

```powershell
rtk python scripts/npc_capacity_estimator.py `
  --reply-seconds 1.7 `
  --npc-interval-seconds 120 `
  --utilization 0.5 `
  --streams 1 `
  --basis scenario
```

Le résultat doit notamment contenir :

```json
{
  "basis": "scenario",
  "planned_replies_per_minute": 17.647,
  "supported_active_npcs": 35,
  "queue_policy": "serialize_per_stream"
}
```

Le résultat signifie que 35 PNJ peuvent demander une courte réponse toutes les
deux minutes dans ce scénario. Il ne signifie pas que 35 modèles fonctionnent en
parallèle.

## 4. Tester votre propre rythme de jeu

Pour un monstre qui grogne au maximum toutes les cinq minutes, remplacez
`--npc-interval-seconds 120` par `300`. Pour un PNJ qui dialogue toutes les
30 secondes, utilisez `30`.

Gardez `--basis scenario` jusqu'à ce que la durée d'une réponse provienne d'un
banc réel et reproductible.

## 5. Vérifier la réussite

Votre premier banc est réussi si :

- la commande produit un JSON valide ;
- `basis` vaut `scenario` ;
- le nombre de flux reste celui que vous avez réellement prévu ;
- vous pouvez expliquer pourquoi le nombre de PNJ baisse lorsqu'ils parlent plus
  souvent.

Passez ensuite au guide [Mesurer la capacité PNJ](../how-to/measure-npc-capacity.md)
pour remplacer le scénario par des mesures.
