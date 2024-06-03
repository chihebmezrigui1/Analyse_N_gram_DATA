## Overview
Ce projet consiste à créer des fonctions en Python permettant d'interagir avec l'API Google Sheets via Google Cloud Platform, ainsi qu'à effectuer une analyse n-gram sur les données collectées.

## Instructions d'Installation
### Prerequisites
- Un éditeur de code ( ex : Vscode ) 
- Python 3 and pip
### Configuration de l'Environnement de Développement
- Clonez ce repository sur votre machine locale en utilisant la commande suivante : <br/>
git clone -b master https://github.com/chihebmezrigui1/etude_cas_gcp.git
- Accédez au répertoire du projet : <br/>
cd etude_cas_gcp
### Installation des Dépendances:
- Vous utilisez pip pour installer les dépendances requises en exécutant la commande suivante :
pip install -r requirements.txt
#### Les dépendances suivantes seront installées :
- gspread==6.1.2: <br/>Une bibliothèque pour l'authentification à un serveur Google pour accéder aux API GCP.
- google-auth==2.29.0:<br/> Une bibliothèque pour travailler avec Google Sheets.
- nltk==3.8.1:<br/> Une bibliothèque pour le traitement du langage naturel.
- pandas==2.2.2:<br/> Une bibliothèque pour la manipulation de données.
- matplotlib==3.9.0:<br/> Une bibliothèque pour la visualisation de données.
- wordcloud==1.9.3:<br/> Une bibliothèque pour la création de nuages de mots.
  
## Les fonctions utilisées :

### Fonction 1 : 
#### Configuration de l'API Google Sheets
- Vous accédez à la Console Google Cloud Platform et créez un nouveau projet.
##### Activer l'API Google Sheets :
- Dans le menu à gauche, allez dans "API & Services" > "Bibliothèques".
- Effectuez une recherche sur "Google sheets API" , Après cliquez sur "Activer" pour activer l'API .
##### Créer un fichier de configuration pour stocker le clé et les informations d'identification :
- Allez dans "API & Services" > "Identifiants" avec selection du "Compte de service" .
- Donnez un nom à votre compte de service et cliquez sur "Créer et continuerr".
- Choissisez le role "Editeur" , et après sur "OK" .
##### Générer et télécharger la clé de compte de service :
- Dans la partie "Comptes de services" , vous trouverez votre compte de service . Comme vous pouvez le voir dans mon exemple dans le screenshot :
  ![image](https://github.com/chihebmezrigui1/etude_cas_gcp/assets/99685119/04f1e7a7-5a6f-4731-8ab5-c54734f130d8)
- Cliquez sur "Gérer les comptes de service", puis sur les trois points et sélectionnez "Gérer une clé". Ensuite, vous serez redirigé vers une page où il y a un bouton "Ajouter une clé". Cliquez dessus, puis choisissez "Créer une clé" et sélectionnez le format JSON. Félicitations ! Votre clé sera téléchargée . 😃👏
- La fonction "connexion_to_googlesheets" établit une connexion à l'API Google Sheets en utilisant un fichier JSON contenant les clés d'authentification.
  
### Fonction 2 : Analyse n-gram
- La fonction "clean_text" est utilisée pour nettoyer et prétraiter les données textuelles en français.
- La fonction "generate_ngrams" génère des n-grammes à partir d'un texte donné : <br/> la bibliothèque nltk est utilisée pour générer des n-grammes à partir des mots nettoyés.
- La fonction "analyze_ngrams" analyse la fréquence des n-grammes dans une liste de textes : <br/> Elle est utile pour identifier les séquences de mots les plus courantes dans un corpus de données textuelles. 
- J'ai chargé les données textuelles depuis un fichier CSV "data_science_phrases.csv" pour effectuer l'analyse n-gram à l'aide des fonctions définies précédemment .
- La Fonction "vis_nuage_mots" visualise les données de n_grams et leurs fréquence sous forme d'un nuage de mots : <br/>
  Un exemple pour Visualisation des données de 1_grams et leur fréquence .
![image](https://github.com/chihebmezrigui1/etude_cas_gcp/assets/99685119/0e0e8281-6e4b-42c8-96a0-26c22514de12)
"NB : Vous trouverez les autres captures de vis dans le dossier images, sous-dossier data."
### Fonction 2 : Remplir un Google Sheets à partir d'un DataFrame

