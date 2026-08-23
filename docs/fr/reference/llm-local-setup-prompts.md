# Prompts LM pour poursuivre la mise en route locale

Remplacez seulement les valeurs entre accolades. Ne collez jamais de mot de
passe, secret JWT, clé privée, dump de base ou donnée joueur.

Chaque prompt conserve les mêmes règles : lire l'état, ne rien inventer,
préserver les données, avancer par petite étape et demander confirmation avant
une action sensible.

## 1. Transformer une idée en fiche de projet

```text
Tu m'accompagnes comme débutant technique pour préparer un projet Ultimate Odycer.
Pose-moi une seule question à la fois sur le genre, l'époque, la boucle de jeu,
le nombre de joueurs, les déplacements, la persistance, les plateformes et
l'échelle du premier prototype. À la fin, produis une fiche courte et sépare
faits, décisions et éléments encore indisponibles. Ne choisis pas le moteur ou
la topologie avant d'avoir mes réponses.
```

## 2. Recommander moteur, template et topologie

```text
Lis d'abord le catalogue public local-setup-catalog et ma fiche ci-dessous.
Recommande Godot par défaut, sauf contrainte explicite. Compare uniquement les
templates réellement listés et conserve leur statut exact. Choisis entre
flat_map, planet, mega_planet et solar_system en privilégiant le plus petit
prototype capable de prouver la boucle de jeu. Explique le compromis et demande
mon accord avant de figer la décision.

Fiche : {FICHE_SANS_SECRET}
```

## 3. Vérifier les prérequis Windows

```text
Guide-moi par une seule commande non destructive à la fois pour vérifier
Windows, WSL, Docker et Docker Compose. Pour chaque commande, donne le résultat
attendu et attends ma sortie avant de continuer. Ne propose ni installation
payante ni ouverture réseau automatique. Ne demande jamais un secret.
```

## 4. Vérifier une release sans l'exécuter

```text
Aide-moi à vérifier une archive Ultimate Odycer sans l'exécuter. Commence par
la page officielle https://www.ultimateodycer.com/releases/ et arrête-toi si
elle ne liste aucune release. Compare le nom, la plateforme, la taille et le
SHA-256. Ne fabrique aucune URL, version, empreinte ou commande spécifique à un
fichier absent. Voici seulement les métadonnées publiques que j'ai copiées :
{METADONNEES_RELEASE_SANS_SECRET}
```

## 5. Diagnostiquer Docker et PostgreSQL

```text
Analyse ce diagnostic local sans modifier ni supprimer de données. Commence par
versions, état Compose, santé PostgreSQL et journaux sans secret. Distingue
volume persistant et sauvegarde. Interdis down avec suppression de volumes,
prune, DROP de la base active et affichage du mot de passe. Propose une seule
vérification à la fois avec résultat attendu.

Commande et erreur : {ERREUR_SANS_SECRET}
```

## 6. Connecter Godot

```text
Vérifie avant toute modification que le dépôt contient project.godot et déclare
une compatibilité explicite avec ma version serveur. Utilise uniquement les
fichiers de configuration documentés par ce template et localhost. Ne modifie
pas le routeur, le pare-feu ou l'autorité serveur. Aide-moi à prouver login,
entrée dans le monde, avatar visible et une action minimale, une étape à la fois.

Versions publiques : {VERSIONS_SANS_SECRET}
```

## 7. Analyser une case d'acceptation en échec

```text
La case suivante de la liste d'acceptation Ultimate Odycer a échoué :
{CASE_ET_PREUVE_NEGATIVE}

Classe le résultat comme failed, blocked, unavailable ou partial. Identifie la
première preuve manquante et propose un contrôle non destructif. Ne transforme
pas un mock, un build ou une documentation valide en preuve runtime.
```

## 8. Planifier la suite après la mise en route

```text
Voici mes preuves de mise en route locale, sans secret : {PREUVES}
Voici mon objectif suivant : {OBJECTIF}

Vérifie d'abord quelles portes sont réellement vertes. Propose le plus petit
jalon testable suivant, ses fichiers probables, son résultat observable et ses
limites. Préserve mon travail existant. Demande confirmation avant suppression,
exposition réseau, achat, déploiement ou publication.
```

## Réponse attendue d'un bon LM

Un bon accompagnement :

- cite le fichier ou la sortie utilisée ;
- indique ce qui est observé, estimé, décidé ou indisponible ;
- ne demande pas de secret ;
- propose une étape réversible ;
- attend le résultat avant la suivante ;
- signale honnêtement un blocage.
