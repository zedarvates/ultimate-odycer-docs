# Troubleshoot local setup

Start from the observed symptom. Change one variable at a time and retain the
command, result, and time of each check.

## Quick questions and answers

### Where do I download the server?

Only from the [official releases page](https://www.ultimateodycer.com/releases/).
If it says that no public release exists, nothing on your machine needs fixing:
the step is `unavailable`.

### The SHA-256 does not match. Can I try anyway?

No. Do not run the archive. Delete that download, download it again from the
official page, and compare all 64 characters.

### WSL or Docker does not respond.

Run separately:

```powershell
wsl --version
docker version
docker compose version
```

The first failing command identifies the prerequisite to repair. Do not change
PostgreSQL until all three checks pass.

### PostgreSQL does not become healthy.

```powershell
docker compose -f .\deploy\docker-compose.yml ps
docker compose -f .\deploy\docker-compose.yml logs postgres
```

Check that `ODYCER_DB_PASSWORD` is present, disk space is available, and the
local port is not already used. Do not copy the password into a support request.

### The server runs but reports SQLite fallback.

This is a partial result. Check that `config.json` uses the database port and
name from Compose shipped with the same release. Restart the server only after
PostgreSQL is healthy. Do not delete fallback SQLite data before a validated
inspection or catch-up procedure.

### A port is already in use.

Identify the owning process with Windows or Linux tools. Do not stop it when it
belongs to another project. Use only release-documented port settings and
update server, client, and health checks together.

### The server is healthy but Godot cannot connect.

Check in order:

1. exact template/server compatibility;
2. active login service;
3. login `localhost` address and port;
4. handoff from login to game server;
5. Godot, login, and game logs for the same time.

A visible menu does not prove connection.

### The PostgreSQL volume disappeared.

Stop writes. Do not immediately create another volume with the same name.
Inventory existing volumes and locate the latest backup outside Docker with its
SHA-256. Recover from verified evidence, not an assumption.

### Backup or restore check fails.

Keep the dump and digest. Check free space, PostgreSQL tool version, container
health, and the complete error. The check must target only the verification
database; do not use the active database as a diagnostic target.

### The shared workstation becomes too slow.

Stop the client or an optional module cleanly, then observe CPU, memory, and
disk. Reduce Docker resources or disable unnecessary creation tools. Do not
infer a server limit from a workstation saturated by Godot or ComfyUI.

### A Tools Suite module is absent.

Check its status and your release compatibility matrix. An
`under_construction`, `planned`, or absent module cannot be installed. Use the
server-only path.

## Safe information to share with an LLM

- Windows, WSL, Docker, and Compose versions;
- release version;
- service names and healthy/unhealthy status;
- command and error message;
- time and secret-free log excerpt;
- expected result.

Never share a password, JWT secret, private key, database dump, or player data.

See also the [LLM prompts](../reference/llm-local-setup-prompts.md).
