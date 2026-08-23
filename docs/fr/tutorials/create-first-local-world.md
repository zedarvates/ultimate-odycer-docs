# Créer son premier monde local

Ce tutoriel accompagne un débutant technique aidé par un LM depuis son idée
jusqu'à une installation locale vérifiée. Il ne suppose ni studio, ni serveur
cloud, ni expérience préalable d'administration système.

> **État actuel — `unavailable` :** aucune release publique du serveur n'est
> encore téléchargeable. Vous pouvez terminer la préparation du projet, mais
> vous devez vous arrêter à l'étape 6 tant que la
> [page officielle des releases](https://www.ultimateodycer.com/releases/)
> n'affiche pas une archive réelle accompagnée de son SHA-256.

## Ce que vous allez décider

1. la vision créative de votre jeu ;
2. le moteur 3D ;
3. le template client ;
4. la topologie du monde ;
5. le profil de la machine locale ;
6. les composants réellement disponibles ;
7. la suite du projet à confier éventuellement à un LM.

## 1. Écrire une fiche de projet courte

Répondez avec des phrases simples :

- Quel est le genre et l'époque du jeu ?
- Que font les joueurs pendant dix minutes ordinaires ?
- Jouent-ils seuls, en petit groupe ou dans un monde très peuplé ?
- Comment se déplacent-ils ?
- Le monde continue-t-il d'évoluer quand ils sont déconnectés ?
- Quel appareil doit faire fonctionner le client ?
- Quelle échelle souhaitez-vous tester en premier ?

Exemple original :

> RPG urbain multijoueur. Les joueurs acceptent des missions, conduisent,
> commercent et développent leurs activités dans une ville persistante. Le
> premier prototype utilise un quartier unique et quelques joueurs locaux.

Une référence comme « GTA-like » décrit une famille de fonctions. Elle
n'autorise pas à reprendre personnages, lieux, scénario, code, dialogues,
assets ou identité visuelle d'une œuvre existante.

## 2. Choisir le moteur

Choisissez **Godot** si vous n'avez pas une contrainte forte qui impose un autre
moteur. C'est le chemin de référence documenté par Ultimate Odycer.

- Godot : recommandé et détaillé ;
- Three.js : solution Web alternative ;
- Unity ou Unreal Engine : possibles, sans template validé actuellement ;
- FoveaCore : solution spécialisée encore en construction.

Consultez la
[matrice moteurs, templates et mondes](../reference/engine-template-world-matrix.md)
avant de continuer.

## 3. Choisir le template

Un template fournit une direction client ; il ne prouve pas que le jeu, le
réseau ou les assets sont terminés. Vérifiez toujours son statut.

Pour le chemin débutant, retenez le template Godot correspondant le mieux à
l'expérience visée. Si son statut est `under_construction` ou `planned`, gardez
votre choix dans la fiche de projet et n'inventez pas les fichiers manquants.

## 4. Choisir la topologie

- `flat_map` : ville, donjon, arène, région ou monde urbain ;
- `planet` : planète sphérique unique ;
- `mega_planet` : planète immense exigeant streaming et partitionnement ;
- `solar_system` : plusieurs corps et espaces de transition.

Commencez par la structure la plus petite capable de prouver votre boucle de
jeu. Le RPG urbain de l'exemple commence sur une `flat_map`, pas sur une planète
entière.

## 5. Choisir le profil local

Les chiffres suivants sont des valeurs de planification `estimated`, pas des
minima certifiés par une release.

| Profil | Processeur | Mémoire | SSD libre | Usage |
|---|---:|---:|---:|---|
| Serveur dédié | 4 cœurs | 8 Gio | 20 Gio | Serveur et PostgreSQL uniquement |
| Poste partagé | 6 cœurs | 16 Gio | 40 Gio | Travail ou jeu pendant que le serveur tourne |
| Poste de création | 8 cœurs | 32 Gio | 100 Gio | Godot et outils de création optionnels |

Le besoin GPU de ComfyUI reste `unavailable` tant qu'un module, ses modèles et
une mesure reproductible ne sont pas publiés. Pour approfondir le choix du
matériel, consultez [choisir le matériel](../how-to/choose-hardware.md).

## 6. Vérifier la release

Ouvrez la [page officielle](https://www.ultimateodycer.com/releases/).

Continuez uniquement si elle affiche :

- une version ;
- une archive correspondant à votre plateforme ;
- sa taille ;
- une empreinte SHA-256 complète ;
- une documentation de compatibilité.

Si la page indique qu'aucune release publique n'existe, votre résultat valide
est la fiche de projet enregistrée avec les choix moteur, template, topologie et
profil matériel. Revenez plus tard ; n'utilisez pas une archive reçue ailleurs.

## 7. Installer le socle local

Lorsqu'une release existe, suivez dans l'ordre :

1. [installation Windows](../how-to/install-local-server-windows.md) ;
2. [variante Linux](../how-to/install-local-server-linux.md), si nécessaire ;
3. [sauvegarde et restauration de contrôle](../how-to/backup-and-test-restore-postgresql.md) ;
4. [connexion du template Godot](../how-to/connect-godot-template.md) ;
5. [liste finale d'acceptation](../reference/local-setup-acceptance-checklist.md).

## 8. Choisir les modules optionnels

L'installation doit proposer deux chemins compatibles avec la même famille de
release :

- serveur seul ;
- serveur avec modules Tools Suite sélectionnés.

La Tools Suite et ses éditeurs de donjons, villes, architectures, créatures et
avatars, l'Asset Factory avec ComfyUI et les autres modules sont actuellement
`under_construction`. Un module absent de la release n'est pas installable.

## Résultat du tutoriel

La mise en route n'est terminée que si tous les contrôles applicables de la
liste d'acceptation réussissent. Une page bien écrite ou un test documentaire
ne prouve jamais que le serveur, PostgreSQL, Godot ou un outil fonctionne sur
votre machine.
