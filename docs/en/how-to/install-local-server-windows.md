# Install the local server on Windows

This is the primary installation path. It prepares Docker, PostgreSQL, and the
server archive without automatically exposing the machine to the Internet.

> **Availability gate:** the
> [releases page](https://www.ultimateodycer.com/releases/) currently says that
> no public release can be downloaded. Until this changes, perform only the
> machine checks and stop before downloading.

## Before starting: open the right PowerShell

Use a currently supported stable release of **PowerShell 7**, not
"Windows PowerShell" 5.1. The `Read-Host -MaskInput` option used below was
introduced in PowerShell 7.1. Installing PowerShell 7 does not replace 5.1;
they can coexist. If needed, follow the
[official Microsoft installation guide](https://learn.microsoft.com/powershell/scripting/install/install-powershell-on-windows).

Open PowerShell 7 from the Start menu or select that profile in Windows
Terminal. The name "Terminal" does not identify the interpreter running
inside it. These checks request no password and change nothing:

```powershell
$PSVersionTable.PSVersion
(Get-Command Read-Host).Parameters.ContainsKey('MaskInput')
Get-Command Get-FileHash
```

Expected result: version 7.1 or later, `True`, then the `Get-FileHash` command.
If the version is 5.1 or a command is missing, stop and open the right terminal
before proceeding. Do not remove `-MaskInput` to bypass the error or paste a
password into the command. The
[Microsoft Read-Host reference](https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/read-host)
explains that masking protects the display, not the value stored in memory.

After extracting the release, open this terminal in the folder containing
`VERSION`. Check your location with `Get-Location` and `Test-Path .\VERSION`
(expected: `True`). Paths starting with `.\` are relative to this folder.
Read-only checks do not require an administrator terminal; an installation
may request separate elevation, which the user must approve.

## 1. Choose the machine profile

| `estimated` profile | CPU | RAM | Free SSD | Headroom to retain |
|---|---:|---:|---:|---|
| Dedicated server | 4 cores | 8 GiB | 20 GiB | operating system and backups |
| Shared workstation | 6 cores | 16 GiB | 40 GiB | work, browser, or game |
| Creation workstation | 8 cores | 32 GiB | 100 GiB | Godot and optional modules |

These figures plan a first local trial. A future release sheet must replace an
estimate with an `observed` measurement before calling it a certified minimum.

## 2. Check Windows, WSL, and Docker

Docker Desktop with the WSL 2 backend is the beginner path. Check its terms for
your organization. The
[Docker Windows documentation](https://docs.docker.com/desktop/setup/install/windows-install/)
lists supported Windows versions and licensing conditions.

In PowerShell:

```powershell
wsl --version
docker version
docker compose version
```

Expected result: all three commands succeed without starting a container.
`docker version` must show both **Client and Server** sections without a
connection error. A client version alone does not prove the Docker engine
works. If WSL or Docker is missing, follow the official documentation and
repeat this step. For engine errors, use the
[troubleshooting guide](troubleshoot-local-setup.md) before starting anything.

On a shared workstation, set sensible processor and memory limits in Docker
Desktop so Windows remains usable. Do not present that limit as the server's
maximum capacity.

## 3. Download only a real release

Copy the filename and SHA-256 from the official page. Download the archive into
a new working directory.

Verify it before opening:

```powershell
Get-FileHash -Algorithm SHA256 .\ultimate-odycer-server-<version>-windows-x86_64.zip
```

Replace `<version>` with the displayed value. Compare all 64 characters. If the
digests differ, delete the defective download and stop.

## 4. Extract without mixing versions

Extract each version into its own directory. From the extracted root, require:

```text
VERSION
SHA256SUMS.txt
RELEASE-MANIFEST.json
deploy/QUICKSTART.md
deploy/docker-compose.yml
docs/index.html
```

An archive missing these files does not satisfy the contract described here.
Then verify the
[offline documentation and server archive contract](../reference/offline-documentation-and-server-archive.md).

## 5. Start PostgreSQL

Keep the same PowerShell 7 terminal for operations that use the password
environment variable. It belongs to this session and its child processes;
it is neither a password backup nor an encrypted secret. Do not display it
or send an environment-variable inventory to an LLM.

Enter the password without displaying it in the command:

```powershell
$env:ODYCER_DB_PASSWORD = Read-Host "PostgreSQL password" -MaskInput
docker compose -f .\deploy\docker-compose.yml up -d postgres
docker compose -f .\deploy\docker-compose.yml ps
```

Expected result: `postgres` becomes healthy and uses the named volume
`odycer_pgdata` (the actual name may have a Compose project prefix).
Docker is not a backup; a destructive command or disk failure
can still remove the volume.

## 6. Create the local configuration

```powershell
Copy-Item .\deploy\config.example.json .\config.json
```

Open `config.json` and replace every `CHANGE_ME` value. Keep the game, login,
and WebAdmin addresses on local loopback. Never publish the JWT secret or
PostgreSQL password, including in a prompt sent to an LLM.

## 7. Start the services

Follow the `deploy/QUICKSTART.md` shipped with your version. Under the currently
planned contract, Windows executables start from the archive root:

```powershell
.\bin\login-server.exe
.\bin\mmorpg-server.exe
```

Use two terminals if both processes remain in the foreground. Do not open a
router or firewall port for this local tutorial.

## 8. Check health and PostgreSQL

```powershell
Invoke-RestMethod http://localhost:8082/api/health
```

The result must report a healthy service. Inspect the release logs and require
confirmation of the PostgreSQL connection. SQLite fallback is a temporary
safety net and blocks successful completion of this tutorial.

## 9. Back up before continuing

Continue immediately with
[back up and test PostgreSQL restoration](backup-and-test-restore-postgresql.md).
Local setup is incomplete until that gate passes.

## Optional modules

Choose server only or server with compatible Tools Suite modules. Install only
modules listed for the same version. The Tools Suite is currently
`under_construction`; its absence does not block the server-only path.
