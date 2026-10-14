param(
    [Parameter(Mandatory=$true)][string]$PostgresBin,
    [int]$Port = 15432,
    [string]$Database = 'postgres',
    [string]$Username = 'admin_local',
    [switch]$UseEnvironmentCredentials
)
$ErrorActionPreference = 'Stop'
if ($Username -cnotmatch '^[A-Za-z][A-Za-z0-9_]{2,31}$') { throw 'Nom : 3 a 32 lettres, chiffres ou tirets bas.' }
$psql = Join-Path (Resolve-Path -LiteralPath $PostgresBin).Path 'psql.exe'
if (-not (Test-Path -LiteralPath $psql)) { throw 'psql.exe absent.' }
function Read-PrivateText([string]$Prompt) {
    $secret = Read-Host $Prompt -AsSecureString
    $pointer = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secret)
    try { return [Runtime.InteropServices.Marshal]::PtrToStringBSTR($pointer) }
    finally { [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($pointer); $secret.Dispose() }
}
if ($UseEnvironmentCredentials) {
    $databasePassword = $env:PGPASSWORD
    $password = $env:ODYCER_ADMIN_PASSWORD
    if (-not $databasePassword -or -not $password) { throw 'PGPASSWORD et ODYCER_ADMIN_PASSWORD requis pour ce mode explicite.' }
} else {
    $databasePassword = Read-PrivateText 'Mot de passe PostgreSQL (postgres)'
    $password = Read-PrivateText 'Nouveau mot de passe WebAdmin (12 caracteres minimum)'
}
if ($password.Length -lt 12 -or [Text.Encoding]::UTF8.GetByteCount($password) -gt 72 -or $password.Contains([string][char]0)) {
    throw 'Le mot de passe doit avoir au moins 12 caracteres et au plus 72 octets UTF-8.'
}
$sqlPassword = $password.Replace("'", "''")
$info = New-Object Diagnostics.ProcessStartInfo
$info.FileName = $psql
# Database is a single libpq environment value, never interpolated into arguments.
$info.Arguments = "-X -h 127.0.0.1 -p $Port -U postgres -v ON_ERROR_STOP=1 -At"
$info.UseShellExecute = $false
$info.CreateNoWindow = $true
$info.RedirectStandardInput = $true
$info.RedirectStandardOutput = $true
$info.RedirectStandardError = $true
$info.EnvironmentVariables['PGDATABASE'] = $Database
$info.EnvironmentVariables['PGPASSWORD'] = $databasePassword
$info.EnvironmentVariables['PGCLIENTENCODING'] = 'UTF8'
$process = [Diagnostics.Process]::Start($info)
$output = $process.StandardOutput.ReadToEndAsync()
$errors = $process.StandardError.ReadToEndAsync()
try {
    $process.StandardInput.WriteLine("BEGIN; SET standard_conforming_strings=on; CREATE EXTENSION IF NOT EXISTS pgcrypto;")
    $process.StandardInput.WriteLine("INSERT INTO players(username,email,password_hash,role,status) VALUES ('$Username','$Username@example.invalid',crypt('$sqlPassword',gen_salt('bf',12)),'admin','active'); COMMIT;")
    $process.StandardInput.Close()
    if (-not $process.WaitForExit(30000)) { $process.Kill(); throw 'Delai de creation depasse.' }
    if ($process.ExitCode -ne 0) { throw 'Creation refusee. Verifier la base, ses migrations et un nom de compte encore inutilise.' }
    Write-Host "Compte WebAdmin cree : $Username" -ForegroundColor Green
    Write-Host 'Aucun compte existant modifie. Le mot de passe ne figure ni dans la commande ni dans un fichier.'
} finally {
    $password = $sqlPassword = $databasePassword = $null
    if (-not $process.HasExited) { $process.Kill(); $process.WaitForExit() }
    $process.Dispose()
}
