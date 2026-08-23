# Linux local-installation variant

This page contains only Linux differences. Start with the
[primary Windows guide](install-local-server-windows.md), which defines the
availability, compatibility, and persistence gates.

> **Current state — `unavailable`:** no public Linux archive is listed on the
> [official page](https://www.ultimateodycer.com/releases/). Do not turn the
> Windows archive or internal source into an improvised Linux release.

## Prerequisites

- a maintained Linux distribution;
- Docker Engine and the Compose plugin;
- enough disk space for the selected profile;
- a real Linux archive and SHA-256 published for the same version.

Check:

```bash
docker version
docker compose version
```

## Verify the archive

```bash
sha256sum ultimate-odycer-server-<version>-linux-x86_64.zip
```

Compare the result with the releases page before extraction. If the archive
contains `SHA256SUMS.txt`, also run from its root:

```bash
sha256sum -c SHA256SUMS.txt
```

## Start PostgreSQL

Set `ODYCER_DB_PASSWORD` without putting it in shell history, then start only
PostgreSQL:

```bash
read -s -p "PostgreSQL password: " ODYCER_DB_PASSWORD
export ODYCER_DB_PASSWORD
docker compose -f deploy/docker-compose.yml up -d postgres
docker compose -f deploy/docker-compose.yml ps
```

The service must become healthy and use `odycer_pgdata`.

## Executables

Follow the release's `deploy/QUICKSTART.md`. If execution permission is needed:

```bash
chmod u+x bin/login-server bin/mmorpg-server
```

Do not recursively make every file executable.

## Limits of this variant

Docker Engine availability does not prove Linux server availability. The Godot
connection, backup, restore check, and final checklist remain mandatory. macOS
is out of scope; a future mobile application targets Android only.
