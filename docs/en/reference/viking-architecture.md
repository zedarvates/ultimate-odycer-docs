# Viking architecture — first sourced research set for Ultimate Odycer

Research date: **1 November 2026**. This first set covers houses, workshops, longhouses, earth-and-timber defences, gateways and bridges. It supports metric models with explicit provenance and uncertainty.

See [facts.jsonl](../../../examples/architecture/viking/facts.jsonl) and [sources.json](../../../examples/architecture/viking/sources.json). `uo-architecture-research/v1` is an **experimental research exchange format**, not an existing native wiki or RAG schema. These files do not establish ingestion, indexing, editor integration, Godot collisions or VR validation.

## Scope and houses

Choose region, site, phase and function before generating architecture. Hedeby trading houses, Icelandic farms and Danish royal fortresses are distinct references. Published dimensions are not always explicitly internal or external; preserve their stated scope, including maximum width.

| Reference | Published nominal plan, m |
|---|---:|
| Hedeby, 874+ prototype, mirrored reconstructions 1/7 | 12 × 5.5 |
| Hedeby, 882 workshop | 5.2 × 3.6 |
| Hedeby, small 880s workshop | 3.2 × 2.6 |
| Hedeby, 852 merchant house | 12.1 × 6.5 |
| Hedeby, tenth-century hall | 16.1 × 6.7 |
| Hedeby, 833 cloth merchant house | 16.3 × 6.2 |

Source: [Haithabu museum, current building notices](https://haithabu.de/de/dauerausstellung). Museum numbering and occupational interpretations have changed; retain names, dimensions and source version together.

For the **874+** prototype, surviving wall and gable evidence supports approximately **2 m walls** and a **40° roof pitch**, while the precise roof structure remains hypothetical: [museum interview with Dr Matthias Toplak](https://haithabu.de/de/die-wikinger-haeuser-im-freigelaende--ein-archaeologisches-langzeitexperiment). A simplified ridge calculation gives **4.308 m**, excluding covering and overhang; it is derived geometry, not a surveyed historical height.

[Ribe](https://www.ribevikingecenter.dk/en/explore/ripa-townhouses) provides a **17 × 5.25 m** building called the Inn, whose original purpose is unknown. Its Tvedgade house has no surviving roof evidence; three museum roofs explore alternatives. The [reconstructed Hviding farm](https://www.ribevikingecenter.dk/en/explore/viking-farm-buildings) includes a **35 × 8 m** longhouse and an excavated smithy approximately **3.5 × 4.5 m**.

The [Fyrkat reconstructed longhouse](https://www.vikingeskibsmuseet.dk/fagligt/e-laering/viden-om-vikingetiden/vikingetidens-geografi/runesten-og-billedsten/spor-efter-vikingerne/ringborgen-fyrkat) is **28.5 × 7.4 m**. The [1942 Trelleborg reconstruction](https://trelleborgvikingeborg.dk/en/events/activities/rent-the-long-house) is **29.6 × approximately 8 m**; the museum now identifies its vertical exterior supports as outdated, replacing that interpretation with inclined supports.

Keep Borg/Lofotr records separate: [UiT](https://arkitekturguide.uit.no/files/show/5399) gives **83 × 9.5 m** for excavated evidence; [Museum Nord](https://www.museumnord.no/en/exhibition/craftsmen/) gives **83 × 12 m** for the reconstruction completed in 1995. Do not average unresolved width conventions or infer an original roof height.

The [National Museum of Iceland submission published on UNESCO’s Tentative List](https://whc.unesco.org/fr/listesindicatives/5589/) describes internal timber roof supports, turf walls and roof, and a long-side entrance. The juxtaposed-gable `burstabær` form developed around **1800**, so its silhouette must not be backdated to a Viking preset. Tentative listing is not World Heritage inscription. This research set establishes no dimensioned Stöng longhouse plan.

## Defences and bridges

| Reference | Published information and limits |
|---|---|
| [Trelleborg explanatory planning document](https://en.natmus.dk/fileadmin/user_upload/Editor/natmus/Trelleborg/Vikinge_age_ring_fortresses/Trelleborg_districtplan_1224.pdf), pp.24–25 | Fixed bridge **17 × 3 m**; V ditch **17–18 m** wide, up to **4 m** deep; rampart base **17 m**. Walkway **3–4 m** high and parapet **+2 m** are reconstruction estimates. Exclude modern planning height limits. |
| [Aggersborg, Viking Ship Museum](https://www.vikingeskibsmuseet.dk/fagligt/undervisning/vikingeviden/vikingetidens-geografi/vikingetiden-i-skandinavien/aggersborg-og-lindholm-hoeje) and [site museum](https://aggersborg.com/en/the-ring-fortress/) | Inner diameter approximately **240 m**; rampart base **9 m**, height approximately **4 m**; **48** longhouses. This is a particular royal layout, not a village default. |
| [Danevirke Museum](https://danevirkemuseum.de/de/das-danewerk/) | Late eighth/early ninth-century fieldstone wall approximately **3 m** high, **3 m** wide and **4 km** long. Waldemar’s brick phase follows **1163** and belongs outside a tenth-century preset. |
| [Ravning heritage authority](https://slks.dk/doil/stederne/ravning-enge-bro-og-hulveje) | Around 980: bridge at least **760 m** long, approximately **5 m** wide, **280** bays. Posts up to **6 m** include buried length, not a six-metre deck height. |

Borgring needs publication-specific records. The [2017 article](https://www.cambridge.org/core/journals/antiquity/article/borgring-the-discovery-of-a-viking-age-ring-fortress/53F7E590702E0511A0B487D6C15E2686) gives an **outer diameter of 144 m**, rampart base **10.5–10.7 m** and north-gateway width **5 / 4.4 / 5 m** along its passage. The [2021 excavation synthesis](https://tidsskrift.dk/dja/article/download/121920/176010), pp.2–5,9,16–17, refines the diameter to **144.5 m**. Original rampart height remains unknown; approximately **3 m**, plus a possible **1.5–1.8 m** palisade, is a proposed profile. No contemporary interior buildings, timber roads or internal timber rampart framework were observed in the investigations described. Do not copy Fyrkat’s buildings into it. Ground elevation—approximately **8.5–9 m** north and **5–6 m** south above mean sea level—is distinct from rampart height.

The consulted Trelleborg and Ravning accounts do not document lifting mechanisms. Model the documented Trelleborg bridge as fixed; this is not a universal claim about the absence or invention date of drawbridges.

## Editor and knowledge rules

1. Attach every parameter to its site, phase, source and evidence category. Unknown values remain `null`.
2. Distinguish maximum and usable width; inner and outer diameter; preserved and proposed height; height and elevation. A bounding rectangle is not an exact curved floor area.
3. Label modelling choices such as wall thickness, overhang, openings, timber sections and post spacing as assumptions until a plan supports them.
4. Generate roof and structure from consistent axes and spans; check openings, supports, thresholds and intersections before decoration.
5. Record gameplay adaptations explicitly. A wider navigation doorway or added stair is not archaeological evidence.
6. Verify metric export, import, collisions, human scale and navigation in the actual target engine. A geometric preview cannot establish runtime correctness.

Further work covers dimensioned small farm plans; ports, quays and boardwalks; site-specific gateway sections; barns, storage, ovens, wells, latrines and boathouses; timber bridge joints; and independently dated medieval castle/drawbridge references. Map this exchange set to the existing wiki and recipe contracts, deduplicate by stable identifiers and read back committed results before claiming the active index has been enriched.
