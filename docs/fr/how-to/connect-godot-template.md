# Connecter un template Godot au serveur local

Godot est le chemin client recommandé. Cette page ne transforme pas une
fondation documentaire en client jouable.

> Les templates Godot publics sont actuellement `under_construction`. Continuez
> seulement si le dépôt choisi contient réellement un projet Godot et annonce
> une compatibilité avec votre version du serveur.

## 1. Vérifier les identifiants de compatibilité

Comparez :

- la version dans `VERSION` de l'archive serveur ;
- la compatibilité déclarée dans le template ;
- la version du schéma PostgreSQL ;
- la version de la documentation embarquée ;
- les éventuels modules Tools Suite sélectionnés.

Un nom proche ou une date récente ne remplace pas une correspondance explicite.

## 2. Ouvrir une copie du template

Conservez le template téléchargé intact et travaillez dans une copie dédiée à
votre jeu. Ouvrez cette copie avec la version de Godot indiquée par le dépôt.

Si le dépôt ne contient pas `project.godot`, arrêtez-vous : il s'agit encore
d'une fondation documentaire.

## 3. Configurer les adresses locales

Utilisez uniquement le mécanisme documenté par le template. Les valeurs doivent
viser `localhost` pour :

- le service de login ;
- le serveur de jeu ;
- le WebAdmin, s'il est installé.

Ne modifiez pas le routeur et ne remplacez pas une adresse locale par une
adresse d'écoute générale pour réussir ce tutoriel.

## 4. Lancer le chemin minimal

Dans l'ordre :

1. PostgreSQL sain ;
2. service de login ;
3. serveur de jeu ;
4. projet Godot ;
5. création ou utilisation d'un compte de test local ;
6. entrée du personnage dans le monde.

Le client ne doit jamais décider seul de l'or, des points de vie, de la vitesse
ou d'une autre statistique autoritaire.

## 5. Prouver une action minimale

La preuve attendue comprend :

- authentification acceptée ;
- monde chargé ;
- avatar de test visible ;
- une action minimale autorisée, par exemple un déplacement ;
- aucune erreur fatale dans les journaux client et serveur.

Un écran de menu, une scène statique ou un mock réseau ne suffit pas.

## 6. Redémarrer

Arrêtez proprement le client et les services, puis relancez-les. Vérifiez que la
configuration et les données de test attendues persistent dans PostgreSQL.

Passez ensuite à la
[liste d'acceptation](../reference/local-setup-acceptance-checklist.md).
