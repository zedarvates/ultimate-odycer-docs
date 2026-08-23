# Dépanner la mise en route locale

Commencez par le symptôme observé. Ne changez qu'une variable à la fois et
conservez la commande, le résultat et l'heure de chaque contrôle.

## Questions-réponses rapides

### Où télécharger le serveur ?

Uniquement sur la [page officielle des releases](https://www.ultimateodycer.com/releases/).
Si elle indique qu'aucune release publique n'existe, il n'y a rien à réparer sur
votre machine : l'étape est `unavailable`.

### Le SHA-256 ne correspond pas. Puis-je quand même essayer ?

Non. N'exécutez pas l'archive. Supprimez le téléchargement concerné, téléchargez
de nouveau depuis la page officielle et comparez les 64 caractères.

### WSL ou Docker ne répond pas.

Exécutez séparément :

```powershell
wsl --version
docker version
docker compose version
```

La première commande en erreur identifie le prérequis à réparer. N'essayez pas
de modifier PostgreSQL avant que ces trois contrôles réussissent.

### PostgreSQL ne devient pas sain.

```powershell
docker compose -f .\deploy\docker-compose.yml ps
docker compose -f .\deploy\docker-compose.yml logs postgres
```

Vérifiez la présence de `ODYCER_DB_PASSWORD`, l'espace disque et l'absence de
conflit sur le port local. Ne copiez pas le mot de passe dans une demande d'aide.

### Le serveur fonctionne mais annonce le repli SQLite.

Ce résultat est partiel. Vérifiez que `config.json` utilise le port et le nom de
base du Compose livré avec la même release. Redémarrez le serveur seulement
après que PostgreSQL soit sain. Ne supprimez pas le fichier SQLite de repli tant
que ses données n'ont pas été examinées ou rattrapées par une procédure validée.

### Un port est déjà utilisé.

Identifiez d'abord le processus propriétaire avec les outils Windows ou Linux.
Ne l'arrêtez pas s'il appartient à un autre projet. Utilisez uniquement les
options de port documentées par la release et mettez à jour ensemble serveur,
client et contrôles de santé.

### Le serveur est sain mais Godot ne se connecte pas.

Contrôlez dans cet ordre :

1. compatibilité exacte template/serveur ;
2. service de login actif ;
3. adresse `localhost` et port du login ;
4. passage du login vers le serveur de jeu ;
5. journaux Godot, login et jeu à la même heure.

Un menu visible ne prouve pas la connexion.

### Le volume PostgreSQL a disparu.

Arrêtez les écritures. Ne recréez pas immédiatement un volume portant le même
nom. Inventoriez les volumes existants et recherchez la dernière sauvegarde
hors Docker avec son SHA-256. Une récupération se fait depuis une sauvegarde
vérifiée, pas depuis une supposition.

### La sauvegarde ou la restauration de contrôle échoue.

Conservez le dump et son empreinte. Vérifiez l'espace libre, la version des
outils PostgreSQL, la santé du conteneur et le message d'erreur complet. Le test
doit viser uniquement la base de contrôle ; n'utilisez pas la base active comme
cible de diagnostic.

### Le poste partagé devient trop lent.

Arrêtez proprement le client ou un module optionnel, puis observez CPU, mémoire
et disque. Réduisez les ressources attribuées à Docker ou désactivez les outils
de création non nécessaires. Ne concluez pas à une limite du serveur à partir
d'un poste saturé par Godot ou ComfyUI.

### Un module Tools Suite est absent.

Vérifiez son statut et la matrice de compatibilité de votre release. Un module
`under_construction`, `planned` ou absent n'est pas installable. Utilisez le
chemin serveur seul.

## Informations sûres à partager avec un LM

- versions de Windows, WSL, Docker et Compose ;
- version de la release ;
- noms des services et statut sain/non sain ;
- commande exécutée et message d'erreur ;
- heure et extrait de journal sans secret ;
- résultat attendu.

Ne partagez jamais mot de passe, secret JWT, clé privée, dump de base ou donnée
joueur.

Voir aussi les [prompts LM](../reference/llm-local-setup-prompts.md).
