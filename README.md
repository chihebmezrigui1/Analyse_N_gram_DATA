## Overview
Ce projet consiste à créer des fonctions en Python permettant d'interagir avec l'API Google Sheets via Google Cloud Platform, ainsi qu'à effectuer une analyse n-gram sur les données collectées.

## Instructions d'Installation
### Prerequisites
- Un éditeur de code ( ex : Vscode ) 
- Python 3 and pip
### Configuration de l'Environnement de Développement
- Clonez ce repository sur votre machine locale en utilisant la commande suivante :
git clone https://github.com/chihebmezrigui1/etude_cas_gcp.git
- Accédez au répertoire du projet :
cd etude_cas_gcp
### Installation des Dépendances:
- Vous utilisez pip pour installer les dépendances requises en exécutant la commande suivante :
pip install -r requirements.txt
#### Les dépendances suivantes seront installées :
- gspread==6.1.2: Une bibliothèque pour l'authentification à un serveur Google pour accéder aux API GCP.
- google-auth==2.29.0: Une bibliothèque pour travailler avec Google Sheets.
- nltk==3.8.1: Une bibliothèque pour le traitement du langage naturel.
- pandas==2.2.2: Une bibliothèque pour la manipulation de données.
- matplotlib==3.9.0: Une bibliothèque pour la visualisation de données.
- wordcloud==1.9.3: Une bibliothèque pour la création de nuages de mots.
### Configuration de l'API Google Sheets
- Vous accédez à la Console Google Cloud Platform et créez un nouveau projet.
#### Activer l'API Google Sheets :
- Dans le menu à gauche, allez dans "API & Services" > "Bibliothèques".
- Effectuez une recherche sur "Google sheets API" , Après cliquez sur "Activer" pour activer l'API .
#### Créer un fichier de configuration pour stocker le clé et les informations d'identification :
- Allez dans "API & Services" > "Identifiants" avec selection du "Compte de service" .
- Donnez un nom à votre compte de service et cliquez sur "Créer et continuerr".
- Choissisez le role "Editeur" , et après sur "OK" .
#### Générer et télécharger la clé de compte de service :
- Dans la partie "Comptes de services" , vous trouverez votre compte de service . Comme vous pouvez le voir dans mon exemple dans le screenshot :
  ![image](https://github.com/chihebmezrigui1/etude_cas_gcp/assets/99685119/04f1e7a7-5a6f-4731-8ab5-c54734f130d8)
- Cliquez sur "Gérer les comptes de service", puis sur les trois points et sélectionnez "Gérer une clé". Ensuite, vous serez redirigé vers une page où il y a un bouton "Ajouter une clé". Cliquez dessus, puis choisissez "Créer une clé" et sélectionnez le format JSON. Félicitations ! Votre clé sera téléchargée . 😃👏
  
## Les fonctions utilisées 
- La fonction connexion_to_googlesheets(json_keyfile) établit une connexion à l'API Google Sheets en utilisant un fichier JSON contenant les clés d'authentification. Elle prend en paramètre le chemin vers ce fichier JSON.

