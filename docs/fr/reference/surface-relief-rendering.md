# Relief de surface : géométrie, POM et silhouettes

**Statut : référence documentaire.** Performances locales : `unavailable`.
Les choix de réemploi ci-dessous sont des `decision` proposées ; aucun shader,
client, casque ou pipeline Asset Factory n'est validé par cette fiche.

## Provenance et correction

La [vidéo initiale de Next Level Game Art, du 9 avril 2026](https://www.youtube.com/watch?v=TUAyiCswYt4)
avance une hypothèse de Silhouette Parallax Occlusion Mapping pour Crimson
Desert. Dans son [correctif du 5 mai 2026](https://www.youtube.com/watch?v=44PT8XRZRGA),
l'auteur réoriente son analyse vers le Screen Space Displacement Mapping
(SSD/SSDM). Vers 2:33 du correctif, il indique encore l'absence de confirmation
du studio. Cette attribution reste une analyse externe du moteur BlackSpace.

Les transcriptions automatiques anglaises et les métadonnées ont été examinées
le 8 septembre 2026. Cet examen ne reproduit ni les mesures de l'auteur ni
l'implémentation du jeu. Les références techniques ci-dessous décrivent leurs
propres méthodes ; elles ne confirment pas celle de Crimson Desert.

## Vocabulaire et limites

| Technique | Effet recherché | Limite à conserver |
| --- | --- | --- |
| Normal / bump mapping | Détail dans la réponse lumineuse | Contour géométrique inchangé |
| Parallax simple | Décalage des coordonnées de texture selon la vue | Approximation, sensible aux angles rasants |
| POM | Intersection recherchée dans une carte de hauteur | Coût par pixel ; silhouette classique généralement inchangée |
| Silhouette POM | Traitement du contour apparent | Variante spécifique et plus coûteuse ; pas un simple réglage universel |
| Géométrie / déplacement de sommets | Modification du maillage rendu | Densité adaptée et représentation des collisions à traiter séparément |

Références : [CryEngine POM](https://www.cryengine.com/docs/static/engines/cryengine-5/categories/23756816/pages/29450125),
[CryEngine Silhouette POM](https://www.cryengine.com/docs/static/engines/cryengine-5/categories/23756816/pages/29450143)
et [Three.js MeshStandardMaterial](https://threejs.org/docs/pages/MeshStandardMaterial.html).

SSD/SSDM désigne ici l'analyse du correctif. Ne pas opposer automatiquement ce
nom à toutes les variantes POM : recherche dans une heightmap et écriture de
profondeur peuvent se combiner. Le [chapitre 18 de GPU Gems 3, par Policarpo et Oliveira](https://developer.nvidia.com/gpugems/gpugems3/part-iii-rendering/chapter-18-relaxed-cone-stepping-relief-mapping)
décrit un relief mapping avec mise à jour de profondeur et auto-ombrage.
Une profondeur modifiée ne prouve donc pas une tessellation. Déduction
d'implémentation : changer la profondeur des fragments existants ne crée pas,
à lui seul, une couverture au-delà de l'emprise projetée du maillage.

## Réemploi dans les clients

**Godot :** `heightmap_enabled` active le parallax et
`heightmap_deep_parallax` le POM. Avec `uv1_triplanar`, le height mapping du
matériau standard est ignoré. Prévoir des UV pour ce premier essai. Ces options
ne prouvent pas un SPOM équivalent à BlackSpace.
[BaseMaterial3D](https://docs.godotengine.org/en/stable/classes/class_basematerial3d.html)

**Three.js :** `displacementMap` déplace les sommets ; `bumpMap` agit sur
l'éclairage. Une variante POM exige un shader adapté au backend retenu et un
matériau de repli. Elle n'est pas fournie par l'ajout d'une displacement map.
[MeshStandardMaterial](https://threejs.org/docs/pages/MeshStandardMaterial.html)

Ces pages moteur ont été revérifiées le 9 septembre 2026. Les documentations
`stable` et Three.js évoluent : consigner la version réellement testée.

**`decision` proposée :** garder les volumes structurants, ouvertures,
surplombs et zones de contact en géométrie adaptée ; comparer le POM sur un sol
pavé ou un mur. Le profil visuel reste configurable par le créateur. Le serveur
conserve l'autorité sur l'état du monde, les collisions et la persistance,
selon la [frontière client](../explanation/client-architecture.md).

Pour un candidat Asset Factory, conserver silhouette, échelle, UV/tangentes,
cartes height/normal cohérentes, licence et empreintes. Cette proposition
n'ajoute pas de capacité au pipeline existant.

## Preuves nécessaires avant adoption

| Comparaison proposée | Éléments à consigner |
| --- | --- |
| Normale seule, POM disponible, géométrie modérée | Même relief source, lumière, caméra, résolution et échelle |
| Mur avec angle et ouverture, sol, objet passant devant | Coutures, silhouettes, contact, profondeur et ombres |
| Parcours caméra répété | Temps CPU/GPU distincts, frame médiane et p95/p99, mémoire, vidéo |
| Profil Web | Compilation, matériau de repli, ressources disponibles et rechargement sans réseau |
| Profil VR | Casque réel, chaque œil, mouvements de tête et stabilité temporelle |

Associer aux résultats les versions moteur/backend, navigateur, pilote, GPU et
empreintes des assets/shaders. Marquer toute mesure absente `unavailable` ; une
durée JavaScript n'est pas une mesure GPU. Moins de triangles ne garantit pas
un rendu plus rapide. Conserver aussi les résultats défavorables.

L'adoption exige un gain visuel observé dans le budget total du client et un
repli vers le matériau de référence. Une variante absente reste
`not_implemented`. Une image desktop ne valide ni le hors ligne ni la VR.
Ces critères concernent une future adoption du matériau ; ils n'ajoutent pas
de blocage aux PR d'intégration documentaire ou réseau.

## Pages liées

- [Manuel de production créative](../tutorials/creative-production-handbook.md)
- [Outils 3D et matériaux](3d-assets-materials-and-photogrammetry-tools.md)
- [Import, optimisation et provenance](import-optimization-licensing-and-provenance.md)
