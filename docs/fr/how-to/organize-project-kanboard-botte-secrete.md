# Organiser le projet avec Kanboard et Botte Secrète

Kanboard conserve le travail visible. Botte Secrète prépare et route les tâches
assistées par LM. Aucun des deux ne publie automatiquement au serveur.

## Tableau recommandé

Colonnes : `Idées → Conception → Prêt → En cours → Revue → Validation → Bloqué
→ Terminé`.

Swimlanes : monde/cartes, client Godot, serveur, Tools Suite, 3D/matériaux,
personnages/animation, audio, UI/VFX/vidéo, documentation/releases.

## Modèle de carte

```markdown
## Objectif observable
## Entrées autorisées
## Outil retenu et alternatives
## Formats et conversion
## Licence, provenance et confidentialité
## Critères d'acceptation
## Preuves attendues
## Prompt LM sans secret
## Blocage actuel
```

Joignez des liens et hashes plutôt que des secrets ou dumps. Sauvegardez la
base Kanboard et ses pièces jointes. Les plug-ins sont optionnels : le catalogue
officiel ne garantit pas une revue centralisée de leur code.

## Passage par Botte Secrète

```text
carte Kanboard
→ politique et capacités Botte Secrète
→ prompt borné
→ outil déterministe, LM local ou cloud
→ validation et preuve
→ déplacement humain de la carte
```

Botte Secrète peut réduire contexte/logs, choisir le niveau d'effort, trouver
skills et outils, surveiller budget et lancer le checkup. Elle ne transforme pas
une sortie locale en preuve fiable sans validation.

## API Kanboard

Par défaut, aucune mutation automatique. Une future intégration doit commencer
en lecture seule, utiliser HTTPS hors local, stocker le jeton hors prompts,
préférer l'API utilisateur avec permissions, être idempotente et demander
confirmation avant création ou déplacement. L'API applicative donne accès à
toutes les procédures sans contrôles de permissions projet : elle n'est pas le
choix par défaut.

## Prompt de routage

```text
À partir de cette carte Kanboard sans secret, classe la tâche comme outil
déterministe, LM local ou raisonnement cloud. Réduis-la au plus petit résultat
testable. Liste entrées, sorties, preuves et risques. Ne modifie pas Kanboard.
Demande confirmation avant upload, achat, suppression, réseau, déploiement ou
publication.
```
