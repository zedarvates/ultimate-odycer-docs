# Liste d'acceptation de la mise en route locale

Une case n'est cochée que si vous possédez la preuve indiquée. Utilisez
`non applicable`, `blocked` ou `unavailable` plutôt qu'une réussite inventée.

## Projet

- [ ] La fiche de projet décrit la boucle de jeu, les joueurs et l'échelle.
- [ ] Le moteur et le template sont nommés avec leur statut réel.
- [ ] La topologie choisie est justifiée.
- [ ] Le profil matériel est marqué `estimated` ou `observed`.

## Release

- [ ] La page officielle listait réellement l'archive.
- [ ] Le SHA-256 téléchargé correspond exactement.
- [ ] La version serveur correspond à la documentation embarquée.
- [ ] Les modules optionnels appartiennent à la même famille de compatibilité.

## PostgreSQL

- [ ] PostgreSQL est sain.
- [ ] Le volume nommé persiste après redémarrage.
- [ ] Les journaux confirment PostgreSQL, sans repli SQLite actif.
- [ ] Un dump existe hors du volume Docker.
- [ ] Le SHA-256 du dump correspond.
- [ ] La restauration dans la base de contrôle a réussi.

## Serveur et réseau

- [ ] Les services de login et de jeu démarrent depuis l'archive vérifiée.
- [ ] Le contrôle de santé répond sainement.
- [ ] Le WebAdmin local répond s'il a été installé.
- [ ] Aucun port Internet n'a été ouvert automatiquement.
- [ ] Les secrets n'apparaissent ni dans les journaux ni dans les prompts LM.

## Godot

- [ ] Le dépôt contient un vrai projet Godot compatible.
- [ ] Le client atteint le login puis le serveur de jeu local.
- [ ] Un personnage de test entre dans le monde.
- [ ] L'avatar est visible et effectue une action minimale autorisée.
- [ ] Les journaux client et serveur ne contiennent pas d'erreur fatale.

## Redémarrage

- [ ] Les services s'arrêtent proprement.
- [ ] La configuration survit au redémarrage.
- [ ] Les données de test attendues persistent dans PostgreSQL.

## Verdict

- **Réussi :** toutes les cases applicables sont prouvées.
- **Partiel :** le serveur local fonctionne, mais un composant optionnel manque.
- **Bloqué :** une release, un template jouable ou une dépendance obligatoire
  n'est pas disponible.
- **Échec :** un contrôle obligatoire a produit une preuve négative.

La validation de cette documentation ne coche aucune case runtime à votre
place.
