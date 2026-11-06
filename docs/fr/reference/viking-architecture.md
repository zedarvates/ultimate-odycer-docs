# Architecture viking — première base sourcée pour Ultimate Odycer

Recherche du **1 novembre 2026**. Première vague : habitats, ateliers, longues maisons, défenses de terre et de bois, portes et ponts. Elle permet de construire des modèles métriques dont chaque paramètre possède une provenance et un degré de certitude.

Cette page accompagne [facts.jsonl](../../../examples/architecture/viking/facts.jsonl) et [sources.json](../../../examples/architecture/viking/sources.json). Le format `uo-architecture-research/v1` est un **format expérimental d’échange de recherche**, pas le schéma natif d’un wiki ou du RAG. Ces fichiers ne prouvent aucune ingestion, indexation, intégration dans l’éditeur, collision Godot ou validation en VR.

## Périmètre historique

Sélectionner d’abord **région, site, phase et fonction**. Une maison de marchand de Hedeby, une ferme islandaise et une forteresse royale danoise ne constituent pas un style unique interchangeable. Les fiches suivantes se rapportent principalement aux IXe–Xe siècles ; les prolongements postérieurs restent identifiés.

Les mots « château » et « muraille » dans le catalogue doivent permettre de retrouver les besoins de jeu sans importer automatiquement donjons, créneaux de pierre, herses ou ponts levants dans chaque recette viking. Pour cette vague, commencer par les défenses réellement documentées : terrassement, gazon, bois, passage de porte et accès fixe. Les formes médiévales postérieures peuvent devenir un autre lot, daté et sourcé.

## Habitats : métrique avant décoration

Dimensions en mètres. Les notices muséales ne précisent pas toujours la convention intérieur/extérieur ; les valeurs ci-dessous restent des **emprises nominales publiées**, souvent de largeur maximale, et non des surfaces habitables certifiées.

| Référence | Emprise publiée | Portée |
|---|---:|---|
| Hedeby, prototype 874+, maisons 1/7 | 12 × 5,5 | Deux variantes miroir du même prototype |
| Hedeby, atelier 882 | 5,2 × 3,6 | Planches verticales |
| Hedeby, petit atelier des années 880 | 3,2 × 2,6 | Madriers horizontaux |
| Hedeby, marchand 852 | 12,1 × 6,5 | Ossature intérieure |
| Hedeby, halle Xe siècle | 16,1 × 6,7 | Poteaux, sablières, planches |
| Hedeby, marchand textile 833 | 16,3 × 6,2 | Ossature et clayonnage |

