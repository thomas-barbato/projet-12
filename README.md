# projet-12 
# Développez une architecture back-end sécurisée en utilisant Django ORM

Ce projet vise à créer une API RESTful *(Application Programming Interface)*
Cette API a pour but de permettre à une équipe de gestion évènementielle,
de créer une liste de clients, créer des contracts ainsi que des évènements.

Cette API a été écrite en utilisant **Django Rest Framework** et **JWT**, ainsi qu'une base de données **POSTGRESQL**. Et pour ce projet nous utiliserons **postman**.
#
**L'API doit permettre les actions suivantes :**

- Les employés sont répartis en 3 groupes : **SALES, SUPPORT et MANAGEMENT**
- Seuls les utilisateurs authentifiés peuvent accéder à l'API.
- L'interface d'administration n'est accessibles qu'au groupe MANAGEMENT. Elle permet d'y créer contracts, clients, évènements, utilisateurs...
- Le groupe SALES est capable de créer des clients
- Le groupe SALES est capable d'afficher et mettre à jour les clients qui leur sont attribués
- Le groupe SALES est capable d'afficher et de modifier les contracts des clients qui leur sont attribués.
- Le groupe SALES est capable de créer des évènements.
- Le groupe SUPPORT est capable d'afficher et mettre à jour les évènements qui leur sont attribués
- Le groupe SUPPORT est capable d'afficher les clients des évènements qui leur sont attribués.

## Installation de l'API:

Installez la dernière version de python , disponible ici : https://www.python.org/downloads/

Importez le projet depuis git: `git clone https://github.com/thomas-barbato/projet-12.git`

Créez un environnement virtuel :
`python3 -m venv /path/to/new/virtual/environment`
Ou `python -m virtualenv venv`

Activez l'environnement virtuel:
`cd Venv\Scripts\`
`.\activate.bat`
`cd .. `
`cd .. `

Installez les dépendances:
`pip install -r requirements.txt`

## Charger les données de test (étape optionnelle):

Pour charger les données contenues dans les fixtures, vous devez entrer la commande suivante:
`python manage.py loaddata 1_users.json, 2_clients.json, 3_contracts.json, 4_events.json`

Le mot de passe de chaque utilisateur est : `Thomas404*`

Lorsque vous n'en aurez plus besoin, vous pourrez nettoyer la base de données avec la commande suivante: `python manage.py flush`

## Démarrer le projet :

Pour démarrer le projet, entrez la commande suivante: `python manage.py runserver`

## Acceder à l'interface admin:

Pour accéder à l'interface d'administration, rendez-vous à l'url suivante :

``http://127.0.0.1:8000/admin``

- email: ``management1@email.com`` , password : ``Thomas404*``

## Acceder à postman

**Pour pouvoir lancer des requetes à l'API, nous utilisons donc POSTMAN
et maintenant qu'il est lancé, veuillez importer la collection qui se trouve
à cette url :**

``https://github.com/thomas-barbato/projet-12/blob/main/projet-12.postman_collection.json``

**Ensuite:**

1. Cliquez sur "importer"
2. Importer la collection précédemment téléchargée
3. Connectez-vous via l'un des comptes utilisateurs déjà créés (ou créez le vôtre) 
- via la collection: Dossier : User , fichier : login
- via l'url:``http://127.0.0.1:8000/api/login`` 

**Un exemple d'utilisateurs déjà créés que vous pouvez utiliser :**

- email: ``sales1@email.com`` , password : ``Thomas404*``
- email: ``support1@email.com`` , password : ``Thomas404*``
- email: ``management1@email.com`` , password : ``Thomas404*``

## Rapport Flake8

Ce projet respect la norme PEP8, vous pouvez consulter le rapport dans le dossier `flake8-report`.
Pour lancer un test par vous même, vous devrez installer la bibliothèque flake8-html avec la commande suivante:

`pip install -r requirements-testing.txt`

Un fichier de configuration se trouve à la racine du projet, se fichier ce nomme `setup.cfg`,
il vous permet de lancer flake8 sans avoir à ajouter d'option, vous devrez donc entrer la commande suivante:

`flake8 ./api/`