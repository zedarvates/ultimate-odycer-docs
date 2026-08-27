# Dessiner une carte et préparer sa conversion

Vous pouvez commencer sur papier, tablette, Krita, GIMP, Inkscape, QGIS ou tout
outil capable d'exporter une image lisible. Le LM produit une proposition, pas
une carte autoritative.

## 1. Préparer le dessin

Indiquez :

- nord ou orientation ;
- échelle, ou la mention « échelle inconnue » ;
- limite du monde ;
- relief et altitude attendus ;
- eau, routes, quartiers, régions et landmarks ;
- emprises de bâtiments ;
- entrées, sorties, portails et transitions ;
- zones de spawn, quête, danger et sécurité ;
- légende, couleurs et zones incertaines.

Exportez en PNG, JPEG ou SVG. Conservez le fichier source et ses droits.

## 2. Donner un contexte au LM

Ajoutez la fiche du projet, la topologie choisie (`flat_map`, `planet`,
`mega_planet` ou `solar_system`) et la résolution/échelle connue.

```text
Analyse cette carte comme une proposition Ultimate Odycer.
N'invente pas les informations invisibles. Sépare observations, interprétations,
décisions proposées et incertitudes. Extrais orientation, échelle, limites,
relief, eau, routes, régions, landmarks, bâtiments, transitions et zones de
gameplay. Produis un brouillon uo.map-intent/v1 sans modifier de fichier ni
publier au serveur. Demande ma validation avant toute conversion suivante.
```

## 3. Produire la proposition structurée

Le résultat doit contenir au minimum :

```json
{
  "schema": "uo.map-intent/v1",
  "authority": "proposal_only",
  "source_image": "map-v1.png",
  "scale_status": "known_or_unknown",
  "features": [],
  "uncertainties": [],
  "human_approved": false
}
```

Ce contrat est documentaire tant qu'un schéma public validé n'est pas publié.

## 4. Choisir l'éditeur

- City Editor Lite : paramètres CityConfig et tracés bornés ;
- Architecture Editor Lite : bâtiments multi-niveaux sans runtime ;
- Creature Editor Lite : hors périmètre cartographique ;
- éditeurs City/Architecture/Dungeon complets : prototypes ou surfaces proxy ;
- QGIS/Blender : préparation externe avec conversion nécessaire.

## 5. Prévisualiser et corriger

L'éditeur doit fonctionner en `preview_only`. Comparez dessin et aperçu,
corrigez échelle, connexions, collisions potentielles, accessibilité, zones
vides et incohérences. Une prévisualisation verte ne prouve pas Godot.

## 6. Versionner la proposition

Conservez : image source, map-intent, sortie éditeur, version, hash, licence,
provenance, auteur, incertitudes et décision humaine.

Si aucun import visuel n'est disponible, le résultat valide est le dessin, la
proposition et une carte Kanboard bloquée. N'inventez ni fichier runtime ni ID
serveur.
