# Services Obolune fondés sur les résultats

Statut : direction commerciale DÉCIDÉE / implémentation des capacités variable selon le service.

## Règle
**Complexité à l’intérieur. Simplicité à l’extérieur. Preuves à la sortie.**

Les clients achètent des résultats, pas des noms de composants internes. SYSTAI, StoryCore, Botte Secrète, Parcimonia, les Knowledge Graphs, modèles et adaptateurs restent des détails d’implémentation, sauf lorsqu’une inspection technique est utile.

Un libellé commercial NE DOIT PAS laisser entendre qu’une capacité est éprouvée en production quand sa capacité sous-jacente est seulement PROPOSÉE ou EXPÉRIMENTALE.

## Quatre points d’entrée principaux

### Build My Game
Pour créer ou étendre du contenu et des systèmes jouables. SYSTAI interprète l’intention et propose la composition appropriée de capacités éprouvées/expérimentales selon la politique du projet.

### Build My Story
Point d’entrée centré sur StoryCore pour le travail narratif et le contenu de jeu :
- Game Lore Builder
- Story Builder
- Character Builder
- Act Builder
- Scene Builder
- Quest Builder
- Dialogue Builder
- Campaign Builder
- World Story Builder
- Story-to-Game
- Lore & Quest Checker

Ces noms décrivent des résultats côté client. Chacun exige une carte de statut des capacités distincte fondée sur les preuves StoryCore réelles.

### Optimize My Game
Les services candidats comprennent Online Game Optimizer, Game Server Optimizer, Game Performance, Game Asset Optimizer et Game AI Cost/Latency Optimizer. Les affirmations avant/après exigent des preuves mesurées comparables.

### Check My Game
Services orientés QA, cohérence et publication : vérifications du jeu/de la publication, cohérence lore/quêtes, compatibilité, provenance/licence, sécurité et préparation des preuves selon le périmètre de capacités démontré.

## Parcours client
Intention client -> point d’entrée de service simple -> clarification SYSTAI -> politique/budget du projet -> graphe de capacités/travail proposé -> travail/preuves -> rapport de résultat pour le client.

## Preuves
Les services d’optimisation et de contrôle doivent retourner un rapport Avant/Après ou Constats/Preuves :
- référence et contexte de mesure ;
- changements ou constats exacts ;
- mesures après changement lorsqu’elles sont comparables ;
- zones inchangées et inconnues ;
- preuves/tests ;
- coût/temps consommé ;
- réserves ;
- éléments nécessitant une revue humaine.

## Frontières
GitHub reste canonique pour les modèles, schémas et documentations techniques ouverts. Obolune présente les produits/services et renvoie aux sources techniques lorsque cela est utile. La présentation commerciale ne doit pas transformer Obolune en registre.
