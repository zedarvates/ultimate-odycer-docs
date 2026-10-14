# Démarrer Ultimate Odycer sur Windows

> **Statut `observed`, qualification privée.** La version publique du serveur
> reste `unavailable`. Sans archive privée correspondante remise par le projet,
> consulte les captures et prépare les prérequis, puis arrête-toi avant de lancer
> le serveur. Cette publication concerne le guide, pas les exécutables.

[Guide HTML illustré](../../assets/windows-startup-20261014/TUTORIEL-WINDOWS.html) ·
[Pack hors ligne et scripts](../../assets/windows-startup-20261014/tutoriel-odycer-windows.zip) ·
[English](../../en/tutorials/start-local-server-windows-illustrated.md)


**Un premier serveur local, de l’archive à WebAdmin.** Guide en français du
14 octobre 2026, illustré par des captures réelles de Windows Server 2022.

À l’arrivée : PostgreSQL répond, le propriétaire natif pilote le jeu, le login
et WebAdmin, et tu peux te connecter à la console d’administration. Prévois un
dossier neuf, deux fenêtres PowerShell et un navigateur.

Pour chaque fenêtre, fais **Windows + R**, puis saisis :

```text
powershell.exe -NoProfile -ExecutionPolicy Bypass
```

Cette option permet les scripts du guide dans cette fenêtre uniquement ; elle
ne change pas la politique PowerShell de la machine.

Ce guide accompagne l’archive privée de qualification `unavailable` du projet.
Il couvre un démarrage sur ta machine, avec toutes les adresses sur
`localhost`. La mise en ligne et Windows 11 constituent des étapes séparées.

## Avant de commencer

