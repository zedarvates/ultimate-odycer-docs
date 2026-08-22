# Démarrer un projet Ultimate Odycer à partir du matériel public

Ce tutoriel reste dans les dépôts publiés. Vous repartirez avec une carte
de l'écosystème, une copie docs validée, et un flux de modèles JSON
épingles. Vous ne vous connecterez pas a un serveur de production et vous
n'obtiendrez pas un client MMO jouable.

## Résultat attendu

- vous pouvez expliquer ce qui est public et ce qui ne l'est pas ;
- le validateur de documentation renvoie `validation: ok` ;
- vous savez épingler un modèle du registre sans inventer de compatibilité.

## Préalables

- Python 3.11 ou plus récent ;
- un terminal ouvert sur une copie locale de ce dépôt ;
- aucun identifiant de production.

## 1. Lire la carte publique

Ouvrez la [vue d'ensemble de l'écosystème](../explanation/ecosystem-overview.md)
et notez :

- ce hub de documentation ;
- le registre de modèles JSON ;
- les quatre starters clients documentation seulement ;
- le suivi public des retours ;
- le serveur Zig non publié.

## 2. Valider ce dépôt

Dans PowerShell :

```powershell
rtk python scripts/validate_docs.py
rtk python -m unittest discover -s tests -v
```

La première commande doit se terminer par `validation: ok`.

## 3. Épingler un contrat de contenu, pas un monde live

Clonez ou parcourez [ultod-json-template-registry](https://github.com/zedarvates/ultod-json-template-registry).
Résolvez une entrée de catalogue, enregistrez sa version et son SHA-256, et
traitez une liste de compatibilité vide comme non supportée.

Ne téléchargez pas des modèles automatiquement dans un jeu en cours.

## 4. Choisir un profil de futur client

Choisissez un starter documentation seulement : Godot VR, Godot Classic 3D,
Three.js 2.5D ou FoveaCore. Lisez son `SCOPE.md` et sa page de
compatibilité serveur. Si l'alignement est bloqué, n'inventez pas de client
réseau.

## 5. Voie PNJ home lab optionnelle

Si vous dimensionnez du matériel de dialogue local, continuez avec le
[premier banc PNJ](first-npc-benchmark.md). Gardez l'inférence en boucle
locale et étiquettez les resultats `scenario` ou `estimated` tant que vous
n'avez pas mesuré.

## 6. Vérifier le succès

Le tutoriel est terminé lorsque vous pouvez montrer les dépôts publics,
nommer la frontière serveur non publiée, et refuser une revendication de
compatibilité sans preuve.

Suite : [vue d'architecture](../explanation/architecture-overview.md),
[créer du contenu](../how-to/author-world-content.md), ou
[contribuer et tester](../how-to/contribute-and-test.md).
