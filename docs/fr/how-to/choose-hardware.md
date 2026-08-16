# Choisir du matériel PNJ avec un budget limité

Utilisez ce guide lorsque vous devez choisir entre une carte ESP32, un Raspberry
Pi, un mini-PC N100 neuf et un PC professionnel reconditionné. Le meilleur achat
est parfois de conserver le matériel déjà disponible.

## 1. Définir le niveau de dialogue

Choisissez le besoin le plus proche :

| Besoin | Matériel de départ |
|---|---|
| Sons, grognements, patrons et vocabulaire fermé | ESP32 déjà disponible |
| Courtes variations générées dans un domaine très étroit | ESP32-S3 avec PSRAM |
| Dialogue local 1–3B partagé au coût d'achat minimal | PC professionnel reconditionné x86, 16 Go ou plus |
| Petit serveur neuf, silencieux et sobre | Mini-PC N100, après vérification de la RAM et du SSD |
| GPIO, HAT, caméra ou capteurs Linux indispensables | Raspberry Pi 5 |

Une microSD augmente le stockage, pas la RAM ni la puissance de calcul.

## 2. Comparer le coût complet

Les valeurs suivantes sont `estimated`, datées d'août 2026, et ne constituent
pas des devis :

| Option | Coût complet indicatif | Limite principale |
|---|---:|---|
| ESP32 classique déjà possédé avec module SD/audio | 5–15 € supplémentaires | Pas adapté à un LLM de plusieurs millions de paramètres |
| ESP32-S3 N16R8 avec SD/audio | 15–40 € | Modèle et vocabulaire très contraints |
| PC professionnel reconditionné Tiny/Micro/Mini, 16/256 | 140–220 € | État, génération du CPU et alimentation à contrôler |
| PC professionnel reconditionné SFF, 16/256 | 100–220 € | Plus volumineux ; consommation à mesurer à la prise |
| Mini-PC N100 neuf, 8/128 ou 16/256 | Prix réel du vendeur + mises à niveau | RAM parfois soudée, refroidissement et SSD variables |
| Raspberry Pi 5 4 Go complet | 170–200 € | RAM limitée et coût des accessoires |

Ces fourchettes sont des scénarios budgétaires, pas une observation du marché.
Enregistrez le prix daté de l'annonce retenue comme `observed`. Ajoutez toujours
alimentation, refroidissement, stockage, câbles, garantie, éventuelles mises à
niveau et consommation mesurée localement. Une carte nue n'est pas un système
complet.

## 3. Appliquer la règle d'achat

N'achetez rien lorsque l'appareil disponible respecte déjà la qualité, la
latence et le débit requis. Achetez seulement si un banc démontre un écart qui
empêche l'usage visé.

Pour un mini-PC ou un PC professionnel reconditionné, vérifiez avant achat :

- au moins 16 Go de RAM, remplaçable si possible ;
- SSD de 256 Go ou plus, avec type et emplacement annoncés ;
- refroidissement actif et accès aux pièces ;
- processeur avec instructions AVX2 pour les runtimes CPU usuels ;
- système d'exploitation et licence clairement indiqués ;
- garantie, vendeur et politique de retour identifiables ;
- adaptateur secteur d'origine ou compatible inclus ;
- absence de mot de passe BIOS, de verrouillage d'entreprise ou d'inventaire ;
- réseau réellement décrit en Gb/s, pas une traduction ambiguë de la fréquence
  Wi-Fi.

Les familles courantes sont Lenovo ThinkCentre Tiny, Dell OptiPlex Micro et HP
EliteDesk/ProDesk Mini. Les boîtiers SFF plus grands sont souvent moins chers et
plus faciles à refroidir ou à étendre. Ce sont des familles à rechercher, pas
des recommandations de vendeur ou des preuves de performance.

Consultez la procédure [Acheter un PC professionnel reconditionné](buy-refurbished-business-pc.md)
avant de comparer une annonce avec un N100 neuf.

## 4. Refuser les raccourcis

- « Le modèle tient en RAM » ne prouve pas une latence acceptable.
- « Double réseau 2,5 GHz » ne prouve pas deux ports Ethernet 2,5 Gb/s.
- Le nombre de profils stockés ne prouve pas le nombre de conversations actives.
- Le TDP du processeur n'est ni la consommation du système à la prise ni un banc
  de performance LLM.
- « Reconditionné » ne garantit ni une batterie CMOS neuve, ni un SSD sain, ni
  l'absence de verrouillage BIOS.
- Une démonstration ESP32-S3 ne prouve pas la compatibilité d'un ESP32 classique.

Après sélection, mesurez l'appareil avec
[Mesurer la capacité PNJ](measure-npc-capacity.md) avant d'annoncer un nombre de
PNJ pris en charge.
