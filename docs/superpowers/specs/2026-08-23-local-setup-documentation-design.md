# Conception du parcours de mise en route locale

Date : 2026-08-23  
Statut : conception approuvée, mise en œuvre à planifier

## Objectif

Créer un parcours public, bilingue et utilisable hors ligne qui accompagne un
débutant technique assisté par un LM depuis son idée de jeu jusqu'à une mise en
route locale vérifiée d'Ultimate Odycer.

Le même contenu source doit alimenter :

1. la documentation Markdown de ce dépôt ;
2. une version HTML publiée sur le site Ultimate Odycer ;
3. une version HTML autonome incluse dans chaque archive publique du serveur.

La documentation se termine par une FAQ, des raccourcis pour utilisateurs
avancés et des prompts typiques permettant de poursuivre le projet avec un LM.

## Principes

- Une source Markdown canonique génère les sorties Web et hors ligne.
- Godot est le parcours de référence entièrement détaillé.
- Windows est la plateforme principale ; Linux dispose de variantes validées.
- macOS est hors périmètre. Une future application mobile viserait Android.
- Les choix avancés restent accessibles par un index sans alourdir le parcours
  débutant.
- Toute capacité est étiquetée `disponible`, `en construction`, `prévue` ou
  `indisponible`.
- Les valeurs matérielles sont étiquetées `observée`, `estimée`, `décision` ou
  `indisponible`, conformément aux conventions existantes du dépôt.
- Aucun téléchargement, paquet, test ou niveau de compatibilité ne doit être
  annoncé avant d'exister et d'être vérifié.
- Le serveur reste autoritaire. Aucun client, template ou outil de création ne
  devient une source de vérité pour les données de jeu.

## Publics

### Parcours principal

Le lecteur principal est un débutant technique accompagné par un LM. Chaque
étape fournit :

- l'objectif en langage simple ;
- les prérequis ;
- les actions copiables ;
- le résultat attendu ;
- un contrôle de réussite ;
- les erreurs fréquentes ;
- un prompt de secours à donner à un LM sans lui fournir de secret.

### Parcours avancé

Un index avancé mène directement aux commandes, fichiers de configuration,
contrats de versions, procédures de sauvegarde et points de validation. Il ne
duplique pas le contenu principal.

### Lecteur LM

L'index LM référence les sources humaines canoniques. Il n'accorde aucune
autorisation d'installation, de suppression, de publication, d'ouverture de
port ou d'utilisation de secrets. Les prompts d'exemple demandent au LM de
vérifier les versions, de préserver les fichiers existants et de s'arrêter
avant toute action sensible.

## Parcours documentaire

Le parcours par défaut suit cet ordre :

1. Décrire le projet de jeu.
2. Choisir le moteur 3D.
3. Choisir un template compatible.
4. Décrire la vision créative du monde.
5. Choisir ou faire recommander sa topologie technique.
6. Choisir un profil matériel et vérifier les prérequis.
7. Vérifier la page officielle des releases.
8. Installer Docker et PostgreSQL sous Windows.
9. Configurer la persistance et la connexion du serveur à PostgreSQL.
10. Installer le serveur public lorsqu'une archive vérifiée existe.
11. Installer le template Godot et le connecter localement.
12. Installer, si désiré, les modules compatibles de la Tools Suite.
13. Effectuer la sauvegarde et la restauration de contrôle.
14. Exécuter la validation locale finale.
15. Poursuivre avec la FAQ, les raccourcis et les prompts pour LM.

Si aucune release serveur n'est disponible, le parcours s'arrête proprement et
explique que la suite n'est pas encore exécutable. Il ne remplace jamais une
archive absente par un binaire interne ou une construction non auditée.

## Choix du moteur et des templates

### Moteurs

- **Godot** : chemin recommandé et détaillé.
- **Three.js** : chemin alternatif Web demandant des adaptations.
- **Unity** : moteur alternatif sans promesse de template validé.
- **Unreal Engine** : moteur alternatif sans promesse de template validé.
- **FoveaCore** : chemin spécialisé, présenté selon son état public réel.

La documentation sépare le moteur du type d'expérience, même lorsqu'un template
associe déjà les deux.

### Catalogue initial

| Template | Moteur | Expérience | Statut de documentation |
|---|---|---|---|
| Classic 3D MMORPG | Godot | MMORPG 3D classique | En construction |
| VR MMORPG | Godot | MMORPG en réalité virtuelle | En construction |
| 2.5D MMORPG | Three.js | MMORPG Web 2.5D/isométrique | En construction |
| FPS-RPG Online | FoveaCore | FPS/RPG en ligne | En construction |
| Prêt à tout faire pour de l'argent | Godot | RPG urbain multijoueur en monde ouvert | Prévu |

Le cinquième dépôt prévu porte le nom technique
`ultod-client-godot-open-city-crime-rpg-template`. La documentation peut
indiquer qu'il convient aux projets de type GTA-like, mais le template doit
rester original : aucun personnage, lieu, scénario, code, dialogue, asset ou
identité visuelle d'une œuvre existante n'est repris.