Source : [musée de Haithabu, notices courantes](https://haithabu.de/de/dauerausstellung). La numérotation et certaines affectations anciennes ont changé : garder nom, dimensions et version de source ensemble. Les affectations professionnelles restent des interprétations.

La maison de **874+** constitue le premier modèle conseillé : murs d’environ **2 m**, pente de **40°**, appuyés sur des pans conservés ; la structure précise du toit reste hypothétique. Source : [entretien du musée avec Dr Matthias Toplak](https://haithabu.de/de/die-wikinger-haeuser-im-freigelaende--ein-archaeologisches-langzeitexperiment). Le faîtage simplifié calculé à partir de ces données est `2 + 2,75 × tan(40°) ≈ 4,308 m`, hors couverture et débord. Ce calcul ne devient pas une mesure archéologique.

À [Ribe](https://www.ribevikingecenter.dk/en/explore/ripa-townhouses), le bâtiment nommé « Inn » mesure **17 × 5,25 m**, mais sa fonction originale est inconnue. Le toit de la maison de Tvedgade n’est pas conservé : les trois variantes muséales illustrent des hypothèses. La [ferme de Hviding reconstituée](https://www.ribevikingecenter.dk/en/explore/viking-farm-buildings) possède une longue maison de **35 × 8 m** ; sa forge fouillée mesure environ **3,5 × 4,5 m**. Ne pas généraliser les usages supposés à toutes les maisons.

Pour les grandes halles, distinguer le [longhouse reconstruit de Fyrkat](https://www.vikingeskibsmuseet.dk/fagligt/e-laering/viden-om-vikingetiden/vikingetidens-geografi/runesten-og-billedsten/spor-efter-vikingerne/ringborgen-fyrkat), **28,5 × 7,4 m**, de celui de [Trelleborg reconstruit en 1942](https://trelleborgvikingeborg.dk/en/events/activities/rent-the-long-house), **29,6 × environ 8 m**. À Trelleborg, le musée corrige les supports verticaux du modèle ancien : les supports historiques étaient inclinés. Une photographie de reconstruction ne suffit donc pas comme plan définitif.

À Borg/Lofotr, conserver deux fiches : [UiT](https://arkitekturguide.uit.no/files/show/5399) publie **83 × 9,5 m** pour la fouille ; [Museum Nord](https://www.museumnord.no/en/exhibition/craftsmen/) publie **83 × 12 m** pour la reconstruction achevée en 1995. Les conventions de largeur ne sont pas conciliées ici ; ne pas les moyenner. Hauteur et structure exacte ne se déduisent pas de l’emprise.

En Islande, la [description déposée par le National Museum of Iceland sur la liste indicative UNESCO](https://whc.unesco.org/fr/listesindicatives/5589/) documente la longue maison à ossature intérieure, entrée latérale, murs et toiture de tourbe. La ferme à pignons juxtaposés `burstabær` se développe vers **1800** : sa silhouette ne doit pas être rétroprojetée dans un modèle viking. Cette liste indicative n’est pas une inscription au patrimoine mondial. Aucun plan coté de Stöng n’est établi dans ce lot.

## Approfondissement : volumes courbes et intérieurs

Le [panneau patrimonial SLKS de septembre 2011](https://slks.dk/fileadmin/user_upload/0_SLKS/Dokumenter/Fortidsminder_Diger/DOIL/KUAS_8190015_Skilte_Fyrkat_september2011_Low.pdf), **p.7 du PDF**, décrit la reconstruction de Fyrkat réalisée par Holger Schmidt dans les années 1980 : **28,5 m** de long, **7,5 m** au centre et **5 m** aux pignons, trois pièces, quatre entrées, foyer central et banquettes. La notice précédente à **7,4 m** reste une autre référence ; les largeurs ne sont pas moyennées.

Le [plan et la coupe de Schmidt, *Viking Age Buildings* (1990), fig.5, p.197, échelle 1:200](https://tidsskrift.dk/jda/article/download/127450/173733/269092) fournissent une référence graphique de reconstruction. Les porches latéraux y sont décalés vers des cloisons opposées ; cette relation n’établit pas leurs coordonnées. Le modèle paramétrique retient une **courbe parabolique choisie**, sans numérisation de ce plan. Hauteur de mur **2,2 m**, pente **45°**, croupes, sections de bois, ouvertures **1,1 × 1,9 m** et emplacement des cloisons sont des **hypothèses de modélisation**, pas des cotes relevées sur la figure. Aucune précision supérieure n’est déduite de sa seule échelle imprimée.

Pour le prototype Hedeby 874+, la [notice de la maison 7](https://haithabu.de/de/dauerausstellung) appuie trois compartiments, foyer, banquettes latérales et second accès extérieur. Leur géométrie détaillée et les sections ou espacements de charpente restent supposés. Les intérieurs et toitures amovibles servent à inspecter ces choix ; ils ne certifient ni la structure ni les collisions du jeu.

## Défenses : préserver la coupe et la phase

| Site et source | Données retenues | Limites à conserver |
|---|---|---|
| [Trelleborg, document communal hébergé au Musée national](https://en.natmus.dk/fileadmin/user_upload/Editor/natmus/Trelleborg/Vikinge_age_ring_fortresses/Trelleborg_districtplan_1224.pdf), p.24–25 | Pont fixe 17 × 3 m ; fossé en V de 17–18 m, profondeur jusqu’à 4 m ; rempart de base 17 m | Circulation à 3–4 m et parapet +2 m : estimations de restitution, pas mesures intactes ; maxima de permis modernes exclus |
| [Aggersborg, Viking Ship Museum](https://www.vikingeskibsmuseet.dk/fagligt/undervisning/vikingeviden/vikingetidens-geografi/vikingetiden-i-skandinavien/aggersborg-og-lindholm-hoeje) ; [musée du site](https://aggersborg.com/en/the-ring-fortress/) | Diamètre intérieur ≈240 m ; rempart de base 9 m et hauteur ≈4 m ; 48 longues maisons | Plan royal particulier ; hauteur approximative ; aucune forme de tour déduite |
| [Danevirke Museum](https://danevirkemuseum.de/de/das-danewerk/) | Mur de blocs fin VIIIe–début IXe siècle : environ 3 m de haut, 3 m de large, 4 km de long | Mur de briques de Waldemar après 1163 : autre phase, exclue du preset Xe siècle |
| [Ravning, autorité patrimoniale danoise](https://slks.dk/doil/stederne/ravning-enge-bro-og-hulveje) | Vers 980 : longueur au moins 760 m, largeur ≈5 m, 280 travées ; poteaux jusqu’à 6 m | Longueur totale des poteaux, partie enterrée incluse ; aucune hauteur de tablier de 6 m déduite |

### Borgring : conserver les publications successives

L’[étude de 2017](https://www.cambridge.org/core/journals/antiquity/article/borgring-the-discovery-of-a-viking-age-ring-fortress/53F7E590702E0511A0B487D6C15E2686) donne un diamètre **extérieur de 144 m**, une base de rempart **10,5–10,7 m** et un passage nord de largeur **5 / 4,4 / 5 m** selon sa profondeur.

La [synthèse des fouilles publiée en 2021](https://tidsskrift.dk/dja/article/download/121920/176010), p.2–5,9,16–17, précise le diamètre à **144,5 m**. La hauteur originale demeure inconnue ; un front proche de **3 m**, complété d’une possible palissade **1,5–1,8 m**, reste une proposition. Les maisons, rues de bois et ossatures internes du rempart attendues par comparaison n’ont pas été observées dans les investigations décrites. Ne pas compléter automatiquement avec les maisons de Fyrkat. L’altitude du **terrain** est distincte : environ **8,5–9 m** au nord, **5–6 m** au sud au-dessus du niveau marin moyen ; ce n’est pas la hauteur du rempart.

Le pont de Trelleborg décrit dans le document est fixe. Les notices retenues pour Trelleborg et Ravning ne documentent pas de mécanisme levant : cela borne le premier modèle, sans prétendre établir une absence universelle ou une date d’invention du pont-levis.

## Règles pratiques pour l’éditeur et le wiki

1. Associer chaque paramètre à un fait, sa source, sa phase et son statut : mesure archéologique publiée, reconstruction muséale, interprétation ou calcul dérivé. Une valeur inconnue reste `null` dans le corpus.
2. Distinguer largeur maximale, largeur utile, diamètre intérieur/extérieur, hauteur conservée, hauteur proposée et altitude. Un rectangle englobant calculé n’est pas la surface exacte d’un bâtiment courbe.
3. Exposer les hypothèses de modélisation : épaisseur, débord, dimensions de porte, position des poteaux, tracé courbe et sections du bois ne deviennent pas des cotes historiques faute de plan.
4. Générer la toiture et sa charpente depuis les mêmes axes et portées ; contrôler le passage des portes, les seuils, les appuis et les intersections. Éviter de recouvrir un mauvais raccord par de la décoration.
5. Séparer preuve historique, géométrie numérique et adaptation de jeu. Une porte élargie pour la navigation ou un escalier ajouté reste une adaptation explicite.
6. Vérifier en unités métriques, puis contrôler l’import, les collisions, l’échelle humaine et la navigation dans le moteur réellement ciblé. Un export JSON ou un aperçu géométrique ne valide pas ces points.

## Suite du catalogue

| Lot | Références déjà amorcées | Recherche à terminer avant recette fidèle |
|---|---|---|
| Maisons villageoises | Hviding, Hedeby et Islande | Plans de petites fermes, dépendances, murs et ouvertures cotés |
| Port et ville | Hedeby, Ribe | Quais, embarcadères, chemins de planches, parcelles, drainage et entrepôts ; phases séparées |
| Forteresses | Trelleborg, Fyrkat, Aggersborg, Borgring | Plans de portes, coupes locales, matériaux et niveaux de preuve par site |
| Annexes | Forge Hviding, ateliers Hedeby | Étable, stockage, four, puits, latrines et hangar à bateau ; fonction attestée ou supposée |
| Ponts et levage | Trelleborg et Ravning | Assemblages, sections et niveaux ; références datées propres pour tout pont-levis |
| Extension médiévale | Phases postérieures de Danevirke | Châteaux et mécanismes spécifiques avec dossiers distincts |

Le corpus conserve les réserves au niveau de chaque fait. La prochaine intégration doit mapper ces faits vers le contrat existant du wiki et des recettes, dédupliquer par identifiants stables, puis relire le résultat enregistré. L’index actif n’est pas annoncé comme enrichi par la seule présence de ce dossier.
