# World, map, and structure tools

## Recommended production paths

| Need | Free / Local | Accessible Alternative | Professional |
|---|---|---|---|
| Hand-drawn map | Krita, GIMP, Inkscape | Inkarnate | Specialized cartography service |
| Layers and roads | QGIS | Blender | Houdini |
| Terrain | QGIS + Blender | World Machine | Houdini |
| City layout | City Editor Lite | City Editor `[Scaffolding / Proxy]` | QGIS/Blender with conversion |
| Architecture | Architecture Editor Lite | Blender | Maya/Houdini |
| Dungeon | Dungeon Editor Lite | Blender/Inkarnate | Specialized procedural pipeline |

## QGIS

Free and open source. Recommended for points, lines, polygons, roads, rivers,
regions, GeoJSON layers, rasters, and elevation datasets. A GIS layer remains a
source artifact: it must be converted into a validated world contract before
engine use.

## Blender

Free and open source. Used for blockouts, terrain sculpting, buildings, UV
unwrapping, retopology, animation, and GLB conversion. Add-ons and imported
assets retain their respective independent licenses.

## Inkarnate

Freemium/subscription cloud service. Useful for illustrated conceptual maps;
commercial rights depend on the active plan. Exported images remain visual
references until converted into structured formats.

## World Machine and Houdini

World Machine offers a free non-commercial tier and commercial licenses. Houdini
Apprentice is non-commercial; Indie and Commercial tiers enforce revenue caps,
formats, and pipeline limits. Generated heightmaps and meshes must pass terrain
and Godot import gates.

## Lite Editors

- City Editor Lite validates CityConfig Lite parameters and bounded layouts,
  without Zig or Godot runtime dependencies;
- Architecture Editor Lite validates HouseBlueprint Lite floorplans, without
  costs, HP, custom assets, collision, HLOD, Godot, VR, or server publication;
- Dungeon Editor Lite validates Dungeon Blueprint Lite rooms, without rewards,
  loot tables, species spawning, custom meshes, props, Zig loaders, or server
  publication;
- Creature Editor Lite does not handle maps.

## Artifacts and validation gates

- PNG/JPEG/SVG: visual design reference;
- GeoJSON: geographic spatial data requiring conversion;
- PNG/EXR/RAW: heightmap requiring validation;
- GLB: 3D model candidate, not runtime proof;
- JSON Lite: structured contract proposal;
- preview: local authoring proof only.

Before server validation, require version, schema, checksum hash, provenance,
license, polygon/texture budget, human review, and isolated engine import proof.
