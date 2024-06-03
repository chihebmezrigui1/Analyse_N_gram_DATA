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
- Utilisez pip pour installer les dépendances requises en exécutant la commande suivante :
pip install -r requirements.txt
#### Les dépendances suivantes seront installées :
gspread==6.1.2: Une bibliothèque pour l'authentification à un serveur Google pour accéder aux API GCP.
google-auth==2.29.0: Une bibliothèque pour travailler avec Google Sheets.
nltk==3.8.1: Une bibliothèque pour le traitement du langage naturel.
pandas==2.2.2: Une bibliothèque pour la manipulation de données.
matplotlib==3.9.0: Une bibliothèque pour la visualisation de données.
wordcloud==1.9.3: Une bibliothèque pour la création de nuages de mots.
