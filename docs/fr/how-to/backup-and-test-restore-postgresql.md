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

Sous Windows, utilisez le terminal PowerShell 7 et le dossier de la release
vérifiés dans le [guide d'installation](install-local-server-windows.md).
`pwsh` doit être disponible pour les scripts ci-dessous. Si vous avez ouvert
un nouveau terminal, les variables de mot de passe de la session précédente
n'y sont pas automatiquement présentes : reprenez la saisie masquée prévue
par la release, sans afficher le secret ni le demander au LM.

```powershell
docker volume ls
docker compose -f .\deploy\docker-compose.yml ps
```

La clé logique du volume est `odycer_pgdata` et PostgreSQL doit être sain.
Le nom affiché par Docker peut être préfixé par le nom du projet Compose,
par exemple `<projet>_odycer_pgdata`. Ne créez pas un second volume pour faire
correspondre son nom au tutoriel. Vérifiez le montage du service et les labels
`com.docker.compose.project` et `com.docker.compose.volume` du volume réel.
Voir la [référence Docker sur les volumes Compose](https://docs.docker.com/reference/compose-file/volumes/).

N'exécutez pas les commandes qui suppriment les volumes, notamment une descente
Compose avec l'option de suppression des volumes ou un nettoyage global des
volumes.

## 2. Créer une sauvegarde sur l'hôte

Si les scripts vérifiés de votre release proposent `-WhatIf`, commencez par :

```powershell
pwsh -File .\deploy\backup-postgres.ps1 -WhatIf
pwsh -File .\deploy\test-restore-postgres.ps1 -WhatIf
```

Vérifiez le dossier de sortie et le nom de la base de contrôle annoncés.
Cette simulation ne crée aucun dump, ne restaure rien et ne prouve pas que
PostgreSQL fonctionne. Ne supposez pas que tout script tiers respecte ce mode.

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

Avant la commande de restauration, vérifiez dans le script dont l'empreinte
a été contrôlée quels noms de base il crée et supprime. Le contrat actuel utilise
`ultimate_odycer_restore_check`, un nom fixe : une base existante de ce nom
peut être supprimée au début du test. Ne lancez pas deux tests en parallèle.

Pour ce contrat, ce contrôle lit uniquement la présence de cette base :

```powershell
docker compose -f .\deploy\docker-compose.yml exec -T postgres psql -v ON_ERROR_STOP=1 -U odycer -d postgres -Atc "SELECT datname FROM pg_database WHERE datname = 'ultimate_odycer_restore_check';"
```

Continuez uniquement si la commande réussit sans afficher de nom de base.
Si elle affiche `ultimate_odycer_restore_check`, échoue ou si la cible reste
incertaine, arrêtez-vous. Faites identifier et préserver la base existante ;
ne la supprimez pas automatiquement pour débloquer le tutoriel. L'absence de
résultat après une erreur ne constitue pas une réussite.

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
