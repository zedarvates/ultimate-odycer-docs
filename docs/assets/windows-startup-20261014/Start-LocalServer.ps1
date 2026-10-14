param([Parameter(Mandatory=$true)][string]$ServerDirectory,[int]$AdminPort=8084)
$ErrorActionPreference='Stop'
$root=(Resolve-Path -LiteralPath $ServerDirectory).Path
$config=Get-Content -LiteralPath (Join-Path $root 'config.json') -Raw -Encoding UTF8 | ConvertFrom-Json
if ($AdminPort -eq $config.server.webadmin_port) { throw 'Ports WebAdmin autonome et integre identiques.' }
$logRoot=Join-Path $root ('logs\tutorial-'+[DateTime]::Now.ToString('yyyyMMdd-HHmmss'))
[IO.Directory]::CreateDirectory($logRoot) | Out-Null
$info=New-Object Diagnostics.ProcessStartInfo
$info.FileName=Join-Path $root 'bin\odycer-services.exe'
$info.Arguments='--runtime-dir "'+$root+'" --admin-port '+$AdminPort
$info.WorkingDirectory=$root
$info.UseShellExecute=$false; $info.CreateNoWindow=$true
$info.RedirectStandardInput=$true; $info.RedirectStandardOutput=$true; $info.RedirectStandardError=$true
$values=@{
    PATH=(Join-Path $root 'bin'); DB_HOST=$config.server.db_host; DB_PORT=[string]$config.server.db_port;
    DB_NAME=$config.server.db_name; DB_USER=$config.server.db_user; DB_PASSWORD=$config.server.db_password;
    DB_SSL_MODE=$config.server.db_ssl_mode; JWT_SECRET=$config.server.jwt_secret;
    ENABLE_TLS='true'; TLS_CERT_PATH=$config.network.tls_cert_path; TLS_KEY_PATH=$config.network.tls_key_path;
    GAME_PORT=[string]$config.server.server_port; LOGIN_PORT=[string]$config.server.login_port;
    WEBADMIN_PORT=[string]$config.server.webadmin_port; LICENSE_KEY=$config.server.license_key;
    PRODUCTION='false'; APP_ENV='development'; REDIS_HOST='127.0.0.1'; REDIS_PORT='16379';
    LOGIN_WORKER_THREADS='4'; DB_MIN_CONNECTIONS='2'; DB_MAX_CONNECTIONS='8'
}
foreach($entry in $values.GetEnumerator()) { $info.EnvironmentVariables[$entry.Key]=[string]$entry.Value }
$owner=[Diagnostics.Process]::Start($info)
$output=$owner.StandardOutput.ReadToEndAsync(); $errors=$owner.StandardError.ReadToEndAsync()
Write-Host "Proprietaire natif lance, PID $($owner.Id). WebAdmin : http://127.0.0.1:$AdminPort" -ForegroundColor Cyan
Write-Host 'Attendre les controles de sante dans un second terminal. Garder cette fenetre ouverte.'
while (-not $owner.HasExited) {
    $command=Read-Host 'Pour arreter proprement, taper shutdown puis Entree'
    if ($command -cne 'shutdown') { continue }
    $owner.StandardInput.WriteLine('shutdown'); $owner.StandardInput.Flush()
    if (-not $owner.WaitForExit(120000)) {
        Write-Host 'Fermeture toujours en attente : lire les logs de persistance. Aucun kill effectue.' -ForegroundColor Yellow
    }
}
[IO.File]::WriteAllText((Join-Path $logRoot 'owner.stdout.log'),$output.Result)
[IO.File]::WriteAllText((Join-Path $logRoot 'owner.stderr.log'),$errors.Result)
$code=$owner.ExitCode; $owner.Dispose()
if ($code -ne 0) { throw "Le proprietaire a termine avec le code $code. Logs : $logRoot" }
Write-Host "Proprietaire arrete proprement, code 0. Logs : $logRoot" -ForegroundColor Green
