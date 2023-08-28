# formation - Django fondamentaux

## Présentation
Ceci est la structure de base pour un projet Django destiné aux formations.

## Dépendances Django
Ce projet utilise une app d'un autre projet. Vous devez donc vous assurer de disposer de cette
app avant de lancer le projet.

Vous pouvez placer la dépendance où vous le souhaitez et il faudra l'indiquer au projet.

Pour cela, dupliquez le fichier `.env-demo` et renommez-le `.env`. Ce dernier **ne devra pas être
mis sous contrôle de version !** De toutes manières, il est déclaré dans le `.gitignore`.

Remplacez les valeurs dans ce fichier par les vôtres.

## Préparation de l'environnement
Créez si vous le souhaitez un environnement virtuel (fortement conseillé) et activez le.

Installez les dépendances avec `pip install -r requirements.txt`. Les dépendances sont expliquées
ci-dessous.

## Structure du projet
Ce projet n'est que le squelette pour construire une app Django.

Le répertoire `scripts` contient les scripts de _maintenance_ qui consistent pour ce projet à
charger les données. Les données en elles même sont dans le répertoire `assets`. Elles sont
décrites ci-dessous.

## Données
Les données de ce projet sont issus d'une part de l'Open Data du Ministère de la Culture. Il s'agit
* De la liste des musées de France : https://data.culture.gouv.fr/explore/dataset/liste-et-localisation-des-musees-de-france/information/
* De leur fréquentation : https://data.culture.gouv.fr/explore/dataset/frequentation-des-musees-de-france/information/

Ces deux sources de données ont des données croisées permettant de retrouver les fréquentations par musée et leur
localisation géographique.

D'autres données de ce projet proviennent de [l'INSEE](https://www.insee.fr/) et sont plus
spécifiquement le [Code officiel géographique au 1er janvier 2023](https://www.insee.fr/fr/information/6800675).

3 fichiers au format CSV sont présents dans le répertoire `assets` pour une facilité d'accès :
 * v_departement qui est la liste des départements
 * v_region qui est la liste des régions
 * v_pays qui est la liste des pays

Le site de l'INSEE contient la description du contenu de ces fichiers. En résumé, vous avez… 

Pour les départements :
 * Code département
 * Code région
 * Code de la commune chef-lieu
 * Type de nom en clair
 * Nom en clair (majuscules)
 * Nom en clair (typographie riche) 
 * Nom en clair (typographie riche) avec article

Pour les régions :
 * Code région
 * Code de la commune chef-lieu
 * Type de nom en clair
 * Nom en clair (majuscules)
 * Nom en clair (typographie riche)
 * Nom en clair (typographie riche) avec article

Pour les pays :
 * Code du pays ou territoire
 * Code actualité du pays
 * Code officiel géographique de l'ancien pays de rattachement
 * Code officiel géographique de l'actuel pays de rattachement
 * Année d'indépendance
 * Libellé utilisé dans le COG
 * Nom officiel du pays
 * Ancien nom du pays
 * Code du pays sur 2 caractères conforme à la norme internationale ISO 3166 de représentation des noms de pays
 * Code du pays sur 3 caractères conforme à la norme internationale ISO 3166 de représentation des noms de pays
 * Code du pays à 3 chiffres conforme à la norme internationale ISO 3166 de représentation des noms de pays


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
 * [python-dotenv](https://pypi.org/project/python-dotenv/) : utilisé pour la configuration du projet

Car vous vous doutez bien qu'on va aussi faire de la qualité…