## Conception du monde

Le guide distingue deux décisions.

### Vision créative

Le lecteur décrit au minimum :

- genre et époque ;
- ambiance et références fonctionnelles ;
- activités principales ;
- nombre et rôle des joueurs ;
- moyens de déplacement ;
- degré de persistance ;
- échelle souhaitée ;
- plateformes visées.

### Topologie technique

- **Carte plate** : villes, donjons, arènes, régions ou monde urbain. C'est le
  choix initial recommandé pour un RPG urbain de type GTA-like.
- **Planète** : monde sphérique unique avec déplacement à grande échelle.
- **Méga-planète** : planète de très grande taille nécessitant partitionnement,
  streaming et validation de capacité.
- **Système solaire** : plusieurs corps et espaces de transition ; complexité
  la plus élevée.

Un humain ou un LM peut recommander une topologie à partir de la vision
créative, mais le choix final appartient à l'utilisateur. Le guide n'affirme
pas qu'une topologie est prise en charge tant que son chemin serveur-client
n'est pas validé.

## Profils d'installation locale

### Serveur dédié

La machine exécute uniquement le serveur, PostgreSQL et les services locaux
nécessaires. Le guide privilégie la stabilité, le stockage persistant et la
sauvegarde.

### Poste partagé

L'utilisateur continue à travailler ou jouer sur la machine pendant que le
serveur fonctionne. Le guide réserve de la mémoire et des cœurs à Windows,
limite les ressources Docker et explique la différence entre ralentissement du
poste et incapacité réelle du serveur.

### Poste de création

La machine exécute Godot et, facultativement, des modules de la Tools Suite.
Les besoins de l'Asset Factory et de ComfyUI, notamment le GPU, la VRAM et le
stockage des modèles, sont séparés des besoins minimaux du serveur.

Les exigences chiffrées proviennent des métadonnées et mesures de chaque
release. Avant ces mesures, le guide fournit uniquement des estimations
explicitement étiquetées et une méthode de dimensionnement.

## PostgreSQL, Docker et sauvegardes

Le chemin Windows recommandé utilise Docker avec le backend WSL 2 et une image
PostgreSQL à version fixée. Linux reçoit une variante Docker Engine.

Le parcours doit couvrir :

- la vérification de Docker et de WSL 2 ;
- la création d'un volume PostgreSQL nommé et persistant ;
- la configuration des identifiants par fichier local non versionné ;
- la connexion du serveur à PostgreSQL ;
- le contrôle de santé et de version du schéma ;
- une sauvegarde PostgreSQL vers un dossier hôte extérieur au volume Docker ;
- une restauration de contrôle ;
- les conséquences de `down -v`, de la suppression d'un volume, d'une
  désinstallation et d'une opération de nettoyage ;
- la séparation entre volume persistant et véritable sauvegarde.

La réussite d'une sauvegarde ne suffit pas : une restauration de contrôle doit
être effectuée avant de déclarer la mise en route terminée.

## Serveur et Tools Suite

La page canonique de téléchargement est
`https://www.ultimateodycer.com/releases/`. Elle est la seule source proposée
pour une archive serveur officielle. Une release apparaît dans le guide
uniquement si l'archive et son empreinte SHA-256 sont réellement publiées.

Chaque famille de release partage un identifiant de compatibilité entre :

- le serveur ;
- les templates clients ;
- la Tools Suite ;
- le schéma PostgreSQL ;
- la documentation embarquée.

L'utilisateur choisit :

1. **Serveur seul** ; ou
2. **Serveur avec modules Tools Suite sélectionnés**.

La Tools Suite est optionnelle et actuellement en construction. Son catalogue
prévu comprend notamment les éditeurs de donjons, villes, architectures,
monstres et avatars, l'Asset Factory avec ComfyUI, le WebAdmin et d'autres
outils futurs. Aucun de ces modules n'est marqué disponible sans paquet public
et validation correspondante.

## Critère de réussite locale

La mise en route est terminée lorsque les contrôles applicables réussissent :

- l'archive et son empreinte ont été vérifiées ;
- PostgreSQL utilise un stockage persistant ;
- le serveur se connecte à la base et son contrôle de santé est valide ;
- le serveur reste limité au périmètre réseau explicitement choisi ;
- le template Godot démarre et rejoint le serveur local ;
- un compte ou personnage de test rejoint le monde ;
- l'avatar apparaît et effectue une action minimale autorisée ;
- la configuration survit à un arrêt et un redémarrage ;
- une sauvegarde et une restauration de contrôle réussissent ;
- le WebAdmin ou les autres outils sélectionnés s'ouvrent localement ;
- aucun port Internet n'a été ouvert automatiquement.

Un contrôle non applicable est indiqué comme tel. Un contrôle impossible faute
de release ou de composant public bloque la déclaration de réussite complète.

## Source unique et sorties HTML

### Source canonique

Les fichiers Markdown bilingues de ce dépôt sont la source unique. Le HTML ne
doit pas être maintenu manuellement.

