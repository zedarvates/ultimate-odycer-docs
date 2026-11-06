# NeuroCore pour PNJ et créatures — axe expérimental

Statut : **recherche / non autoritaire / sans promotion automatique**.

## Intention

Explorer une couche de décision très légère, persistante et inspirée des réseaux spiking pour les décisions à haute fréquence des PNJ et monstres : vigilance, poursuite, esquive, fuite, regroupement, attaque locale et investigation.

Le but n'est pas de remplacer les LLM partout. Le but est de réserver les modèles coûteux aux tâches qui en ont réellement besoin : dialogue, raisonnement social, planification longue, interprétation d'événements inhabituels et connaissance ouverte.

## Architecture cible

```text
signaux du jeu
    ↓
NeuroCore réflexe
    ↓
action candidate
    ↓
validation autoritaire serveur
    ↓
combat / mouvement / animation

faible confiance ou événement complexe
    ↓
routeur cognitif
    ├─ petit modèle
    └─ LLM/VLM
```

NeuroCore ne reçoit aucune autorité directe sur l'économie, l'inventaire, les dégâts, les récompenses, les règles de quête ou l'état canonique du monde.

## État interne envisagé

Variables lentes compactes, spécifiques au type de créature : peur, douleur, faim, agressivité, curiosité, cohésion de groupe, mémoire de menace et éventuellement fatigue.

À terme, certaines de ces variables pourront jouer le rôle de neuromodulateurs analogues à la dopamine, sérotonine ou octopamine, mais seulement après benchmark du noyau simple.

## Programme expérimental

1. **F0 — scaffold SNN déterministe** : neurones à fuite, seuils, période réfractaire, état lent.
2. **F1 — sparsité / compression** : graphe creux, fixed-point, INT8/INT16, ablation de connexions.
3. **F2 — motifs biologiques ouverts** : importer seulement des sous-circuits de connectomes ouverts dont la provenance et la licence sont vérifiées.
4. **F3 — types chimiques** : neurotransmetteurs comme effets typés, pas seulement signe excitateur/inhibiteur.
5. **F4 — neuromodulation / plasticité** : signaux lents et adaptation locale bornée.
6. **F5 — distillation** : transformer les motifs utiles en contrôleurs minimaux propres au jeu.

Chaque étape doit être comparée à l'étape précédente. Aucun mécanisme biologique n'est conservé uniquement parce qu'il est biologiquement plausible.

## Benchmark obligatoire

Comparer au minimum :

- logique déterministe / Behaviour Tree ;
- NeuroCore flottant ;
- NeuroCore quantifié ;
- petit NN dense si pertinent ;
- escalade vers petit modèle/LLM pour les cas complexes.

Charges : 1, 100, 1 000 et 10 000 agents simulés.

Mesures : temps CPU/GPU, mémoire, décisions/s, divergence quantification, taux d'action acceptable, faux positifs dangereux, diversité comportementale, taux d'escalade et stabilité temporelle.

## Critère de promotion

Une version ne peut atteindre un client Godot/Three.js ou le serveur qu'après : tests reproductibles au head exact, bénéfice mesurable sur une charge cible, absence de régression sur les limites autoritaires et scénario de repli déterministe disponible.

Le premier prototype exécutable est suivi dans `ultimate-odycer-tools-suite`, PR expérimentale #25.
