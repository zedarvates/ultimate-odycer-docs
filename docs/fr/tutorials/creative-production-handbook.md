# Manuel de production créative

Ce manuel accompagne un débutant assisté par un LM depuis l'idée jusqu'à un
asset candidat vérifié. Il ne remplace ni l'auteur, ni la licence d'un asset, ni
la validation du serveur.

## Avant de commencer

Conservez une fiche de projet, un dossier de sources, les licences, les liens
officiels et les preuves de chaque conversion. Une capture ou un aperçu ne rend
pas un contenu prêt pour le runtime.

Choisissez un parcours :

- **gratuit et local** : logiciels libres, fichiers sur votre machine ;
- **économique** : achat unique, freemium ou licence limitée ;
- **professionnel** : abonnement, crédits ou offre studio/cloud.

Le [catalogue des outils](../reference/creative-tools-catalog.md) n'affiche pas
de prix exact : il indique le modèle tarifaire et le lien officiel.

## Écriture et conception du monde

Définissez genre, époque, boucle de jeu, factions, règles, économie, quêtes et
dialogues. Twine constitue un bon chemin gratuit pour les embranchements ; un LM
peut structurer les idées mais doit conserver les décisions ouvertes.

**Carte Kanboard produite :** « Valider la fiche créative du monde » avec
critères, dépendances et sources.

## Cartes, terrains, villes et donjons

Vous pouvez commencer par un dessin papier, PNG, JPEG, SVG, des couches QGIS ou
un blockout Blender. Suivez [dessiner et convertir une carte](../how-to/draw-and-convert-map.md),
puis comparez les [outils monde et structure](../reference/world-map-and-structure-tools.md).

**Carte Kanboard produite :** « Produire la proposition de carte v1 ».

## 3D, matériaux et photogrammétrie

Le chemin gratuit recommandé combine Blender, Material Maker, Poly Haven et
Meshroom. Asset Factory peut préparer des candidats et manifestes, mais ses
preuves GLB ou de contrat splat ne prouvent pas automatiquement le rendu GPU,
OpenXR ou l'adoption par le client canonique. Pour un client 2.5D, un pipeline
hybride peut rendre des modèles 3D en sprites multi-directionnels et atlas JSON.
Dans le template Three.js actuel, ce générateur de sprites puis SFX reste prévu.

**Carte Kanboard produite :** « Valider un asset représentatif avec provenance ».

## Personnages et animation

Séparez forme visuelle, squelette, animation et statistiques de gameplay. Les
éditeurs Lite produisent des propositions JSON ; le serveur conserve l'autorité
sur statistiques, attaques, spawn et physique.

**Carte Kanboard produite :** « Valider le personnage test et ses droits ».

## Audio, UI, VFX et vidéo

Conservez WAV/FLAC comme masters, exportez le format runtime documenté et
vérifiez séparément musique, voix, samples, polices, icônes et plug-ins. Une
licence logicielle gratuite ne rend pas automatiquement les contenus gratuits.

**Carte Kanboard produite :** « Valider le pack audiovisuel minimal ».

## IA locale ou cloud

