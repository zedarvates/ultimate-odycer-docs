# Index avancé de la mise en route locale

Cet index fournit des raccourcis. Chaque commande renvoie vers la page qui
explique ses préconditions et son interprétation.

| Objectif | Raccourci | Source |
|---|---|---|
| Choisir moteur et monde | Lire la matrice | [Matrice](engine-template-world-matrix.md) |
| Vérifier WSL et Docker | `wsl --version`, `docker version`, `docker compose version` | [Windows](../how-to/install-local-server-windows.md) |
| Vérifier l'archive | `Get-FileHash -Algorithm SHA256` | [Windows](../how-to/install-local-server-windows.md) |
| État PostgreSQL | `docker compose ... ps` | [Windows](../how-to/install-local-server-windows.md) |
| Journaux PostgreSQL | `docker compose ... logs postgres` | [Dépannage](../how-to/troubleshoot-local-setup.md) |
| Santé serveur | `Invoke-RestMethod http://localhost:8082/api/health` | [Windows](../how-to/install-local-server-windows.md) |
| Sauvegarde | `deploy/backup-postgres.ps1` | [Sauvegarde](../how-to/backup-and-test-restore-postgresql.md) |
| Restauration de contrôle | `deploy/test-restore-postgres.ps1` | [Sauvegarde](../how-to/backup-and-test-restore-postgresql.md) |
| Connexion Godot | Comparer les identifiants de compatibilité | [Godot](../how-to/connect-godot-template.md) |
| Verdict final | Parcourir les preuves | [Acceptation](local-setup-acceptance-checklist.md) |

## Lecture directe des contrats

- `VERSION` : version de l'archive serveur ;
- `RELEASE-MANIFEST.json` : inventaire et provenance de la release ;
- `SHA256SUMS.txt` : empreinte de chaque fichier embarqué ;
- `docs/docs-build-manifest.json` : version et empreintes de la documentation ;
- `examples/local-setup-catalog.json` : états publics courants ;
- contrat de compatibilité du template : version client et serveur acceptée.

## Preuves à séparer

- validation Markdown ;
- build HTML hors ligne ;
- archive extraite et vérifiée ;
- PostgreSQL réel ;
- serveur réel ;
- connexion Godot réelle ;
- publication du site ;
- déploiement externe.

Une couche verte ne rend pas automatiquement vertes les suivantes.
