# Exploiter une pile Ultimate Odycer en home lab

Utilisez ce guide pour garder un laboratoire privé honnête. Ce n'est pas un
runbook de production, un guide de load-balancer, ni une checklist internet
public.

## 1. Rester dans la frontière publique

- documentation et outils de capacité PNJ de ce dépôt ;
- modèles JSON experimentaux du registre public ;
- starters clients documentation seulement ;
- inférence en boucle locale et fixtures synthétiques ;
- aucun point de production, donnee joueur ou copie de serveur propriétaire.

## 2. Préférer la boucle locale

Les listeners LLM locaux doivent rester en boucle locale. Un listener LAN
privé exige authentification, contrôles d'origine, pare-feu et plan de
repli. Un tutoriel n'autorise pas à exposer un service.

## 3. Observer sans revendiquer la production

Signaux locaux utiles :

- durée de réponse PNJ et politique de file de l'estimateur de capacité ;
- journaux structurés avec noms synthétiques ;
- comptes fail-closed : intentions refusées, sorties LLM remplaçées, timeouts.

Prometheus, Grafana, sharding multi-serveurs et sauvegarde de mondes live
restent non publiés. Ne collez pas d'IP, jetons ou journaux reels dans les
issues.

## 4. Changer d'échelle seulement avec une preuve

| Étape | Preuve autorisée | Pas une preuve |
|---|---|---|
| Home lab | validation docs, métriques PNJ synthétiques | CCU, confort VR, TLS de production |
| Staging isole | fixtures locales nommées, sans données joueur | failover multi-régions hébergé |
| Production | non publié | n'importe quelle page de ce dépôt |

Poursuivez avec [choisir le matériel](choose-hardware.md) et
[mesurer la capacité PNJ](measure-npc-capacity.md).
