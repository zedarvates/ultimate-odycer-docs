# Surface relief: geometry, POM, and silhouettes

**Status: documentation reference.** Local performance: `unavailable`.
The reuse choices below are proposed `decision` items; this page validates no
shader, client, headset, or Asset Factory pipeline.

## Provenance and correction

The [initial Next Level Game Art video, dated April 9, 2026](https://www.youtube.com/watch?v=TUAyiCswYt4)
proposes Silhouette Parallax Occlusion Mapping as an explanation for Crimson
Desert. In the [May 5, 2026 correction](https://www.youtube.com/watch?v=44PT8XRZRGA),
the author revises that analysis toward Screen Space Displacement Mapping
(SSD/SSDM). Around 2:33 of the correction, the author still notes the lack of
studio confirmation. This attribution remains external analysis of BlackSpace.

The English automatic transcripts and metadata were reviewed on September 8,
2026. That review reproduces neither the author's measurements nor the game's
implementation. The technical references below describe their own methods;
they do not confirm the method used by Crimson Desert.

## Vocabulary and limits

| Technique | Intended effect | Limit to preserve |
| --- | --- | --- |
| Normal / bump mapping | Detail in the lighting response | Geometric outline stays unchanged |
| Simple parallax | View-dependent texture coordinate offset | Approximation, sensitive to grazing angles |
| POM | Intersection search in a height map | Per-pixel cost; conventional silhouette generally stays unchanged |
| Silhouette POM | Apparent outline treatment | Specific, more expensive variant; not a universal material switch |
| Geometry / vertex displacement | Changes to the rendered mesh | Suitable density and separately maintained collision representation |

References: [CryEngine POM](https://www.cryengine.com/docs/static/engines/cryengine-5/categories/23756816/pages/29450125),
[CryEngine Silhouette POM](https://www.cryengine.com/docs/static/engines/cryengine-5/categories/23756816/pages/29450143),
and [Three.js MeshStandardMaterial](https://threejs.org/docs/pages/MeshStandardMaterial.html).

SSD/SSDM here names the correction's analysis. Do not assume it excludes every
POM variant: height-map intersection search and depth writes can coexist.
[GPU Gems 3 chapter 18, by Policarpo and Oliveira](https://developer.nvidia.com/gpugems/gpugems3/part-iii-rendering/chapter-18-relaxed-cone-stepping-relief-mapping)
describes relief mapping with depth updates and self-shadowing. Modified depth
therefore does not prove tessellation. Implementation inference: changing the
depth of existing fragments alone does not create coverage beyond the mesh's
projected footprint.

## Reuse in clients

**Godot:** `heightmap_enabled` enables parallax and `heightmap_deep_parallax`
enables POM. With `uv1_triplanar`, standard-material height mapping is ignored.
Provide UVs for this first experiment. These options do not prove a BlackSpace
equivalent SPOM implementation.
[BaseMaterial3D](https://docs.godotengine.org/en/stable/classes/class_basematerial3d.html)

**Three.js:** `displacementMap` moves vertices; `bumpMap` affects lighting.
A POM variant needs a shader suited to the chosen backend and a fallback
material. Adding a displacement map does not supply that variant.
[MeshStandardMaterial](https://threejs.org/docs/pages/MeshStandardMaterial.html)

These engine pages were checked again on September 9, 2026. The `stable` and
Three.js documentation can change: record the version actually tested.

**Proposed `decision`:** keep structural volumes, openings, overhangs, and
contact areas in suitable geometry; compare POM on paving or a wall. The creator
can configure the visual profile. The server retains authority over world
state, collisions, and persistence, following the
[client boundary](../explanation/client-architecture.md).

For an Asset Factory candidate, retain silhouette, scale, UVs/tangents,
consistent height/normal maps, license, and hashes. This proposal adds no
capability to the existing pipeline.

## Evidence required before adoption

| Proposed comparison | Evidence to record |
| --- | --- |
| Normal only, available POM, moderate geometry | Same source relief, light, camera, resolution, and scale |
| Wall with a corner and opening, ground, passing object | Seams, silhouettes, contact, depth, and shadows |
| Repeated camera path | Separate CPU/GPU times, median and p95/p99 frame times, memory, video |
| Web profile | Compilation, fallback material, available resources, and reload without network |
| VR profile | Real headset, each eye, head motion, and temporal stability |

Attach engine/backend, browser, driver, and GPU versions plus asset/shader
hashes. Mark missing measurements `unavailable`; JavaScript duration is not
GPU time. Fewer triangles do not guarantee faster rendering. Retain negative
results too.

Adoption requires an observed visual gain within the client's total budget
and a fallback to the reference material. An absent variant remains
`not_implemented`. A desktop image validates neither offline operation nor VR.
These criteria apply to future material adoption; they add no blocker to
documentation or network integration PRs.

## Related pages

- [Creative production handbook](../tutorials/creative-production-handbook.md)
- [3D and material tools](3d-assets-materials-and-photogrammetry-tools.md)
- [Import, optimization, and provenance](import-optimization-licensing-and-provenance.md)
