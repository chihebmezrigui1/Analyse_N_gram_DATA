import re
from google.oauth2.service_account import Credentials
import gspread
import pandas as pd
from collections import Counter
from nltk.corpus import stopwords
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from wordcloud import WordCloud


#--------------------------------  Fonction 1 : Connection à l’API Google Sheets  --------------------------------------

# Accès au service Google Sheet API
def connexion_to_googlesheets(json_keyfile):
    try:
        SCOPES = ["https://www.googleapis.com/auth/spreadsheets",
                  "https://www.googleapis.com/auth/drive"]
        
        credentials = Credentials.from_service_account_file(json_keyfile, scopes=SCOPES)
        user = gspread.authorize(credentials)
        
        print("Connection à l'API Google Sheets réussie.")
        return user
    except Exception as e:
        print(f"Erreur lors de la connection: {e}")
        return None


#-------------------------------- Fonction 2 : Analyse n-gram --------------------------------


# Fonction pour nettoyer et prétraiter les données textuelles
def clean_text(text):
    # Convertir le texte en minuscules
    text = text.lower()
    # Remplacer les lettres accentuées par des lettres normales
    text = re.sub(r'[âãäå]', 'a', text)
    text = re.sub(r'[ç]', 'c', text)
    text = re.sub(r'[èéêë]', 'e', text)
    text = re.sub(r'[ìíîï]', 'i', text)
    text = re.sub(r'[òóôõö]', 'o', text)
    text = re.sub(r'[ùúûü]', 'u', text)
    text = re.sub(r'[ÿ]', 'y', text)

    # Supprimer les caractères spéciaux et les chiffres
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Tokeniser le texte
    words = word_tokenize(text)
    # Supprimer les mots vides (stop words)
    stop_words = set(stopwords.words('french'))
    words = [
        word for word in words 
             if word not in stop_words
    ]
    return words


# Générer les n-grams
def generate_ngrams(text, n):
    words = clean_text(text)
    n_grams = ngrams(words, n)
    return [' '.join(grams) for grams in n_grams]


# Analyser la fréquence des n-grams
def analyze_ngrams(texts, n):
    all_ngrams = []
    for text in texts:
        all_ngrams.extend(generate_ngrams(text, n))
    n_gram_counts = Counter(all_ngrams)
    return n_gram_counts.most_common() # triés par leur fréquence




# Charger les données textuelles depuis le fichier CSV
csv_file_path = r'D:\work\ESKIMOZ\data\data_science_phrases.csv'
df = pd.read_csv(csv_file_path)

# On prend la colonne 'texte' qui contient les données textuelles .
texts = df['texte'].dropna().tolist()

# Déterminer la longueur maximale des textes
max_length = max(len(clean_text(text)) for text in texts)
print("longueur",max_length)

# Dictionnaire pour stocker les résultats des n-grams de différentes tailles
ngrams_results = {}

# Générer et analyser des n-grams automatiquement jusqu'à la longueur maximale des textes
for n in range(1, max_length + 1):
    ngrams_results[n] = analyze_ngrams(texts, n)
    # print(f"{n}-grams les plus fréquents:", ngrams_results[n])

# Sauvegarder les résultats dans des fichiers CSV
for n, ngrams in ngrams_results.items():
    ngrams_df = pd.DataFrame(ngrams, columns=[f'{n}-gram', 'frequency'])
    ngrams_df.to_csv(f'D:/work/ESKIMOZ/data/{n}grams_frequency.csv', index=False)

print(f"Les résultats ont été sauvegardés dans des fichiers CSV nommés '{n}grams_frequency.csv' pour n allant de 1 à {max_length}.")



# VISUALISATION DES DONNEES 


# Fonction pour la visualisation des données de n_grams et leurs fréquence sous forme d'un nuage de mots

def vis_nuage_mots(ngrams_results, n):
    # Préparer les n_grams et leurs fréquences en les Convertir en un dictionnaire
    ngrams_dict = dict(ngrams_results[n])
    # print("afficher dictionnaire",ngrams_dict)
        
    # Création du nuage de mots
    wordcloud = WordCloud(width=900, height=400, background_color='white').generate_from_frequencies(ngrams_dict)
    # Affichage
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')    
    plt.axis('off')
    plt.title(f'Nuage de mots des {n}-grams les plus fréquents')
    plt.show()



# On applique cette fonction pour visualiser le nuage des mots de 1gram les plus fréquents
n=1
vis_nuage_mots(ngrams_results, 3)


# Fonction pour la visualisation des données de n_grams et leurs fréquence sous forme des barres horizontales .
def plot_ngrams(ngrams_results, n):
    ngrams, frequencies = zip(*ngrams_results[n])
    plt.figure(figsize=(10, 6))
    plt.barh(ngrams, frequencies, color='orange')
    plt.xlabel('Fréquence')
    plt.ylabel(f'{n}-gram')
    plt.title(f'{n}-grams les plus fréquents')
    plt.gca().invert_yaxis()
    plt.show()


# On applique cette fonction pour visualiser les 5grams les plus fréquents
n=8
plot_ngrams(ngrams_results, 8)




# -------------------------- Fonction 3 : Remplir un Google Sheets à partir d'un DataFrame  -----------------------------------

# Fonction pour mettre à jour Google Sheets avec un DataFrame
def update_google_sheet(user, spreadsheet_id, sheet_name, dataframe):
    try:
        # Ouvrir le Google Sheet par son ID
        sheet = user.open_by_key(spreadsheet_id)
        worksheet = sheet.worksheet(sheet_name)
        
        # Convertir le DataFrame en liste de listes
        values = [dataframe.columns.values.tolist()] + dataframe.values.tolist()
        worksheet.clear()

        # Mettre à jour les données dans Google Sheets à partir du col A1
        worksheet.update('A1', values)
        
        print("Update de Google Sheets réussie.")
    except Exception as e:
        print(f"Erreur lors de l'update': {e}")




json_url = r'D:\work\ESKIMOZ\eskimoz-etude-cas-46017-d740eda083ad.json' 
# Connexion à l'API Google Sheets
user = connexion_to_googlesheets(json_url)

# Chargement du DataFrame à partir d'un fichier CSV
data_science_phrases_path = r'D:\work\ESKIMOZ\data\7grams_frequency.csv'
df = pd.read_csv(data_science_phrases_path)
print("DataFrame chargé avec succès.")
print(df.head(10))

# ID du Google Sheets
spreadsheet_id = '1dHjS38Er2VyDM__OGn5AlhnXj1EzlF7QdEYwOVmIH50'
sheet_name = 'myfile' 

# Mettre à jour le Google Sheets avec les données du DataFrame
update_google_sheet(user, spreadsheet_id, sheet_name, df)
