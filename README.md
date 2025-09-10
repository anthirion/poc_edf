# Présentation
Ce code a pour vocation à automatiser la complétion d'un fichier excel via des appels API de l'API CountryLayer. Un fichier Excel d'exemple est donné dans le dossier.
L'Excel liste un certain nombre de pays dans une colonne "Contry" puis le script appelle l'API CountryLayer pour compléter automatiquement les colonnes "Capital" et "Region".

## Librairies utilisées
- openpyxl pour l'automatisation de la complétion du fichier excel
- request pour les requêtes API

## Mises en gardes
- Ce code, utilisant openpyxl, ne fonctionne qu'avec les formats Excel suivants (après 2010) :
  - .xlsx
  - .xlsm
  - .xltx
  - .xltm

## Utilisation