### Site Web

Le site génère ou importe le HTML depuis la source canonique. Il affiche la
version courante de la documentation et les statuts réels des composants.

### Archive serveur

Chaque ZIP serveur contient un instantané autonome correspondant à sa release :

- `docs/index.html` ;
- les pages, styles et images nécessaires avec chemins relatifs ;
- la FAQ et les prompts pour LM ;
- la matrice de compatibilité ;
- la version du serveur ;
- l'identifiant de source de la documentation ;
- les fichiers de contexte LM utiles ;
- les empreintes dans `SHA256SUMS.txt`.

La documentation hors ligne ne dépend d'aucun script, service, police ou asset
distant. Un bandeau indique la version documentée et renvoie vers la version en
ligne lorsqu'une connexion est disponible.

## FAQ et prompts pour LM

La FAQ couvre au minimum :

- absence de release téléchargeable ;
- incompatibilité de versions ;
- Docker ou WSL 2 indisponible ;
- PostgreSQL inaccessible ;
- volume manquant ;
- échec de sauvegarde ou de restauration ;
- ports déjà utilisés ;
- serveur sain mais client non connecté ;
- poste partagé devenu trop lent ;
- module Tools Suite encore indisponible.

Les prompts sont structurés par objectif : choisir un moteur, sélectionner un
template, décrire un monde, recommander une topologie, vérifier les prérequis,
diagnostiquer Docker/PostgreSQL, connecter Godot, analyser un échec de test et
planifier la suite du projet.

Chaque prompt demande au LM :

- de commencer par lire l'état et les versions ;
- de ne pas inventer de paquet ou de capacité ;
- de ne jamais demander l'affichage d'un secret ;
- de préserver les fichiers et données existants ;
- de proposer une étape à la fois au débutant ;
- de demander confirmation avant suppression, exposition réseau, achat,
  déploiement ou publication ;
- de fournir une preuve vérifiable de chaque réussite.

## Organisation proposée

Le contenu final est réparti entre :

- un point d'entrée « créer son premier monde local » ;
- un questionnaire de projet et un arbre de décision ;
- un guide Windows principal ;
- des variantes Linux ;
- un guide PostgreSQL et sauvegardes ;
- un guide de connexion Godot ;
- une page Tools Suite et compatibilité ;
- une validation finale ;
- une FAQ ;
- un catalogue de prompts ;
- un index avancé ;
- un index LM mis à jour.

Le README racine ajoute uniquement les liens d'entrée nécessaires et conserve
les changements locaux préexistants, notamment le lien Discord.

## Mise en œuvre par étapes

1. Rédiger le parcours Markdown français et ses contrats de statut.
2. Ajouter l'index avancé, la FAQ et les prompts LM.
3. Produire la version anglaise cohérente.
4. Mettre à jour les index humains et LM.
5. Ajouter et vérifier la génération HTML autonome.
6. Intégrer la sortie générée au site Web.
7. Préparer le contrat d'inclusion dans les futures archives serveur.
8. Activer l'empaquetage uniquement lorsqu'une release publique vérifiée
   existe.

Les étapes 6 à 8 ne prouvent ni publication du site, ni disponibilité du
serveur, ni compatibilité runtime tant que leurs validations propres n'ont pas
réussi.

## Validation

Avant publication, les contrôles doivent couvrir :

- liens Markdown et HTML internes ;
- cohérence français/anglais ;
- validité des index LM ;
- statuts et limites publiques ;
- absence de secret et de chemin interne confidentiel ;
- fonctionnement HTML hors ligne sans réseau ;
- cohérence de version et de compatibilité ;
- génération et vérification des empreintes ;
- copie fraîche du dépôt ;
- tests documentaires existants ;
- contrôle de dérive du projet.

La validation documentaire ne prouve pas le fonctionnement du serveur, du
client, de PostgreSQL, de la Tools Suite, de ComfyUI ou d'un déploiement réel.

## Hors périmètre

- Publication d'une archive serveur inexistante.
- Copie de code serveur propriétaire dans la documentation publique.
- Publication automatique du site ou d'une release.
- Ouverture automatique d'un port externe.
- Support macOS.
- Création de l'application Android.
- Livraison des modules Tools Suite encore en construction.
- Certification de performances sans mesure reproductible.

## Conditions d'acceptation

La conception est satisfaite lorsque :

1. un débutant peut identifier le bon moteur, le bon template et la bonne
   topologie ;
2. le guide s'arrête honnêtement si aucun serveur public n'est disponible ;
3. une release disponible peut être installée avec PostgreSQL persistant ;
4. la sauvegarde et la restauration sont vérifiées ;
5. le client Godot peut atteindre le contrôle local défini par la release ;
6. les utilisateurs avancés disposent de raccourcis indexés ;
7. un LM dispose de prompts sûrs et de sources canoniques ;
8. le site et le ZIP sont produits depuis la même source ;
9. les capacités en construction ne sont jamais présentées comme terminées.
