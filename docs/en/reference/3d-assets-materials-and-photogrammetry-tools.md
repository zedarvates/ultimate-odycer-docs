# 3D assets, materials, and photogrammetry tools

## Recommended free/local path

- Blender: 3D modeling, sculpting, UV unwrapping, retopology, rigging, and GLB
  conversion;
- Material Maker: nodal procedural PBR material authoring and Godot export;
- Poly Haven: CC0 public domain HDRIs, textures, and 3D models;
- Meshroom: local open-source photogrammetry pipeline.

## Ultimate Odycer Tools Suite

Asset Factory produces GLB candidates, review snapshots, manifests, and checksum
hashes. Its `gaussian_splat` contracts accept FOVEA, PLY, or SPLAT formats, but
do not yet prove a reviewed splat generator, GPU sorting runtime, OpenXR, or
canonical client adoption.

## Professional alternatives

Adobe Substance 3D operates via subscription; Autodesk Maya via subscription,
Flex tokens, or Indie terms; ZBrush via subscription; SideFX Houdini across
Non-Commercial, Indie, or Commercial tiers. Always verify third-party assets,
plug-ins, and pipeline license boundaries.

## Photogrammetry best practices

Only photograph authorized subjects. Preserve original captures, metadata,
lighting conditions, and explicit consents. Clean meshes, retopologize, create
clean UV layouts, bake details, and verify scale before exporting.

## Minimal asset validation gate

- GLB/glTF preferred; OBJ/FBX for interchange;
- PBR textures: albedo, normal, roughness, metallic, ambient occlusion, height
  as needed;
- documented provenance, license, checksum hash, and manifest;
- polygon, texture resolution, material count, collision mesh, and LOD budgets;
- isolated Godot import check before any runtime integration.

## 2.5D variant: 3D models to multi-directional sprites

The proposed pipeline is `draft → control render → visual validation → sprite
atlas → client test → accepted`. It requires fixed orthographic cameras,
declared angle directions, normalized lighting, transparent backgrounds,
separated shadows, animations, and JSON sprite atlases. This pipeline remains
planned for the Three.js template; it is not a current capability of Asset
Factory.