ComfyUI est le chemin local privilégié. Chaque modèle, LoRA, custom node et
dataset garde sa propre licence. Pour le cloud, vérifiez upload, rétention,
entraînement, propriété des sorties, consentement vocal et modèle tarifaire.
Des suites spécialisées comme [Sorceress Games](https://sorceress.games/) offrent
également un ensemble très poussé d'outils web (sprites, 3D, voxel, audio, code)
dont l'intégration et l'interopérabilité avec Ultimate Odycer sont encouragées.

**Carte Kanboard produite :** « Auditer le workflow IA avant génération ».

## Import, optimisation, licences et provenance

Préférez GLB/glTF pour la 3D et gardez OBJ/FBX comme formats de conversion.
Vérifiez PBR, UV, collisions, navigation, LOD, compression, budgets, hashes et
manifestes. Aucun asset ne devient `runtime_ready` sans revue humaine et gate
runtime correspondant.

**Carte Kanboard produite :** « Passer le gate d'import Godot isolé ».

## Organisation Kanboard et Botte Secrète

Kanboard conserve le travail visible. Botte Secrète transforme une carte en
tâche bornée, choisit outil déterministe, LM local ou cloud, réduit le contexte
et lance les contrôles. Par défaut, l'humain déplace lui-même la carte.

## Exercice suivi : le quartier des Trois Passages

**Statut : exercice proposé, pas une démonstration livrée ni testée.** Ce nom
désigne un exemple original, pas un nouveau template officiel. Le parcours
utilise une carte plate et vise un essai Godot local. Préparez les fichiers
sans attendre la Tools Suite ; n'inventez pas de connecteur si un module manque.

Objectif joueur : partir d'une place, rejoindre un atelier, prendre un colis
fictif et le déposer dans une cour. Première version : à pied, un quartier,
un bâtiment simple et un personnage provisoire. Véhicules, combat, économie
persistante et monde planétaire sont hors périmètre.

Consacrez au maximum 30 minutes à chaque proposition du LM et deux révisions
avant de demander une décision humaine. Ce budget est un choix d'exercice,
pas une estimation de durée totale ni de performance.

### 1. Fixer les décisions et organiser les fichiers

Écrivez une fiche : objectif, moteur et version choisis, template et statut,
topologie `flat_map`, machine cible, limites. Préparez des dossiers séparés
pour le brief, les dessins sources, les assets éditables, les exports, les
licences et les preuves. Gardez les secrets et dumps PostgreSQL ailleurs.

**Résultat attendu :** une fiche approuvée et une carte Kanboard par étape,
avec un critère de réussite. Botte Secrète peut proposer le découpage ; le LM
ne modifie pas automatiquement le tableau.

> Prompt : « Reformule mon projet en une fiche courte et huit tâches ordonnées.
> Sépare décisions confirmées et questions ouvertes. N'installe rien et ne crée
> aucune tâche dans un service externe. »

### 2. Dessiner le quartier

Dessinez une place, trois passages, l'atelier et la cour. Ajoutez une légende,
le point de départ, la destination et une échelle choisie explicitement.
Un carré de 100 mètres de côté peut servir de convention de départ ; ce n'est
pas une dimension mesurée dans l'image. Séparez terrain, zones praticables,
emprises des bâtiments et annotations.

**Résultat attendu :** dessin source conservé et liste des ambiguïtés, suivant
le [guide de conversion de carte](../how-to/draw-and-convert-map.md).

> Prompt : « Décris uniquement ce qui est visible sur mon dessin. Propose une
> légende et des coordonnées avec leur origine et leurs unités. Signale toute
> dimension déduite. Attends ma validation avant de proposer la conversion. »

### 3. Préparer la proposition de carte

Traduisez le dessin validé en proposition structurée selon le contrat du guide
de conversion. Conservez séparément relief, circulation, bâtiments et zones
de jeu. Si un outil compatible est disponible, vérifiez son import dans une
copie du projet. Sinon, gardez le plan et construisez un décor de volumes
simples dans l'éditeur choisi : ce repli n'est pas un import Tools Suite.

**Résultat attendu :** proposition relue, origine et unités explicites,
transformations documentées. Le statut reste `planned` jusqu'à l'essai réel.

> Prompt : « Prépare une proposition de conversion réversible. Liste les
> fichiers à produire et les capacités réellement disponibles. Aucun appel
> serveur, aucun changement des sources et aucune API inventée. »

### 4. Créer seulement les éléments indispensables

Préparez un atelier simple, un colis et un personnage provisoire. Une capsule
peut représenter le personnage tant que son apparence n'est pas l'objet du
test. Gardez les fichiers éditables et les exports séparés ; consignez auteur,
origine et droits de chaque élément. Un aperçu d'éditeur ne fournit pas
automatiquement un modèle 3D exportable.

**Résultat attendu :** trois éléments identifiables et leurs fiches de
provenance. Les statistiques du personnage ne sont pas autorisées par son mesh.

> Prompt : « Propose les trois éléments minimum pour cette livraison. Réutilise
> mes sources autorisées, liste les droits manquants et les formats attendus.
> Aucun achat, upload ou génération payante sans mon accord. »

### 5. Vérifier l'import visuel isolé

Dans une copie dédiée du projet moteur, contrôlez échelle, orientation,
matériaux et absence d'assets manquants. Testez ensuite collisions et passage
par les trois rues, si ces fonctions existent dans le client choisi. Notez
séparément « visible », « collision vérifiée » et « navigation vérifiée ».

**Résultat attendu :** capture réelle, versions et journal d'import. Sans
exécution, gardez `[Scaffolding / Proxy]` ; un import réussi reste une preuve
isolée, pas une validation multijoueur ou VR.

> Prompt : « Vérifie un élément à la fois dans cette copie autorisée. Décris
> l'attendu et l'observé. Ne coche ni collision ni navigation à partir d'une
> simple capture. Arrête-toi si un fichier ou un outil requis manque. »

### 6. Préparer puis tester la livraison

Écrivez trois états : colis disponible, transporté, livré. Définissez les
conditions de transition, le refus d'une seconde prise et le refus d'une
livraison hors de la cour. Une interaction purement locale peut servir de
maquette ; elle ne valide ni inventaire, ni récompense, ni persistance serveur.

**Résultat attendu :** scénario de test avec actions permises et refusées.
Chaque transition serveur attend un contrat et une implémentation vérifiés.

> Prompt : « Décris les états et les tests de cette livraison, sans inventer de
> message réseau. Sépare maquette locale et décisions du serveur. Ne crée pas
> d'argent ni d'objet persistant pour simuler une réussite. »

### 7. Franchir la porte serveur seulement si elle est ouverte

Suivez le [parcours de premier monde local](create-first-local-world.md) et
sa checklist : archive officielle, versions compatibles, PostgreSQL, login,
entrée dans le monde. Si la release ou le template manque, marquez cette
étape `blocked` et conservez le travail créatif ; ne remplacez pas le serveur
par un faux service en déclarant le parcours réussi.

**Résultat attendu :** preuves séparées de connexion, action acceptée ou
refusée, puis persistance uniquement si elle a réellement été testée.

> Prompt : « Vérifie les prérequis publics et les preuves disponibles. Si une
> condition manque, explique le blocage. Sinon propose un seul test local
> autorisé, sans ouvrir de port Internet. »

### 8. Sauvegarder et transmettre la reprise

Archivez les sources créatives et leurs licences. Pour les données serveur,
suivez le [guide PostgreSQL](../how-to/backup-and-test-restore-postgresql.md) :
un ZIP d'assets ne sauvegarde pas les personnages. Conservez la preuve de
restauration séparément du dump confidentiel.

**Résultat attendu :** un compte rendu avec versions, fichiers, essais réussis,
essais échoués, blocages et prochaine action. « Préparation créative terminée »
et « première boucle locale vérifiée » sont deux résultats différents.

> Prompt : « Rédige la fiche de reprise à partir des seules preuves fournies.
> Distingue observé, prévu et bloqué. N'inclus aucun secret, contenu de dump ou
> chemin personnel. Propose une seule prochaine étape à valider. »

## Checklist avant de déclarer un asset prêt

- [ ] Source et auteur identifiés.
- [ ] Licence et usage commercial vérifiés.
- [ ] Données confidentielles absentes.
- [ ] Format et conversion documentés.
- [ ] Hash et manifeste enregistrés.
- [ ] Aperçu revu par un humain.
- [ ] Budget technique respecté.
- [ ] Import isolé validé.
- [ ] Limites et preuves négatives conservées.
- [ ] Publication serveur encore soumise à son gate autoritatif.
