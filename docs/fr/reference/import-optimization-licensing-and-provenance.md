# Import, optimisation, licences et provenance

## Formats

- 3D : GLB/glTF préféré ; OBJ/FBX avec conversion ;
- splats : FOVEA, PLY ou SPLAT seulement si le contrat les accepte ;
- terrain : PNG/EXR/RAW selon le consommateur ;
- images/UI : PNG, SVG ; audio : WAV/FLAC master, OGG/WAV runtime ;
- données : JSON versionné, CSV intermédiaire contrôlé.

## Optimisation

Vérifiez unités, axes, UV, matériaux, textures, compression, mipmaps, LOD,
collisions, navigation, occlusion, streaming, animation, mémoire CPU/GPU et temps
de chargement. Séparez build, import headless, rendu GPU, XR et preuve réseau.

## Licence et provenance

Pour chaque source : auteur, URL, date, licence, plan applicable, asset/modèle,
modifications, outils, prompts, consentements et hash. Une licence logicielle ne
couvre pas automatiquement les assets générés ou importés.

## Gate de publication

1. schéma et format ;
2. licence et usage commercial ;
3. secrets et contenu interdit ;
4. hash/manifeste ;
5. budgets ;
6. revue humaine ;
7. import Godot isolé ;
8. validation serveur autoritative.

Un échec garde l'asset candidat et la preuve négative ; il ne devient pas
`runtime_ready` par renommage manuel.
