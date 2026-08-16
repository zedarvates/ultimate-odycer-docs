# Acheter un PC professionnel reconditionné pour les PNJ

Utilisez ce guide pour évaluer une annonce Lenovo ThinkCentre Tiny, Dell
OptiPlex Micro, HP EliteDesk/ProDesk Mini ou un équivalent SFF. Le but est
d'obtenir un hôte LLM local réparable sans transformer une bonne affaire en
achat coûteux après mises à niveau.

## 1. Choisir le format

| Format | Point fort | Limite à vérifier |
|---|---|---|
| Tiny/Micro/Mini, environ 1 litre | Compact, pièces professionnelles documentées | Adaptateur secteur propriétaire, refroidissement serré |
| SFF | RAM, stockage et refroidissement souvent plus accessibles | Plus volumineux et consommation à mesurer |

Les noms de gamme sont des exemples de recherche, pas des recommandations de
vendeur. Vérifiez la fiche du modèle et son numéro de machine exact.

## 2. Fixer une configuration minimale

- 16 Go de RAM minimum ; 32 Go si le modèle, le contexte, STT/TTS et les autres
  services doivent cohabiter ;
- SSD de 256 Go minimum, de préférence NVMe, avec état SMART contrôlable ;
- processeur AVX2 ; six cœurs physiques constituent une cible pratique pour un
  hôte CPU d'occasion, pas une garantie de débit ;
- Ethernet Gigabit, alimentation incluse et refroidissement fonctionnel ;
- au moins un emplacement RAM ou stockage encore évolutif si possible.

Un Core i5-8500T rencontré dans des OptiPlex 7060 Micro ou ThinkCentre M720 Tiny
possède six cœurs et six threads. Son TDP annoncé de 35 W ne représente pas la
consommation de la machine à la prise. Le N100 possède quatre cœurs et quatre
threads avec une puissance de base annoncée de 6 W. Ces caractéristiques
officielles décrivent les processeurs ; elles ne prouvent pas lequel répond le
plus vite avec votre modèle LLM.

## 3. Calculer le coût complet

Additionnez :

```text
prix de l'annonce
+ RAM nécessaire
+ SSD nécessaire
+ alimentation manquante
+ Wi-Fi ou réseau supplémentaire
+ livraison et retour éventuel
+ électricité mesurée sur la durée prévue
```

Enregistrez séparément le prix `observed` de l'annonce, les ajouts `estimated`
et la décision finale. N'utilisez pas une fourchette générale comme preuve du
prix réellement disponible dans votre région.

## 4. Contrôler avant la fin du délai de retour

1. Ouvrez le BIOS et vérifiez l'absence de mot de passe administrateur ou de
   verrouillage d'inventaire.
2. Confirmez le CPU, la quantité de RAM, le nombre de barrettes et le SSD reçus.
3. Contrôlez SMART, puis exécutez un test mémoire.
4. Chargez le CPU pendant 20 à 30 minutes et notez température, bruit,
   throttling, erreurs et consommation à la prise.
5. Testez Ethernet, USB, sorties vidéo, redémarrage et reprise après coupure.
6. Si Windows est conservé, vérifiez une version encore prise en charge et
   l'éligibilité réelle de la machine. Windows 10 n'est plus pris en charge
   depuis le 14 octobre 2025 hors dispositif de mises à jour étendues.

Effacez l'ancien stockage et réinstallez un système depuis une source connue
avant d'y placer des données ou des identifiants du home lab.

## 5. Décider entre reconditionné, N100 et Raspberry Pi

Préférez le PC professionnel reconditionné lorsque sa configuration complète
16/256 ou 32/512, son alimentation et sa politique de retour coûtent moins cher
qu'un N100 mis au même niveau, et lorsque l'encombrement ou la consommation
mesurée restent acceptables. Préférez le N100 pour une machine neuve très sobre
et silencieuse si sa RAM et son stockage ne bloquent pas l'évolution. Préférez
le Raspberry Pi lorsque les GPIO, HAT ou capteurs sont le besoin principal.

Dans tous les cas, le nombre de PNJ pris en charge reste `unavailable` avant un
banc reproductible. Continuez avec [Mesurer la capacité PNJ](measure-npc-capacity.md).

## Sources techniques

- [Dell OptiPlex 7060 Micro — processeurs pris en charge](https://www.dell.com/support/manuals/fr-fr/optiplex-7060-micro/opti_7060_mff_setup_specs_manual/processeur?guid=guid-e178c653-4f96-4d67-8c6e-0d7e87454d21)
- [Lenovo ThinkCentre M720 Tiny — spécifications PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkCentre/ThinkCentre_M720_Tiny/ThinkCentre_M720_Tiny_Spec.html)
- [Intel — présentation officielle des processeurs série N](https://download.intel.com/newsroom/2023/client-computing/Intel-N-series-Processors-Media_Presentation.pdf)
- [Microsoft — fin de prise en charge de Windows 10](https://support.microsoft.com/fr-fr/windows/deployment/updates-lifecycle/windows-10-support-has-ended-on-october-14-2025)

Sources consultées le 16 août 2026. Les prix, stocks et garanties doivent être
relevés de nouveau au moment de l'achat.
