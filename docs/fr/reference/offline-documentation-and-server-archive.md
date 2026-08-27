# Documentation hors ligne et archive serveur

Cette référence distingue les trois sorties documentaires d'Ultimate Odycer.
Elle s'adresse aux débutants accompagnés par un LM et aux opérateurs qui
vérifient une archive avant de l'exécuter.

> **État public :** aucune archive serveur publique n'est actuellement
> téléchargeable. La [page officielle des releases](https://www.ultimateodycer.com/releases/)
> reste l'unique source d'un futur fichier et de son SHA-256. Une construction
> locale de la documentation ne constitue pas une release serveur.

## Les trois sorties à ne pas confondre

| Sortie | Rôle | Preuve fournie | Ne prouve pas |
|---|---|---|---|
| Sources Markdown | contenu canonique français et anglais | validation du dépôt | publication Web |
| Paquet HTML hors ligne | lecture locale sans service Web | manifeste et empreintes des fichiers | serveur exécutable |
| Archive serveur | serveur, déploiement et documentation compatible | manifeste de release et SHA-256 publié | déploiement en production |

Le site Web et le paquet hors ligne doivent dériver des mêmes sources. Copier
manuellement une seconde version HTML créerait un contenu divergent.

## Contrat du paquet HTML hors ligne

La racine du paquet contient :

```text
index.html
docs-build-manifest.json
assets/
en/
fr/
```

`docs-build-manifest.json` déclare au minimum :

- le schéma `ultimate-odycer.docs-build.v1` ;
- `documentation_version` ;
- le commit source ;
- le point d'entrée `index.html` ;
- les langues française et anglaise ;
- `compatibility.server` ;
- la taille et le SHA-256 de chaque fichier.

Une page qui s'ouvre ne suffit pas. Un fichier absent, ajouté ou modifié par
rapport au manifeste invalide le paquet.

## Contrat de la future archive serveur

Après extraction, une archive conforme contient notamment :

```text
VERSION
SHA256SUMS.txt
RELEASE-MANIFEST.json
deploy/QUICKSTART.md
docs/index.html
docs/docs-build-manifest.json
```

`RELEASE-MANIFEST.json` relie la release à `docs/index.html`, à la version
documentaire, au commit source et à l'empreinte du manifeste documentaire. La
valeur `docs/docs-build-manifest.json -> compatibility.server` doit être
strictement égale au contenu de `VERSION`.

La Tools Suite reste optionnelle. Une archive serveur ne doit pas prétendre
contenir Dungeon, City, Architecture, Creature, Avatar Editor ou Asset Factory
si la release ne les liste pas réellement comme modules compatibles.

## Vérification Windows pour débutant

1. Vérifiez que le fichier et son SHA-256 existent sur la page officielle.
2. Comparez le SHA-256 de l'archive avant extraction.
3. Extrayez la version dans un nouveau dossier.
4. Vérifiez la présence des six chemins ci-dessus.
5. Comparez la compatibilité documentaire avec la version serveur :

```powershell
$releaseVersion = (Get-Content .\VERSION -Raw).Trim()
$docsManifest = Get-Content .\docs\docs-build-manifest.json -Raw | ConvertFrom-Json
if ($docsManifest.compatibility.server -ne $releaseVersion) {
    throw "Documentation incompatible avec cette version serveur"
}
```

6. Ouvrez `docs/index.html` depuis le dossier extrait. Les pages essentielles
   doivent rester lisibles sans connexion réseau.
7. Continuez avec le `deploy/QUICKSTART.md` de cette même archive.

L'échec d'une étape donne le verdict `failed` ou `blocked`. Ne remplacez pas un
fichier manquant et ne modifiez pas un manifeste pour forcer la réussite.

## Questions-réponses

### Puis-je ajouter le ZIP documentaire au ZIP serveur moi-même ?

Pas pour créer une release officielle. L'empaqueteur serveur doit vérifier les
deux manifestes, la compatibilité et toutes les empreintes avant de produire
l'archive. Une copie manuelle est seulement un dossier local non certifié.

### `docs/index.html` fonctionne : la release est-elle valide ?

Non. Cela prouve uniquement que ce fichier peut être ouvert. Le SHA-256 de
l'archive, les manifestes, la version, les exécutables et l'extraction doivent
également être vérifiés.

### Le manifeste indique `unavailable`.

Il s'agit d'une preuve documentaire locale sans version serveur publique
compatible. Ne l'associez pas à un numéro inventé.

## Prompt LM réutilisable

```text
Aide-moi à vérifier cette archive Ultimate Odycer sans l'exécuter. Utilise
uniquement la page officielle des releases et les fichiers extraits VERSION,
SHA256SUMS.txt, RELEASE-MANIFEST.json, docs/index.html et
docs/docs-build-manifest.json. Compare exactement la version serveur et
compatibility.server, puis classe chaque contrôle passed, failed, blocked ou
unavailable. Ne fabrique aucune version ou empreinte, ne modifie aucun
manifeste, ne demande aucun secret et arrête-toi au premier échec.
```

Voir ensuite la [liste d'acceptation](local-setup-acceptance-checklist.md) ou
l'[index avancé](local-setup-advanced-index.md).
