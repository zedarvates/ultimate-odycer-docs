# Variante d'installation locale sous Linux

Cette page contient uniquement les différences Linux. Commencez par lire le
[guide Windows principal](install-local-server-windows.md), qui définit les
portes de disponibilité, de compatibilité et de persistance.

> **État actuel — `unavailable` :** aucune archive Linux publique n'est
> actuellement listée sur la
> [page officielle](https://www.ultimateodycer.com/releases/). Ne transformez
> pas l'archive Windows ni le code interne en release Linux improvisée.

## Prérequis

- distribution Linux encore maintenue ;
- Docker Engine et le plugin Compose ;
- espace disque correspondant au profil choisi ;
- archive Linux et SHA-256 réellement publiés pour la même version.

Vérifiez :

```bash
docker version
docker compose version
```

## Vérifier l'archive

```bash
sha256sum ultimate-odycer-server-<version>-linux-x86_64.zip
```

Comparez la sortie avec la page des releases avant extraction. Si l'archive
fournit `SHA256SUMS.txt`, exécutez également depuis sa racine :

```bash
sha256sum -c SHA256SUMS.txt
```

## Démarrer PostgreSQL

Définissez `ODYCER_DB_PASSWORD` dans le terminal sans l'inscrire dans
l'historique, puis lancez uniquement PostgreSQL :

```bash
read -s -p "Mot de passe PostgreSQL: " ODYCER_DB_PASSWORD
export ODYCER_DB_PASSWORD
docker compose -f deploy/docker-compose.yml up -d postgres
docker compose -f deploy/docker-compose.yml ps
```

Le service doit devenir sain et utiliser `odycer_pgdata`.

## Exécutables

Suivez le `deploy/QUICKSTART.md` de la release. Si l'archive exige le droit
d'exécution :

```bash
chmod u+x bin/login-server bin/mmorpg-server
```

Ne passez pas récursivement tous les fichiers en exécutables.

## Limites de cette variante

La disponibilité de Docker Engine ne prouve pas celle du serveur Linux. La
connexion Godot, la sauvegarde, la restauration de contrôle et la liste finale
restent obligatoires. macOS est hors périmètre ; une future application mobile
vise Android seulement.
