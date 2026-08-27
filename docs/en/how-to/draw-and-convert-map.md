# Draw a map and prepare its conversion

You can start on paper, tablet, Krita, GIMP, Inkscape, QGIS, or any tool capable
of exporting a legible image. The LLM produces a structured proposal, not an
authoritative map.

## 1. Prepare the drawing

Include:

- north or orientation indicator;
- scale, or the explicit note "unknown scale";
- world boundary or playable limits;
- expected terrain relief and elevation;
- water bodies, roads, districts, regions, and landmarks;
- building footprints;
- entrances, exits, portals, and level transitions;
- spawn, quest, hazard, and safe zones;
- legend, color coding, and uncertain areas.

Export as PNG, JPEG, or SVG. Preserve the original source file and its rights.

## 2. Provide context to the LLM

Add your project brief, chosen world topology (`flat_map`, `planet`,
`mega_planet`, or `solar_system`), and the known scale or resolution.

```text
Analyze this map as an Ultimate Odycer proposal.
Do not invent invisible information. Separate direct observations,
interpretations, proposed decisions, and uncertainties. Extract orientation,
scale, boundaries, relief, water, roads, regions, landmarks, buildings,
transitions, and gameplay zones. Produce a draft uo.map-intent/v1 without
modifying any workspace file or publishing to the server. Request my explicit
validation before any subsequent conversion step.
```

## 3. Produce the structured proposal

The output must contain at least:

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

This contract remains documentary until an officially validated public schema
is published.

## 4. Choose an editor

- City Editor Lite: CityConfig parameters and bounded block layouts;
- Architecture Editor Lite: multi-level building floorplans without runtime;
- Creature Editor Lite: out of scope for maps;
- Full City/Architecture/Dungeon editors: prototypes or scaffolding proxy surfaces;
- QGIS/Blender: external spatial preparation requiring explicit conversion.

## 5. Preview and correct

The editor must run in `preview_only` mode. Compare the drawing and the
preview, then adjust scale, connections, potential collisions, accessibility,
empty areas, and inconsistencies. A green local preview does not prove Godot
runtime compatibility.

## 6. Version the proposal

Record: source image, map-intent document, editor output, version, checksum hash,
license, provenance, author, uncertainties, and human decision.

If no visual importer is currently available, the valid result is the drawing,
the structured proposal, and a blocked Kanboard card. Do not invent runtime files
or server entity IDs.
