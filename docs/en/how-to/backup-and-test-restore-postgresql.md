# Back up and test PostgreSQL restoration

A Docker volume retains data after an ordinary restart. It does not replace a
backup stored outside the volume.

## What the release must provide

The planned contract adds:

```text
deploy/backup-postgres.ps1
deploy/test-restore-postgres.ps1
```

Until a release actually includes these scripts and their digests, their status
is `unavailable` for that release. Do not download a copy from another source.

## 1. Check the volume

On Windows, use the PowerShell 7 terminal and release folder verified in the
[installation guide](install-local-server-windows.md). `pwsh` must be available
for the scripts below. A newly opened terminal does not automatically inherit
password variables from a previous session: repeat the release's masked-input
procedure without displaying the secret or asking the LLM for it.

```powershell
docker volume ls
docker compose -f .\deploy\docker-compose.yml ps
```

The logical volume key is `odycer_pgdata`, and PostgreSQL must be healthy.
Docker may prefix the displayed name with the Compose project name, such as
`<project>_odycer_pgdata`. Do not create a second volume just to match this
guide's name. Check the service mount and the actual volume's
`com.docker.compose.project` and `com.docker.compose.volume` labels.
See the [Docker Compose volume reference](https://docs.docker.com/reference/compose-file/volumes/).

Do not use commands that delete volumes, including a Compose shutdown with the
volume-removal option or a global volume-pruning operation.

## 2. Create a backup on the host

If your release's verified scripts support `-WhatIf`, start with:

```powershell
pwsh -File .\deploy\backup-postgres.ps1 -WhatIf
pwsh -File .\deploy\test-restore-postgres.ps1 -WhatIf
```

Check the reported output directory and verification database name. This
simulation creates no dump, restores nothing and does not prove PostgreSQL
works. Do not assume every third-party script respects this mode.

With a compatible release:

```powershell
pwsh -File .\deploy\backup-postgres.ps1
```

The script must:

- fail when the required password is absent;
- produce a custom-format PostgreSQL dump in `backups/`;
- write an adjacent SHA-256 file;
- never print the password;
- clean up its temporary container file.

Periodically copy important backups to another medium. A directory on the same
disk does not protect against failure of that disk.

## 3. Verify the digest

```powershell
Get-FileHash -Algorithm SHA256 .\backups\<file>.dump
```

The value must match the `.sha256` file created beside the dump.

## 4. Test without destroying the active database

Before restoring, inspect the checksum-verified script for the database names
it creates and drops. The current contract uses the fixed name
`ultimate_odycer_restore_check`: an existing database with that name can be
dropped at the start of the test. Never run two restore checks concurrently.

For this contract, the following check only reads whether that database exists:

```powershell
docker compose -f .\deploy\docker-compose.yml exec -T postgres psql -v ON_ERROR_STOP=1 -U odycer -d postgres -Atc "SELECT datname FROM pg_database WHERE datname = 'ultimate_odycer_restore_check';"
```

Continue only if the command succeeds without printing a database name. If it
prints `ultimate_odycer_restore_check`, fails, or leaves the target uncertain,
stop. Have the existing database identified and preserved; do not delete it
automatically to unblock the tutorial. Empty output after an error is not a
successful check.

```powershell
pwsh -File .\deploy\test-restore-postgres.ps1 -BackupFile .\backups\<file>.dump
```

The check must restore into a separate verification database, verify the schema
and at least one application table, then remove only the verification database.
It must never delete `ultimate_odycer`.

## 5. Retain the evidence

Record:

- UTC date;
- dump name and SHA-256;
- PostgreSQL version;
- server version;
- restore-check result.

Never include the password, JWT secret, or dump contents in this evidence.

## Expected result

The backup exists outside the volume, its digest matches, and the restore check
succeeds. Without all three proofs, local setup remains incomplete.
