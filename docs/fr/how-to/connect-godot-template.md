# Connecter un template Godot au serveur local

Statut : **guide de preuve bornée**. Les starters Godot publics contiennent désormais un projet réel et une fondation réseau transport-indépendante, mais **aucune compatibilité live avec le Zig canonique n'est encore prouvée**.

## Avant de commencer

- Godot Classic et VR ciblent 4.7.2, mais cette version reste `NOT_PROVEN` tant que le validateur local n'a pas produit son reçu JSON.
- Le réseau VR historique est `LEGACY_QUARANTINED`.
- Le contrat public d'intention ne contient aucun socket, endpoint, opcode ou framing Zig privé.
- Une date récente ou une documentation détaillée ne remplace jamais une baseline serveur exacte.

## 1. Valider le moteur avant le réseau

Exécutez le validateur du dépôt choisi avec **Godot 4.7.2-stable** et conservez le reçu `.evidence/` local. Pour VR, un run headless avec `--xr-mode off` prouve seulement le chargement moteur ; il ne prouve ni OpenXR, ni casque, ni réseau.

Si la preuve moteur échoue, arrêtez ici.

## 2. Lire les contrats dans l'ordre

1. architecture client ;
2. `network-contract.md` (`network-intent-v1`, synthétique et transport-indépendant) ;
3. `server-network-contract.md` en conservant son statut **compatibilité non validée** ;
4. proof levels + compatibility manifest du dépôt Godot.

## 3. Ne pas inventer le transport

Le futur adaptateur réel doit être dérivé d'une baseline `zig-server-v2` nommée. Tant que le SHA/tree/toolchain exact n'est pas capturé, n'ajoutez pas d'endpoint, d'opcode ou de framing supposé dans le starter public.

L'adaptateur abstrait actuel peut gérer seulement le cycle :

```text
disconnected -> connecting -> authenticating -> online
```

sans socket réel.

## 4. Première preuve synthétique autorisée

La prochaine étape acceptable est une fixture locale synthétique qui teste :

- handshake simulé ;
- authentification simulée ;
- intention de mouvement bornée ;
- événement autoritaire entrant ;
- payload invalide ;
- déconnexion et reconnexion ;
- refus des champs client autoritaires.

Cette preuve devra rester `SYNTHETIC_FIXTURE_ONLY`.

## 5. Preuve live future

`REAL_SERVER_E2E` exigera :

- révision client exacte ;
- SHA/tree/toolchain Zig exacts ;
- auth + handoff + spawn ;
- mouvement autoritaire ;
- reconnexion ;
- tests négatifs ;
- logs/artefacts nommés.

Un menu, une scène statique, un mock ou un run Godot headless ne suffit pas.
