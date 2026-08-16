# Choisir du matériel PNJ avec un budget limité

Utilisez ce guide lorsque vous devez choisir entre une carte ESP32, un Raspberry
Pi et un mini-PC. Le meilleur achat est parfois de conserver le matériel déjà
disponible.

## 1. Définir le niveau de dialogue

Choisissez le besoin le plus proche :

| Besoin | Matériel de départ |
|---|---|
| Sons, grognements, patrons et vocabulaire fermé | ESP32 déjà disponible |
| Courtes variations générées dans un domaine très étroit | ESP32-S3 avec PSRAM |
| Dialogue local de modèle 1–3B partagé | Mini-PC x86 avec 16 Go de RAM |
| GPIO, HAT, caméra ou capteurs Linux indispensables | Raspberry Pi 5 |

Une microSD augmente le stockage, pas la RAM ni la puissance de calcul.

## 2. Comparer le coût complet

Les valeurs suivantes sont `estimated`, datées d'août 2026, et ne constituent
pas des devis :

| Option | Coût complet indicatif | Limite principale |
|---|---:|---|
| ESP32 classique déjà possédé avec module SD/audio | 5–15 € supplémentaires | Pas adapté à un LLM de plusieurs millions de paramètres |
| ESP32-S3 N16R8 avec SD/audio | 15–40 € | Modèle et vocabulaire très contraints |
| Mini-PC professionnel reconditionné, 16/256 | 140–220 € | Débit à mesurer selon CPU et modèle |
| Raspberry Pi 5 4 Go complet | 170–200 € | RAM limitée et coût des accessoires |

Ajoutez toujours alimentation, refroidissement, stockage, câbles, garantie et
consommation mesurée localement. Une carte nue n'est pas un système complet.

## 3. Appliquer la règle d'achat

N'achetez rien lorsque l'appareil disponible respecte déjà la qualité, la
latence et le débit requis. Achetez seulement si un banc démontre un écart qui
empêche l'usage visé.

Pour un mini-PC home lab, vérifiez avant achat :

- au moins 16 Go de RAM, remplaçable si possible ;
- SSD de 256 Go ou plus, avec type et emplacement annoncés ;
- refroidissement actif et accès aux pièces ;
- processeur avec instructions AVX2 pour les runtimes CPU usuels ;
- système d'exploitation et licence clairement indiqués ;
- garantie, vendeur et politique de retour identifiables ;
- réseau réellement décrit en Gb/s, pas une traduction ambiguë de la fréquence
  Wi-Fi.

## 4. Refuser les raccourcis

- « Le modèle tient en RAM » ne prouve pas une latence acceptable.
- « Double réseau 2,5 GHz » ne prouve pas deux ports Ethernet 2,5 Gb/s.
- Le nombre de profils stockés ne prouve pas le nombre de conversations actives.
- Une démonstration ESP32-S3 ne prouve pas la compatibilité d'un ESP32 classique.

Après sélection, mesurez l'appareil avec
[Mesurer la capacité PNJ](measure-npc-capacity.md) avant d'annoncer un nombre de
PNJ pris en charge.
