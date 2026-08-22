# Utiliser et versionner les modèles JSON

Utilisez ce guide pour consommer ou proposer des modèles dans
[ultod-json-template-registry](https://github.com/zedarvates/ultod-json-template-registry)
sans traiter le registre comme une base de jeu live.

## 1. Lire le contrat

Le registre definit :

- l'organisation : `templates/<famille>/<nom>/v<MAJEUR>.<MINEUR>.<CORRECTIF>/` ;
- les champs obligatoires des nouveaux modèles : `id`, `template_type`, `version` ;
- les champs de catalogue, dont SHA-256 et `compatibility` ;
- les statuts : `draft`, `expérimental`, `stable`, `deprecated`.

Suivez [TEMPLATE-SPEC.md](https://github.com/zedarvates/ultod-json-template-registry/blob/main/TEMPLATE-SPEC.md)
et [VERSIONING.md](https://github.com/zedarvates/ultod-json-template-registry/blob/main/VERSIONING.md).
Ne copiez pas ces fichiers dans ce dépôt.

## 2. Consommer un modèle

1. Résoudre l'entrée via `templates/catalog.json`.
2. Épingler la version exacte. Ne jamais supposer que latest est compatible.
3. Vérifier le SHA-256 avant usage.
4. Vendor un instantané revu pour des builds déterministes.
5. Traiter le statut expérimental comme instable.
6. Traiter une liste de compatibilité vide comme aucune compatibilité certifiée.
7. Valider les valeurs de gameplay côté serveur. Un modèle ne donne pas or,
   objets, dégâts ou vitesse.

Les clients ne doivent pas télécharger ou activer des modèles automatiquement
au runtime.

## 3. Créer un nouveau modèle

Utilisez le kebab-case ASCII pour famille et nom, le snake_case pour les
identifiants, et un nouveau dossier SemVer a chaque changement. Une version
publiée est immuable.

Forme minimale :

```json
{
  "id": "community_festival",
  "template_type": "event",
  "version": "1.0.0",
  "name": "Community Festival",
  "description": "A small recurring social event.",
  "enabled": true,
  "tags": ["social", "seasonal"],
  "duration_ms": 3600000,
  "dependencies": ["location_town_square"]
}
```

Laissez `compatibility` vide tant qu'un consommateur nommé, une version, une
date et une preuve n'existent pas.

## 4. Valider avant de proposer

- JSON UTF-8 strict, sans commentaire ;
- unités explicites ;
- références par identifiants logiques, jamais un chemin absolu ;
- aucun secret, URL de production, donnée personnelle ou override admin ;
- documenter les limites dans le README de version ;
- calculer le vrai SHA-256 avant publication.

Un modèle dans le registre n'est pas une preuve d'intégration serveur ou
client.

## Pages liées

- [Créer du contenu](author-world-content.md)
- [Systèmes de gameplay](../reference/gameplay-systems.md)
- [Vue d'ensemble de l'écosystème](../explanation/ecosystem-overview.md)
