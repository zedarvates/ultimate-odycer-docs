# Connecter le template Three.js 2.5D à un serveur local

Statut : **guide pour travail futur ; aucune compatibilité navigateur existe
aujourd'hui**.

Cette page étend la [référence générale du contrat réseau](../reference/server-network-contract.md)
avec ce quelle signifie spécifiquement pour un client web. Elle ne transforme
pas le template documentaire en client jouable.

## Pourquoi le template ne peut pas se connecter aujourdhui

- Les services canoniques de login et de jeu parlent TCP binaire brut. Les
  navigateurs ne savent ouvrir que des connexions WebSocket ou HTTP ; une
  connexion directe est donc impossible.
- Le périmètre du template Three.js exige des contrats serveur-autoritaires
  documentés avant tout code réseau. Cette preuve existe désormais partiellement
  dans la référence du contrat, mais lécart de transport demeure.
- Le trafic WebSocket du WebAdmin est de la télémétrie administrative, pas un
  canal de jeu ; le réutiliser pour le gameplay violerait les frontières
d'autorité du serveur.

## Deux chemins acceptables

1. Un pont/passerelle documenté : un petit proxy local qui termine le
   WebSocket côté navigateur et parle le protocole TCP binaire au serveur. Il
   doit être publié avec sa propre revue de sécurité, ses règles de cadrage et
   sa fixture loopback.
2. Un point de terminaison WebSocket officiel ajouté au serveur canonique
   derrière son handshake existant, sa négociation de version et ses règles
   d'admission JWT, avec les mêmes garanties d'autorité.

Un troisième chemin, réimplémenter la logique protocole dans une page web non
revue, est rejeté par les règles de publication des deux projets.

## Ce qu'un client web conforme devra implémenter

- Encodage et décodage de trames exactement comme spécifié dans la référence
  du contrat, y compris entiers gros-boutiste et enveloppes préfixées par leur
  longueur.
- Le flux de session : handshake avec jeton JWT, liste/sélection de personnage,
  sélection de spawn avec nonce, puis mises à jour de position à cadence bornée.
- Analyse des lots binaires de réplication (opcode 80) avec interpolation entre
  lots et aucune autorité côté client.
- Attentes TLS alignées sur la configuration du serveur ; les connexions en
  clair échouent quand TLS est requis.
- Reconnexion via le jeton de reprise de session à usage unique lorsqu'il est
  fourni.

## Discipline de test local

Quand un pont ou un point de terminaison arrivera, validez dabord en loopback :

1. Démarrez la pile serveur locale depuis le [guide Windows](install-local-server-windows.md).
2. Confirmez que le service de login répond à un handshake sur son port
   configuré.
3. Réalisez création de compte, login, création/sélection de personnage et un
   spawn monde via le client web.
4. Enregistrez les versions du serveur, de la passerelle et du runtime
   navigateur dans une entrée de matrice de compatibilité, puis mettez à jour
   la décision SERVER-COMPATIBILITY du template.

Tant que l'étape 3 n'a pas été réalisée avec des artefacts nommés, cette page
reste un plan, pas une déclaration de capacité.
