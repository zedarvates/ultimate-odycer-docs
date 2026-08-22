# Pipeline d'agents PNJ

Statut : `decision` pour la conception publique local-first ; le câblage
runtime d'une pile PNJ de production reste non publié. Cette page prolonge
[l'architecture hybride](hybrid-architecture.md) sans transformer un banc
home lab en revendication d'IA de gameplay.

## Pipeline

```text
événement du monde ou parôle du joueur
        |
        v
perception serveur et contrôle de règles
        |  distance, faction, cooldowns, permissions, sûreté
        v
sélecteur de comportement
        |  déterministe d'abord : FSM, arbre de comportement, réponse
        |  en cache, k-NN / micro-modèle, ou script valide
        v
expression LLM optionnelle et bornée
        |  pré-prompt : rôle, tranche de mémoire, style, budget jetons
        |  post-prompt : schéma, actions interdites, longueur, sûreté
        v
validation de sortie
        |  accepter, réparer, ou remplacer par un repli déterministe
        v
présentation joueur et expression ESP32 optionnelle
```

Le LLM ne décide jamais des dégâts, récompenses, inventaires, déplacements
ou droits d'accès. Il exprime une intention déjà validée. Une sortie
invalide ne devient jamais une action de jeu directement.

## Couches de comportement

| Couche | Rôle | Autorité |
|---|---|---|
| Règles et perception | Ce PNJ peut-il agir, voir ou parler ? | serveur |
| FSM / arbre de comportement | Quel type d'acte est légal maintenant ? | serveur ou données validées |
| Mémoire / RAG | Quelles notes peuvent colorer la réponse ? | récupérées, puis filtrées |
| Modèle local (GGUF / ONNX / TensorRT) | Comment la réplique est-elle formulée ? | expression seulement |
| Modèle cloud | Identique au local, avec un coût et un risque vie privée plus élevés | expression seulement, optionnel |
| Cache | Réutiliser une réponse validée pour le même paquet | ne saute jamais la validation pour toujours |
| Repli deterministe | Garder le monde vivant si l'inférence échoue | obligatoire |

k-NN, micro-réseaux et RAG sont un assaisonnement optionnel. Ils ne passent
pas au-dessus des règles serveur. Une mémoire récupérée qui demande de l'or,
des objets ou un accès est écartée.

## Maîtrise des coûts local-first

Pour un home lab :

- garder les listeners en boucle locale sauf conception LAN privée explicite ;
- partager un modèle local entre beaucoup de PNJ au lieu d'un processus par PNJ ;
- budgéter les jetons par paquet : rôle, mémoire courte, une intention, sortie courte ;
- mettre en cache les paquets d'expression identiques ;
- sérialiser les flux d'inférence et garder de la marge, comme dans les
  guides de capacité PNJ ;
- basculer en fail-closed vers un grognement, un geste ou une réplique
  prête si le modèle est lent.

Les modèles cloud sont un débordement optionnel, pas la source de vérité par
défaut. Ils héritent du même schema, des mêmes interdits et de la même
validation. Coûts, journaux et prompts doivent rester sans secrets joueur.

## Mémoire et dialogue

La mémoire PNJ est une tranche filtrée, pas un dump de la base monde. Une
conception publique DEVRAIT conserver :

- l'identite et l'activité courante ;
- un court résumé de relation ;
- la dernière intention joueur acceptée ;
- aucun inventaire, monnaie ou dump de lore non publié.

Le dialogue est de la présentation. Les drapeaux de quête, les changements
de réputation et les dons d'objets restent dans les
[systèmes de gameplay](../reference/gameplay-systems.md) possédés par le
serveur.

## Pages liées

- [Architecture hybride](hybrid-architecture.md)
- [Mesurer la capacité PNJ](../how-to/measure-npc-capacity.md)
- [Exploiter un home lab](../how-to/operate-a-home-lab.md)
