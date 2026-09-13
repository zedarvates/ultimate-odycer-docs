# Scientific transfer roadmap / Feuille de route scientifique

Updated / Mise à jour : 2026-09-10. Category / Catégorie : explanation / explication.

## English

**decision:** evaluate physical prediction, structural drawing and material
fitting through reproducible offline experiments before considering game integration.

| Order | Planned work | Admission evidence |
| --- | --- | --- |
| 1 | Version observation/constraint inputs | Units, frames, stable identities, provenance and schema rejection tests |
| 2 | Evaluate physical reference trajectories | Time-step refinement, boundaries and independent reference comparisons |
| 3 | Evaluate learned prediction against persistence, constant velocity and affine baselines | Held-out scenes, errors by horizon, drift, failures and stated resource conditions |
| 4 | Import reviewed drawings, geometry and appearance candidates | Structure and identity preserved; hashes, licenses, budgets and deterministic round-trip |
| 5 | Consider a runtime adapter | Server authority, replay, divergence handling and fallback demonstrated in the owning runtime |

- [ ] Start with a small synthetic interchange specification after numerical validation.
- [ ] Preserve the proprietary server's authority over gameplay, identity, economy and publication.
- [ ] Report visual plausibility separately from physical accuracy and learned competence.

**observed:** an initial external [CogniARC particle-neighbour experiment](https://github.com/zedarvates/cogniarc/blob/a4aac4a5f42e546c4a4ad777c508e4a1b0f0f136/experiments/particle_graph/README.md)
contains source, focused tests and a reproducible dimensionless fixture.
Its report states Python, OS, architecture and workload. It is not a speed or
capacity measurement.

**unavailable:** calibrated water validation, a trained physical predictor,
production integration, server benchmarks and hardware-capacity gains.
This documentation change modifies no proprietary server or client runtime.

Sources: [SPH reference, Müller et al. (2003)](https://matthias-research.github.io/pages/publications/sca03.pdf),
[learned graph simulation, Sanchez-Gonzalez et al. (2020)](https://arxiv.org/abs/2002.09405),
[DiffVG (2020)](https://people.csail.mit.edu/tzumao/diffvg/).

## Français

**decision :** évaluer prédiction physique, dessin structuré et ajustement des
matériaux dans des expériences hors ligne reproductibles avant une intégration au jeu.

| Ordre | Travail planifié | Preuves d'admission |
| --- | --- | --- |
| 1 | Versionner les observations et contraintes | Unités, repères, identifiants stables, provenance et rejets de schéma |
| 2 | Évaluer les trajectoires physiques de référence | Raffinement du pas de temps, frontières et comparaison indépendante |
| 3 | Comparer la prédiction apprise à la persistance, vitesse constante et modèle affine | Scènes réservées, erreurs par horizon, dérive, échecs et ressources explicites |
| 4 | Importer dessins, géométrie et apparence après revue | Structure, identités, empreintes, licences, budgets et aller-retour déterministe |
| 5 | Envisager un adaptateur au runtime | Autorité serveur, rejeu, gestion des divergences et repli démontrés dans le runtime concerné |

- [ ] Commencer par une petite spécification d'échange synthétique après validation numérique.
- [ ] Préserver l'autorité du serveur propriétaire sur le jeu, l'identité, l'économie et la publication.
- [ ] Séparer plausibilité visuelle, exactitude physique et compétence apprise.

**observed :** un premier [banc CogniARC de particules voisines](https://github.com/zedarvates/cogniarc/blob/a4aac4a5f42e546c4a4ad777c508e4a1b0f0f136/experiments/particle_graph/README.md)
contient code, tests ciblés et cas synthétique reproductible sans dimension.
Son rapport précise Python, système, architecture et charge. Il ne mesure ni
vitesse ni capacité.

**unavailable :** validation sur de l'eau réelle, prédicteur physique entraîné,
intégration en production, benchmark serveur et gain de capacité matérielle.
Cette contribution ne modifie aucun runtime serveur propriétaire ou client.

Sources : [référence SPH, Müller et al. (2003)](https://matthias-research.github.io/pages/publications/sca03.pdf),
[simulation par graphe appris, Sanchez-Gonzalez et al. (2020)](https://arxiv.org/abs/2002.09405),
[DiffVG (2020)](https://people.csail.mit.edu/tzumao/diffvg/).
