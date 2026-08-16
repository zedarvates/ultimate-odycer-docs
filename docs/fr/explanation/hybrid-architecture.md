# Pourquoi séparer serveur, LLM et ESP32

Un home lab économique fonctionne mieux lorsque chaque appareil reçoit une tâche
adaptée à ses limites.

```text
événement du jeu
      ↓
serveur autoritaire ── valide intention, règles et conséquences
      ↓
paquet d'expression borné ── émotion, intensité, archétype, graine
      ↓
mini-PC ou ESP32 ── produit texte court, variation ou son
      ↓
validation de sortie ── accepte ou remplace par un patron déterministe
      ↓
présentation au joueur
```

## Le serveur garde l'autorité

Le LLM ne décide pas des dégâts, récompenses, inventaires, déplacements ou droits
d'accès. Il produit une expression à partir d'une intention déjà validée. Une
sortie invalide n'est jamais transformée directement en action de jeu.

## L'ESP32 devient un nœud d'expression

Un ESP32 classique convient aux patrons, grognements, sons et petits
classificateurs. Un ESP32-S3 avec PSRAM peut explorer un vocabulaire génératif
très fermé. La microSD stocke sons et profils, mais ne remplace pas la RAM.

## Le mini-PC partage le dialogue

Un mini-PC x86 16 Go peut héberger un modèle local partagé par plusieurs PNJ.
Les identités et historiques restent séparés, tandis que les générations passent
dans une file commune. Acheter un ordinateur par PNJ serait plus cher sans
résoudre le problème des conversations simultanées.

## Le repli déterministe protège l'expérience

Chaque intention importante possède une réponse sûre sans LLM. Le joueur obtient
ainsi une réaction même lorsque le modèle est lent, indisponible ou refusé. Cette
architecture permet d'expérimenter avec du matériel peu coûteux sans donner au
modèle une responsabilité qu'il ne peut pas garantir.
