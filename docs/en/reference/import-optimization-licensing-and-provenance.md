# Import, optimization, licensing, and provenance

## Preferred asset formats

- 3D models: GLB/glTF preferred; OBJ/FBX for intermediate conversion;
- Gaussian splats: FOVEA, PLY, or SPLAT only if the receiving contract accepts
  them;
- Terrain and elevation: PNG, EXR, or RAW depending on terrain engine requirements;
- 2D images and UI: PNG, SVG; audio: WAV/FLAC masters, OGG/WAV for runtime;
- Structured data: versioned JSON, controlled intermediate CSV.

## Technical optimization checklist

Verify world units, pivot orientation, coordinate axes, UV mapping, material
slots, texture resolutions, compression formats, mipmap generation, LOD levels,
collision shapes, navigation mesh tagging, occlusion culling, streaming chunks,
animation tracks, CPU/GPU memory footprint, and load times. Always separate
compilation, headless asset import, GPU rendering, XR support, and network
replication proofs.

## Licensing and provenance records

For every asset, record: author, source URL, download date, license terms,
active service plan, foundation model/dataset used, modifications made, authoring
tools, generation prompts, actor consents, and SHA-256 checksum hash. A software
tool license does not automatically license generated or imported third-party
content.

## Public release gate

1. Schema validation and format compliance;
2. License clarity and commercial use permissions;
3. Absence of confidential secrets or prohibited content;
4. Checksum hash and manifest registration;
5. Polygon, texture, and memory budgets;
6. Human operator visual and functional review;
7. Isolated Godot import test;
8. Authoritative server validation.

A failed gate retains the candidate status and negative test proof; an asset
never becomes `runtime_ready` through manual renaming.
