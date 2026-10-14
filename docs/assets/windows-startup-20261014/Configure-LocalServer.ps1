param(
    [Parameter(Mandatory=$true)][string]$ServerDirectory,
    [int]$PostgresPort = 15432,
    [int]$GamePort = 7777,
    [int]$LoginPort = 2106,
    [int]$IntegratedAdminPort = 8082
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path -LiteralPath $ServerDirectory).Path
$target = Join-Path $root 'config.json'
if (Test-Path -LiteralPath $target) { throw 'config.json existe deja : le conserver et le modifier manuellement.' }
foreach ($name in @('server.crt','server.key')) {
    if (-not (Test-Path -LiteralPath (Join-Path $root "certs\$name"))) { throw "Certificat absent : certs\$name" }
}
$secret = Read-Host 'Mot de passe PostgreSQL choisi pendant initdb' -AsSecureString
$pointer = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secret)
try { $password = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($pointer) }
finally { [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($pointer); $secret.Dispose() }
$random = New-Object byte[] 48
$rng = [Security.Cryptography.RandomNumberGenerator]::Create()
try { $rng.GetBytes($random) } finally { $rng.Dispose() }
$config = Get-Content -LiteralPath (Join-Path $root 'deploy\config.example.json') -Raw -Encoding UTF8 | ConvertFrom-Json
$values = @{
    db_host='127.0.0.1'; db_port=$PostgresPort; db_name='postgres'; db_user='postgres'; db_password=$password;
    db_ssl_mode='disable'; jwt_secret=[Convert]::ToBase64String($random); license_key='FREE-ALPHA';
    server_ip='127.0.0.1'; game_advertise_host='127.0.0.1'; server_port=$GamePort;
    login_ip='127.0.0.1'; login_port=$LoginPort; webadmin_ip='127.0.0.1'; webadmin_port=$IntegratedAdminPort;
    auto_open_webadmin_browser=$false; redis_host='127.0.0.1'; redis_port=16379
}
foreach ($entry in $values.GetEnumerator()) { $config.server | Add-Member -NotePropertyName $entry.Key -NotePropertyValue $entry.Value -Force }
$config.network.enable_tls=$true
$config.network.tls_cert_path=Join-Path $root 'certs\server.crt'
$config.network.tls_key_path=Join-Path $root 'certs\server.key'
$config.security.dev_admin_bypass=$false
[IO.File]::WriteAllText($target, ($config | ConvertTo-Json -Depth 20), (New-Object Text.UTF8Encoding($false)))
$password=$null
Write-Host "Configuration locale creee : $target" -ForegroundColor Green
Write-Host 'Mot de passe et JWT ecrits dans config.json, non affiches. Conserver ce fichier prive.'
