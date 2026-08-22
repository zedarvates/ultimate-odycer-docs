# Contribuer et tester l'écosystème public

Utilisez ce guide pour ajouter ou tester du matériel public Ultimate Odycer
sans revendiquer un MMO jouable, un protocole publié ou une compatibilité
de production.

## 1. Choisir le bon dépôt

| Vous voulez... | Aller ici | Ne pas... |
|---|---|---|
| Corriger ou étendre la documentation | [ultimate-odycer-docs](https://github.com/zedarvates/ultimate-odycer-docs) | copier de la doc serveur propriétaire |
| Ajouter ou versionner un modèle JSON | [ultod-json-template-registry](https://github.com/zedarvates/ultod-json-template-registry) | inventer une compatibilité |
| Discuter une future coque cliente | un des quatre starters documentation seulement | importer le code client de jeu existant |
| Signaler un bug ou une idée publique | [ultimate-odycer-feedback](https://github.com/zedarvates/ultimate-odycer-feedback) | coller secrets, journaux ou données joueur |

Dans ce dépôt de documentation, gardez les paires français / anglais
ensemble. Respectez la licence, le périmètre et la checklist de publication
du dépôt cible.

## 2. Tester seulement ce qui est public

Un contrôle public complet ressemble à ceci :

```text
hub docs
  validate_docs.py + tests unitaires + fresh-copy check
registre JSON
  épingler version + SHA-256 + compatibility vide sauf preuve
starter client
  lire SCOPE, ROADMAP et compatibilité serveur ; pas de projet caché
voie PNJ home lab
  capacité scénario ou mesurée, inférence en boucle locale, repli fail-closed
suivi des retours
  issue publique avec reproduction synthétique seulement
```

Une validation docs prouve la structure de la documentation. Elle ne prouve
pas un serveur, un casque, un protocole ou un CCU.

## 3. Lancer les contrôles de ce dépôt

Depuis une copie locale de ce dépôt :

```powershell
rtk python scripts/validate_docs.py
rtk python -m unittest discover -s tests -v
rtk python scripts/fresh_copy_check.py
```

Attendu : `validation: ok`, tests unitaires OK, et `fresh-copy: ok`.

## 4. Tester un modèle sans activer un monde

1. Résoudre une entrée de catalogue.
2. Enregistrer version et SHA-256.
3. Refuser le téléchargement automatique au runtime.
4. Laisser `compatibility` vide tant qu'un consommateur nommé, une version,
   une date et une preuve n'existent pas.
5. Traiter l'instantané comme des données, pas un don d'or, d'objets ou
   d'accès.

Détails : [utiliser les modèles JSON](use-json-templates.md).

## 5. Tester un starter client sans inventer un réseau

Lisez le `SCOPE.md` du starter et sa page de compatibilité serveur. Si
l'alignement est bloqué, les tests autorisés sont la revue de documentation,
les contrôles de licence / périmètre, et des expériences de présentation
locales hors réseau. Une fixture de boucle locale synthétique est la
première preuve réseau autorisée, et seulement après une porte de protocole
public.

Voir [l'architecture client](../explanation/client-architecture.md).

## 6. Échouer de manière fermée

Marquez une preuve manquante `unavailable`. N'inventez pas d'opcodes, d'URL
de production, d'identités joueur ou de compatibilité certifiée. N'exposez
pas un LLM local ou un assistant docs hors boucle locale sauf conception LAN
privée explicite.

## Pages liées

- [Vue d'ensemble de l'écosystème](../explanation/ecosystem-overview.md)
- [Démarrer un projet](../tutorials/start-an-ultimate-odycer-project.md)
- [Exploiter un home lab](operate-a-home-lab.md)
- [CONTRIBUTING.md](../../../CONTRIBUTING.md)
