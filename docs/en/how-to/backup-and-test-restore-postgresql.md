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

```powershell
docker volume ls
docker compose -f .\deploy\docker-compose.yml ps
```

The expected volume is `odycer_pgdata`, and PostgreSQL must be healthy.

Do not use commands that delete volumes, including a Compose shutdown with the
volume-removal option or a global volume-pruning operation.

## 2. Create a backup on the host

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