Rassemble l’archive serveur, les quatre scripts PowerShell joints au guide et
PostgreSQL **16.15 Windows x64**. Le banc utilise le ZIP de binaires EDB, pas
l’assistant d’installation. La page [Binaires PostgreSQL d’EDB](https://www.enterprisedb.com/download-postgresql-binaries)
permet de retrouver ce format ; EDB le destine aux utilisateurs expérimentés.

PostgreSQL a aussi besoin du runtime Microsoft Visual C++ x64. Le banc fournit
les DLL redistribuables MSVC **14.44.35112** à côté des binaires PostgreSQL.
Le ZIP PostgreSQL seul ne les contient pas. Si ces fichiers ne te sont pas
fournis, utilise la [page officielle Microsoft Visual C++](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170)
pour obtenir le package x64 ; son assistant n’est pas illustré dans ce guide.
Ne récupère pas de DLL isolées depuis un site tiers.

Les DLL du dossier `bin` d’Odycer sont déjà incluses dans son archive. Elles ne
remplacent pas les prérequis du **serveur PostgreSQL externe**. Python, Zig,
Node et Visual Studio ne sont pas nécessaires pour exécuter le serveur.
Redis est optionnel pour ce parcours ; son absence peut produire un avertissement
dans les logs.

## 1 — Préparer les dossiers

Crée `C:\Odycer`, puis place les scripts du guide dans `C:\Odycer\tuto`.
Décompresse le serveur dans `C:\Odycer\serveur` : ce dossier doit contenir
directement `bin`, `config`, `data`, `deploy`, `templates` et `webadmin`.
Décompresse le ZIP PostgreSQL dans `C:\Odycer\postgres`, en conservant son
sous-dossier `pgsql`.

Dans PowerShell, définis ces variables. Garde cette première fenêtre ouverte :

```powershell
$server = 'C:\Odycer\serveur'
$pgBin = 'C:\Odycer\postgres\pgsql\bin'
$pgData = 'C:\Odycer\pgdata'
$tuto = 'C:\Odycer\tuto'
Get-ChildItem "$server\bin" -Filter *.exe | Select-Object Name, Length
& "$pgBin\postgres.exe" --version
```

Tu dois trouver `mmorpg-server.exe`, `login-server.exe`, `webadmin-server.exe`
et `odycer-services.exe`. PostgreSQL doit annoncer `16.15`.

![Les quatre exécutables réels dans Windows](../../assets/windows-startup-20261014/captures/01-dossier.png)

*Le banc utilise des dossiers temporaires sous `C:\OdycerQA`. Tes chemins sont
ceux définis ci-dessus ; ne recopie pas les chemins temporaires des images.*

Si tu utilises le CRT app-local fourni avec sa notice, copie ses DLL dans le
dossier `pgsql\bin` avant de poursuivre. Le banc y place notamment
`msvcp140.dll`, `vcruntime140.dll` et les DLL associées de la même distribution.

Vérifie aussi l’archive serveur avec le SHA256 transmis avec ton kit privé :

```powershell
Get-FileHash 'C:\Odycer\ultimate-odycer-server-unavailable-windows-x86_64.zip' -Algorithm SHA256
```

Empreinte de la candidate photographiée :
`262ac6e29408f8df48ba31c86b36c846fe7bb26799c140eff504169e12b891d9`.
Sa signature est une signature privée de qualification ; elle n’est pas une
signature Windows publique reconnue.

## 2 — Créer et démarrer PostgreSQL

À faire **une seule fois dans un dossier `pgdata` neuf**. `-W` te demande de
choisir un mot de passe PostgreSQL sans l’écrire dans la commande :

```powershell
& "$pgBin\initdb.exe" -D $pgData -U postgres --auth=scram-sha-256 --no-locale --encoding=UTF8 -W
if ($LASTEXITCODE -ne 0) { throw 'Initialisation PostgreSQL refusee' }
& "$pgBin\pg_ctl.exe" -D $pgData -l 'C:\Odycer\postgres.log' -o '-h localhost -p 15432' -w -t 30 start
if ($LASTEXITCODE -ne 0) { throw 'PostgreSQL ne demarre pas' }
```

Vérifie la version et les écritures durables ; `psql` peut redemander le mot
de passe PostgreSQL :

```powershell
& "$pgBin\psql.exe" -X -h localhost -p 15432 -U postgres -d postgres -c 'SELECT version(); SHOW fsync; SHOW synchronous_commit;'
```

Résultat attendu : PostgreSQL 16.15, `fsync = on`, `synchronous_commit = on`.

![PostgreSQL natif et les deux réglages de durabilité](../../assets/windows-startup-20261014/captures/02-postgresql.png)

## 3 — Configurer Odycer et TLS

Les scripts suivants refusent d’écraser un certificat ou une configuration
existante. Le premier crée une identité TLS **locale de sept jours**, pour le
nom `localhost`, sans modifier les magasins de certificats Windows.

```powershell
& "$tuto\New-LocalTlsCertificate.ps1" -OutputDirectory "$server\certs"
& "$tuto\Configure-LocalServer.ps1" -ServerDirectory $server
```

Entre le **même mot de passe PostgreSQL** qu’à l’étape 2. Le script génère le
secret JWT et garde l’authentification WebAdmin active. `config.json` est créé
à la racine du serveur : conserve ce fichier et `certs\server.key` privés.

| Usage | Ports de ce guide |
|---|---:|
| PostgreSQL | 15432 |
| Jeu, TLS | 7777 |
| Login, TLS | 2106 |
| WebAdmin intégré au jeu | 8082 |
| WebAdmin autonome du propriétaire natif | 8084 |

Les captures du banc emploient des ports libres attribués automatiquement et
montrent l’adresse IPv4 de boucle locale ; ce texte utilise son alias `localhost`.
Les commandes du guide utilisent les valeurs du tableau. Garde le WebAdmin
intégré et le WebAdmin autonome sur **deux ports différents**.

![Configuration réellement utilisée, sans afficher les secrets](../../assets/windows-startup-20261014/captures/03-configuration.png)

Le certificat local protège les connexions jeu/login en vérifiant `localhost`.
Il ne transforme pas le WebAdmin HTTP local en site HTTPS public.

## 4 — Lancer les trois services

Dans la première fenêtre PowerShell :

```powershell
& "$tuto\Start-LocalServer.ps1" -ServerDirectory $server -AdminPort 8084
```

Garde cette fenêtre ouverte. Le script lance `odycer-services.exe`, qui devient
le propriétaire des trois services. N’en lance pas une deuxième copie à la main.
Laisse quelques secondes au premier démarrage pour créer le schéma et charger
les données.

Dans une **deuxième fenêtre PowerShell**, vérifie les deux réponses HTTP :

```powershell
(Invoke-WebRequest -UseBasicParsing 'http://localhost:8084/health').StatusCode
(Invoke-WebRequest -UseBasicParsing 'http://localhost:8082/health').StatusCode
```

Les deux valeurs doivent être `200`. En cas d’échec, lis les fichiers dans
`C:\Odycer\serveur\logs` et `C:\Odycer\postgres.log` avant de relancer.

![Les trois processus et les deux contrôles de santé](../../assets/windows-startup-20261014/captures/04-services.png)

`conhost.exe`, également visible dans la capture, correspond à l’hôte de
console Windows.

## 5 — Préparer le premier compte administrateur

Une page de connexion n’invente pas de compte administrateur. Pour cette
**nouvelle base locale**, utilise le script joint depuis la deuxième fenêtre :

```powershell
& 'C:\Odycer\tuto\New-LocalAdmin.ps1' -PostgresBin 'C:\Odycer\postgres\pgsql\bin' -Port 15432 -Username admin_local
```

Il demande d’abord le mot de passe PostgreSQL, puis le nouveau mot de passe
WebAdmin : au moins 12 caractères, au maximum 72 octets UTF-8. Le compte est
créé après les migrations, avec un hash bcrypt et le rôle `admin` ; un nom
déjà utilisé est refusé. Les mots de passe ne passent pas dans les arguments
des processus et ne sont pas conservés dans un fichier temporaire.

Le compte `admin_tutoriel` visible sur les captures appartient uniquement au
banc. Utilise **ton** compte `admin_local` et **ton** mot de passe.

## 6 — Ouvrir WebAdmin

Dans le navigateur de cette même machine, ouvre
[WebAdmin local](http://localhost:8084). Renseigne le compte et le mot de passe
créés à l’étape 5, puis clique sur le bouton de connexion.

![La page réelle de connexion à WebAdmin](../../assets/windows-startup-20261014/captures/05-webadmin-connexion.png)

Une fois connecté, vérifie l’état des services. Le propriétaire doit être
disponible et le jeu, le login et WebAdmin doivent apparaître comme démarrés.
Les actions administrateur demandent une confirmation.

![WebAdmin connecté et état des services réels](../../assets/windows-startup-20261014/captures/06-webadmin-services.png)

Le navigateur peut afficher sa propre invitation à enregistrer le mot de passe,
comme dans cette capture ; les trois lignes de services restent visibles dessous.

Si tu vois `401`, reconnecte-toi. Un `403` indique que le compte n’a pas les
droits administrateur attendus. Une capacité ou une liste de joueurs vide
ne prouve pas qu’un client de jeu est déjà connecté.

## 7 — Vérifier que les données restent présentes

Le banc photographié a aussi créé un compte joueur, un personnage et rejoint
Trammel via le protocole TLS. Il a ensuite arrêté et relancé les trois services,
puis retrouvé le personnage et ses 120 pièces. Tu peux lire les personnages de
ta propre base avec :

```powershell
& 'C:\Odycer\postgres\pgsql\bin\psql.exe' -X -h localhost -p 15432 -U postgres -d postgres -c 'SELECT id,name,gold FROM characters;'
```

Une table vide est normale tant que tu n’as pas créé de personnage avec un
client compatible. Le tutoriel s’arrête à la mise en route du serveur ; la
configuration d’un client Godot, Three.js ou VR demande son propre guide.

![Le personnage du banc relu après redémarrage](../../assets/windows-startup-20261014/captures/07-persistance.png)

## 8 — Arrêter et reprendre plus tard

Reviens dans la première fenêtre du lanceur et saisis :

```text
shutdown
```

Attends le message **code 0**. Le lanceur laisse les services terminer leurs
sauvegardes. Si la fermeture reste bloquée, il le signale et conserve les
processus ; lis les logs de persistance avant toute autre action.

Une fois le propriétaire arrêté, arrête PostgreSQL :

```powershell
& 'C:\Odycer\postgres\pgsql\bin\pg_ctl.exe' -D 'C:\Odycer\pgdata' -m fast -w -t 30 stop
```

![Fin du scénario : propriétaire et base arrêtés proprement](../../assets/windows-startup-20261014/captures/08-arret.png)

Pour la prochaine session, relance seulement `pg_ctl ... start`, puis
`Start-LocalServer.ps1`. **Ne refais pas `initdb`** et conserve `pgdata`,
`config.json`, les dossiers `data` et `logs`, et tes certificats. Après sept
jours, renouvelle le certificat de démonstration dans un dossier neuf et
adapte sa référence dans la configuration.

## Si une étape bloque

| Symptôme | Premier contrôle |
|---|---|
| `initdb` ne s’ouvre pas, DLL absente ou code `0xC0000135` | Runtime Microsoft Visual C++ x64 de PostgreSQL ; ne pas déplacer les DLL Odycer. |
| Connexion PostgreSQL refusée | Même port et même mot de passe dans PostgreSQL et `config.json` ; lire `postgres.log`. |
| Port déjà occupé | Choisir un autre port dans la configuration et dans les commandes associées. |
| `/health` ne répond pas | Vérifier le démarrage du propriétaire et les logs ; garder PostgreSQL actif. |
| TLS refuse le serveur | Utiliser le nom `localhost`, vérifier les dates et fournir `server.crt` au client ; garder la vérification TLS active. |
| Compte administrateur refusé | Vérifier le nom créé, le mot de passe et la base visée à l’étape 5. |

## Ce qui a été vérifié

Les images proviennent de deux séances du même profil de VM isolée du projet ;
leurs pixels ne sont pas retouchés. Elles montrent les sorties de vrais processus et le navigateur
WebAdmin. Le certificat est créé dans l’invité, PostgreSQL utilise SCRAM et
les données sont durables. Les scripts de certificat et de premier compte
administrateur sont exécutés dans ce scénario ; la syntaxe des deux scripts
de configuration/lancement fournis au lecteur est contrôlée séparément.
La dernière séance contrôle aussi l’arrêt propre des services et de la VM.

Le pilote QA automatise certaines étapes pour les photographier. Les chemins
temporaires et ports de la VM diffèrent donc du profil fixe donné au lecteur.
Le guide ne revendique ni installeur Windows/SCM, ni Windows 11, ni certificat
public, ni déploiement Internet. Le retrait automatique des secrets effectué
par le banc en fin de test ne doit pas être reproduit sur ton installation.
