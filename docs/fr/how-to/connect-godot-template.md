# Connecter un template Godot au serveur local

Statut : **guide de preuve bornée**. Les starters Godot publics contiennent des projets Godot réels et une fondation réseau transport-indépendante, mais **aucune compatibilité live avec le Zig canonique n'est encore prouvée**.

## Avant de commencer

- Godot Classic et VR ciblent 4.7.2, mais cette version reste `NOT_PROVEN` tant que les reçus exécutables n'existent pas.
- Les deux branches P0 fournissent désormais `tools/run_p0_local_proof.py`, orchestrateur fail-closed en une commande pour la preuve moteur + fixture synthétique avec le même binaire Godot exact.
- Le réseau VR historique reste `LEGACY_QUARANTINED`.
- Le contrat public d'intention ne contient aucun socket, endpoint, opcode ou framing Zig privé.
- Une date récente ou une documentation détaillée ne remplace jamais une baseline serveur exacte.

## 1. Exécuter localement la preuve moteur et synthétique

Avec **Godot 4.7.2-stable**, exécutez depuis le checkout de la PR concernée :

```text
python tools/run_p0_local_proof.py --godot <chemin-vers-godot-4.7.2>
```

L'orchestrateur utilise le même exécutable pour les deux gates et s'arrête au premier échec. Les reçus sont écrits sous `.evidence/` et doivent rester non commités.

Pour VR, toute cette preuve s'exécute XR désactivé. Même un succès complet laisse OpenXR, casque/contrôleurs et interopérabilité Zig non prouvés.

## 2. Lire les contrats dans l'ordre

1. architecture client ;
2. `network-contract.md` (`network-intent-v1`, synthétique et transport-indépendant) ;
3. `server-network-contract.md` en conservant son statut **snapshot non épinglé / compatibilité non validée** ;
4. proof levels + compatibility manifest du dépôt Godot.

## 3. Ne pas inventer le transport

Le futur adaptateur réel doit être dérivé d'une baseline `zig-server-v2` nommée. Tant que le SHA/tree/toolchain exact n'est pas capturé, n'ajoutez pas d'endpoint, d'opcode ou de framing supposé dans le starter public.

L'adaptateur/fixture actuel reste sans socket et peut uniquement prouver le comportement client borné sous entrées synthétiques contrôlées.

## 4. Frontière de la preuve synthétique

La fixture préparée couvre :

- état offline fail-closed ;
- connexion/authentification simulées ;
- intention de mouvement bornée ;
- événement autoritaire synthétique ;
- entrée malformée/non supportée ;
- rejet des champs d'autorité client ;
- déconnexion/reconnexion/reprise ;
- fermeture propre.

Une exécution réussie reste `SYNTHETIC_FIXTURE_ONLY`.

## 5. Preuve live future

`REAL_SERVER_E2E` exigera :

- révision client exacte ;
- SHA/tree/toolchain Zig exacts ;
- transport réellement présent à cette révision Zig vérifié ;
- auth + handoff + spawn ;
- mouvement autoritaire ;
- reconnexion ;
- tests négatifs/adversariaux ;
- logs/artefacts nommés.

Un menu, une scène statique, un mock, une fixture synthétique ou un run Godot headless ne suffit pas pour la compatibilité live.
