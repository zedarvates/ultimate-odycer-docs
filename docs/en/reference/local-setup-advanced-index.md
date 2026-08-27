# Advanced local setup index

This index provides shortcuts. Each command links to the page explaining its
prerequisites and interpretation.

| Goal | Shortcut | Source |
|---|---|---|
| Choose engine and world | Read the matrix | [Matrix](engine-template-world-matrix.md) |
| Check WSL and Docker | `wsl --version`, `docker version`, `docker compose version` | [Windows](../how-to/install-local-server-windows.md) |
| Verify archive | `Get-FileHash -Algorithm SHA256` | [Windows](../how-to/install-local-server-windows.md) |
| PostgreSQL state | `docker compose ... ps` | [Windows](../how-to/install-local-server-windows.md) |
| PostgreSQL logs | `docker compose ... logs postgres` | [Troubleshooting](../how-to/troubleshoot-local-setup.md) |
| Server health | `Invoke-RestMethod http://localhost:8082/api/health` | [Windows](../how-to/install-local-server-windows.md) |
| Backup | `deploy/backup-postgres.ps1` | [Backup](../how-to/backup-and-test-restore-postgresql.md) |
| Restore check | `deploy/test-restore-postgres.ps1` | [Backup](../how-to/backup-and-test-restore-postgresql.md) |
| Godot connection | Compare compatibility identifiers | [Godot](../how-to/connect-godot-template.md) |
| Final verdict | Review evidence | [Acceptance](local-setup-acceptance-checklist.md) |

## Read contracts directly

- `VERSION`: server archive version;
- `RELEASE-MANIFEST.json`: release inventory and provenance;
- `SHA256SUMS.txt`: digest for every bundled file;
- `docs/docs-build-manifest.json`: documentation version and digests;
- `examples/local-setup-catalog.json`: current public states;
- template compatibility contract: accepted client and server versions.

## Keep proof layers separate

- Markdown validation;
- offline HTML build;
- verified extracted archive;
- real PostgreSQL;
- real server;
- real Godot connection;
- site publication;
- external deployment.

A green layer does not automatically make later layers green.
