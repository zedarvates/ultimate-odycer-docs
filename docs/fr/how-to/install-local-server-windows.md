# Installer le serveur local sous Windows

Ce guide est le chemin principal. Il prépare Docker, PostgreSQL et l'archive
serveur sans ouvrir automatiquement la machine sur Internet.

> **Porte de disponibilité :** la
> [page des releases](https://www.ultimateodycer.com/releases/) indique
> actuellement qu'aucune release publique n'est téléchargeable. Tant que cette
> situation ne change pas, effectuez seulement les contrôles de la machine puis
> arrêtez-vous avant le téléchargement.

## Avant de commencer : ouvrir le bon PowerShell

Utilisez une version stable encore prise en charge de **PowerShell 7**, pas
« Windows PowerShell » 5.1. L'option `Read-Host -MaskInput` utilisée plus bas
existe depuis PowerShell 7.1. Installer PowerShell 7 ne remplace pas 5.1 :
les deux peuvent coexister. Suivez au besoin la
[procédure officielle Microsoft](https://learn.microsoft.com/powershell/scripting/install/install-powershell-on-windows).

Ouvrez PowerShell 7 depuis le menu Démarrer, ou choisissez ce profil dans
Windows Terminal. Le nom « Terminal » ne garantit pas quel interpréteur est
ouvert. Ces vérifications ne demandent aucun mot de passe et ne changent rien :

```powershell
$PSVersionTable.PSVersion
(Get-Command Read-Host).Parameters.ContainsKey('MaskInput')
Get-Command Get-FileHash
```

Résultat attendu : une version 7.1 ou supérieure, `True`, puis la commande
`Get-FileHash`. Si la version est 5.1 ou si une commande manque, arrêtez-vous
et ouvrez le bon terminal avant de poursuivre. Ne supprimez pas `-MaskInput`
pour contourner l'erreur et ne collez jamais un mot de passe dans la commande.
La [référence Microsoft de Read-Host](https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/read-host)
précise que le masquage protège l'affichage, pas la valeur stockée en mémoire.

Après extraction de la release, ouvrez ce terminal dans le dossier contenant
`VERSION`. Vérifiez votre emplacement avec `Get-Location` et
`Test-Path .\VERSION` (résultat attendu : `True`). Les chemins commençant par
`.\` partent de ce dossier. Les contrôles de lecture ne nécessitent pas de
terminal administrateur ; une installation éventuelle peut demander une
élévation distincte, à valider par l'utilisateur.

## 1. Choisir le profil de la machine

| Profil `estimated` | CPU | RAM | SSD libre | Réserve à conserver |
|---|---:|---:|---:|---|
| Serveur dédié | 4 cœurs | 8 Gio | 20 Gio | système et sauvegardes |
| Poste partagé | 6 cœurs | 16 Gio | 40 Gio | travail, navigateur ou jeu |
| Poste de création | 8 cœurs | 32 Gio | 100 Gio | Godot et modules optionnels |

Ces valeurs servent à planifier un premier essai local. La fiche d'une future
release doit remplacer une estimation par une mesure `observed` avant de parler
de minimum certifié.

## 2. Vérifier Windows, WSL et Docker

Docker Desktop avec le backend WSL 2 constitue le chemin débutant. Vérifiez ses
conditions d'utilisation pour votre organisation. La
[documentation Docker pour Windows](https://docs.docker.com/desktop/setup/install/windows-install/)
décrit les versions de Windows prises en charge et les conditions de licence.

Dans PowerShell :

```powershell
wsl --version
docker version
docker compose version
```

Résultat attendu : les trois commandes réussissent sans démarrer de conteneur.
`docker version` doit afficher les parties **Client et Server**, sans erreur
de connexion. Une version du client seule ne prouve pas que le moteur Docker
fonctionne. Si WSL ou Docker manque, suivez la documentation officielle puis
reprenez cette étape. En cas d'erreur moteur, utilisez le
[guide de dépannage](troubleshoot-local-setup.md) avant tout lancement.

Sur un poste partagé, fixez une limite raisonnable de processeur et de mémoire
dans Docker Desktop afin que Windows reste utilisable. Ne présentez pas cette
limite comme la capacité maximale du serveur.

## 3. Télécharger uniquement une release réelle

Sur la page officielle, copiez le nom du fichier et son SHA-256. Téléchargez
l'archive dans un nouveau dossier de travail.

Vérifiez l'archive avant de l'ouvrir :

```powershell
Get-FileHash -Algorithm SHA256 .\ultimate-odycer-server-<version>-windows-x86_64.zip
```

Remplacez `<version>` par la valeur affichée sur la page. Comparez les 64
caractères, sans ignorer un seul écart. Si les empreintes diffèrent, supprimez
le téléchargement défectueux et arrêtez-vous.

## 4. Extraire sans mélanger les versions

Extrayez chaque version dans son propre dossier. Depuis la racine extraite,
vérifiez la présence de :

```text
VERSION
SHA256SUMS.txt
RELEASE-MANIFEST.json
deploy/QUICKSTART.md
deploy/docker-compose.yml
docs/index.html
```

Une archive sans ces fichiers ne correspond pas au contrat décrit ici.
Vérifiez ensuite le
[contrat de la documentation hors ligne et de l'archive serveur](../reference/offline-documentation-and-server-archive.md).

## 5. Démarrer PostgreSQL

Saisissez le mot de passe sans l'afficher dans la commande :

Gardez le même terminal PowerShell 7 pour les opérations qui utilisent cette
variable. Elle appartient à cette session et à ses processus enfants : elle
n'est ni une sauvegarde du mot de passe ni un secret chiffré. Ne l'affichez pas
et ne transmettez pas un inventaire des variables d'environnement à un LM.

```powershell
$env:ODYCER_DB_PASSWORD = Read-Host "Mot de passe PostgreSQL" -MaskInput
docker compose -f .\deploy\docker-compose.yml up -d postgres
docker compose -f .\deploy\docker-compose.yml ps
```

Résultat attendu : le service `postgres` devient sain et utilise le volume
de clé logique `odycer_pgdata` (le nom réel peut porter un préfixe Compose).
Docker n'est pas une sauvegarde ; le volume peut encore
être supprimé par une mauvaise commande ou une défaillance du disque.

## 6. Créer la configuration locale

```powershell
Copy-Item .\deploy\config.example.json .\config.json
```

Ouvrez `config.json` et remplacez toutes les valeurs marquées `CHANGE_ME`.
Gardez les adresses du serveur, du login et du WebAdmin sur la boucle locale.
Ne publiez jamais le secret JWT ou le mot de passe PostgreSQL, y compris dans
un prompt envoyé à un LM.

## 7. Lancer les services

Suivez d'abord le `deploy/QUICKSTART.md` livré avec votre version. Pour le
contrat actuellement prévu, les exécutables Windows sont lancés depuis la
racine de l'archive :

```powershell
.\bin\login-server.exe
.\bin\mmorpg-server.exe
```

Utilisez deux terminaux si les processus restent au premier plan. N'ouvrez pas
de port dans le routeur ou le pare-feu pour ce tutoriel local.

## 8. Vérifier la santé et PostgreSQL

```powershell
Invoke-RestMethod http://localhost:8082/api/health
```

Le résultat doit indiquer un service sain. Inspectez ensuite les journaux de la
release et vérifiez qu'ils confirment la connexion PostgreSQL. Un repli SQLite
est un filet de sécurité temporaire : il bloque la réussite de ce tutoriel.

## 9. Sauvegarder avant de continuer

Passez immédiatement au guide
[sauvegarder et tester la restauration PostgreSQL](backup-and-test-restore-postgresql.md).
La mise en route n'est pas terminée tant que cette porte n'est pas verte.

## Modules optionnels

Choisissez serveur seul ou serveur avec modules compatibles de la Tools Suite.
N'installez que les modules réellement listés pour la même version. La Tools
Suite est actuellement `under_construction` ; son absence n'empêche pas le
chemin serveur seul.
