# Outils pour mondes, cartes et structures

## Parcours recommandés

| Besoin | Gratuit/local | Alternative accessible | Professionnel |
|---|---|---|---|
| Carte dessinée | Krita, GIMP, Inkscape | Inkarnate | service cartographique spécialisé |
| Couches et routes | QGIS | Blender | Houdini |
| Terrain | QGIS + Blender | World Machine | Houdini |
| Ville | City Editor Lite | City Editor `[Scaffolding / Proxy]` | QGIS/Blender avec conversion |
| Architecture | Architecture Editor Lite | Blender | Maya/Houdini |
| Donjon | dessin + Dungeon Editor proxy | Blender/Inkarnate | pipeline procédural spécialisé |

## QGIS

Gratuit et open source. Recommandé pour points, lignes, polygones, routes,
rivières, régions, GeoJSON, rasters et données d'altitude. Une couche GIS reste
une source : elle doit être convertie vers un contrat monde validé.

## Blender

Gratuit et open source. Sert au blockout, terrain, bâtiments, UV, retopologie,
animation et conversion GLB. Les add-ons et assets importés conservent leurs
propres licences.

## Inkarnate

Service cloud freemium/abonnement. Utile pour une carte illustrée ; les droits
commerciaux dépendent du plan. L'image exportée reste une référence avant
conversion structurée.

## World Machine et Houdini

World Machine propose un niveau gratuit non commercial et des licences
commerciales. Houdini Apprentice est non commercial ; Indie et Commercial ont
des contraintes de revenus, formats et pipeline. Leurs heightmaps et meshes
doivent passer les gates terrain et Godot.

## Éditeurs Lite

- City Editor Lite valide CityConfig Lite et tracés bornés, sans Zig/Godot ;
- Architecture Editor Lite valide HouseBlueprint Lite, sans coûts, HP, assets,
  collision, HLOD, Godot, VR ou publication ;
- Creature Editor Lite ne traite pas les cartes.

## Sorties et gates

- PNG/JPEG/SVG : référence visuelle ;
- GeoJSON : donnée géographique à convertir ;
- PNG/EXR/RAW : heightmap à vérifier ;
- GLB : candidat 3D, pas preuve runtime ;
- JSON Lite : proposition contractuelle ;
- aperçu : preuve d'auteur locale uniquement.

Avant validation serveur, exigez version, schéma, hash, provenance, licence,
budget, revue humaine et preuve d'import isolée.
