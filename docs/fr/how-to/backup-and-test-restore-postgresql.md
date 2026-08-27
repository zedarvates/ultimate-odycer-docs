# Sauvegarder et tester la restauration PostgreSQL

Un volume Docker conserve les données après un redémarrage ordinaire. Il ne
remplace pas une sauvegarde stockée hors du volume.

## Ce que la release doit fournir

Le contrat prévu ajoute :

```text
deploy/backup-postgres.ps1
deploy/test-restore-postgres.ps1
```

Tant qu'une release ne contient pas réellement ces scripts et leurs empreintes,
leur statut est `unavailable` pour cette release. N'en téléchargez pas une copie
depuis une source différente.

## 1. Vérifier le volume

```powershell
docker volume ls
docker compose -f .\deploy\docker-compose.yml ps
```

Le volume attendu est `odycer_pgdata` et PostgreSQL doit être sain.

N'exécutez pas les commandes qui suppriment les volumes, notamment une descente
Compose avec l'option de suppression des volumes ou un nettoyage global des
volumes.

## 2. Créer une sauvegarde sur l'hôte

Avec une release compatible :

```powershell
pwsh -File .\deploy\backup-postgres.ps1
```

Le script doit :

- échouer si le mot de passe requis manque ;
- produire un dump PostgreSQL au format personnalisé dans `backups/` ;
- écrire un fichier SHA-256 adjacent ;
- ne jamais imprimer le mot de passe ;
- nettoyer son fichier temporaire dans le conteneur.

Copiez ensuite périodiquement les sauvegardes importantes sur un autre support.
Un dossier situé sur le même disque ne protège pas d'une panne de ce disque.

## 3. Vérifier l'empreinte

```powershell
Get-FileHash -Algorithm SHA256 .\backups\<fichier>.dump
```

La valeur doit correspondre au fichier `.sha256` créé avec le dump.

## 4. Tester sans détruire la base active

```powershell
pwsh -File .\deploy\test-restore-postgres.ps1 -BackupFile .\backups\<fichier>.dump
```

Le test doit restaurer dans une base séparée nommée pour le contrôle, vérifier
le schéma et au moins une table applicative, puis supprimer uniquement cette
base de contrôle. Il ne doit jamais supprimer `ultimate_odycer`.

## 5. Conserver la preuve

Notez :

- la date UTC ;
- le nom et le SHA-256 du dump ;
- la version PostgreSQL ;
- la version du serveur ;
- le résultat du test de restauration.

Ne placez jamais le mot de passe, le secret JWT ou le contenu du dump dans cette
preuve.

## Résultat attendu

La sauvegarde existe hors du volume, son empreinte correspond et la restauration
de contrôle réussit. Sans ces trois preuves, la mise en route locale reste
incomplète.
