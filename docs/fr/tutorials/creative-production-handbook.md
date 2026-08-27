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
