# Outils 3D, matériaux et photogrammétrie

## Chemin gratuit/local

- Blender : modélisation, sculpt, UV, retopologie, rig, conversion GLB ;
- Material Maker : matériaux PBR nodaux et export Godot ;
- Poly Haven : HDRI, textures et modèles CC0 ;
- Meshroom : photogrammétrie locale open source.

## Tools Suite

Asset Factory produit des candidats GLB, images de revue, manifestes et hashes.
Ses contrats `gaussian_splat` acceptent FOVEA, PLY ou SPLAT, mais ne prouvent
pas encore un producteur splat revu, un rendu GPU, OpenXR ou le client canonique.

## Alternatives professionnelles

Substance 3D fonctionne par abonnement ; Maya par abonnement/Flex/conditions
Indie ; ZBrush par abonnement ; Houdini selon éditions non commerciale, Indie
ou commerciale. Vérifiez toujours assets, plug-ins et limites de pipeline.

## Photogrammétrie

Photographiez seulement des sujets autorisés. Conservez originaux, métadonnées,
conditions de prise de vue et consentements. Nettoyez, retopologisez, créez UV,
bakez les détails et contrôlez l'échelle avant export.

## Gate minimal

- GLB/glTF préféré ; OBJ/FBX comme interchange ;
- PBR : albedo, normal, roughness, metallic, AO, height selon besoin ;
- provenance et licence ; hash et manifeste ; revue visuelle ;
- budgets polygones, textures, matériaux, collisions et LOD ;
- import Godot isolé avant toute adoption runtime.

## Variante 2.5D : 3D vers sprites

Le flux proposé est `draft → rendu de contrôle → validation graphique → atlas
sprite → test client → accepted`. Il exige caméra fixe, orientations déclarées,
éclairage normalisé, fond transparent, ombre séparée, animations et atlas JSON.
Ce pipeline reste prévu pour le template Three.js ; il n'est pas une capacité
actuelle d'Asset Factory.
