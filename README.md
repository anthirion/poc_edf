# Présentation
Ce code a pour vocation à automatiser la complétion d'un fichier excel via des appels API de l'API CountryLayer. Un fichier Excel d'exemple est donné dans le dossier.
L'Excel liste un certain nombre de pays dans une colonne "Contry" puis le script appelle l'API CountryLayer pour compléter automatiquement les colonnes "Capital" et "Region".

## Librairies utilisées
- openpyxl pour l'automatisation de la complétion du fichier excel
- request pour les requêtes API

## Mises en gardes
- Ce code, utilisant openpyxl, ne fonctionne qu'avec le format .xlsx
- Le fichier excel à modifier doit être fermé pendant que le script s'exécute

## Utilisation
1. Reprendre le fichier Excel en exemple ou créer un nouveau fichier avec les colonnes "Country", "Capital city" et "Region" puis ne compléter que la colonne Country
2. Créer un compte gratuit sur countrylayer.com et copier votre clé d'accès
Tenez compte du fait qu'un compte gratuit limite le nombre d'appels API à 100 appels par mois donc faites attention au nombre de pays que vous mettez dans le fichier Excel pour ne pas utiliser votre quota d'appels gratuits trop vite.
3. Ajouter votre clé d'accès dans le .env.template et renommez le fichier .env
4. Une fois que tout est prêt, taper la commande suivante dans un terminal :
```
python main.py <nom_du_fichier_excel_a_completer>
```