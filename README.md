# formation - Django fondamentaux

## Présentation
Ceci est la structure de base pour un projet Django destiné aux formations.

## Données
Les données de ce projet sont issus de l'Open Data du Ministère de la Culture. Il s'agit
* D'une part de la liste des musées de France : https://data.culture.gouv.fr/explore/dataset/liste-et-localisation-des-musees-de-france/information/
* D'autre part de leur fréquentation : https://data.culture.gouv.fr/explore/dataset/frequentation-des-musees-de-france/information/

Ces deux sources de données ont des données croisées permettant de retrouver les fréquentations par musée et leur
localisation géographique.

## Dépendances du projet
Le fichier requirements liste les dépendances nécessaires au projet dans son ensemble. Il s'agit de :
 * [Django](https://www.djangoproject.com/) : qui est le sujet du projet…
 * [Django REST Framework](https://www.django-rest-framework.org/) : le framework qui va nous permettre de créer des APIs.
 * [django-extensions](https://django-extensions.readthedocs.io/) : qui est une app ajoutant des fonctionalités à
   Django. C'est en particularité la fonctionnalité d'exécuter un script que nous utiliserons.
 * [IPython](https://ipython.org/) : parce que c'est mieux que le shell intéractif standard…

Le fichier contient aussi :
 * [flake8](https://flake8.pycqa.org/) : outil de validation statique de code
 * [pylint](https://pypi.org/project/pylint/) : outil d'analyse statique de code

Car vous vous doutez bien qu'on va aussi faire de la qualité…