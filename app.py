# Import des librairies
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Récuperation de la liste des data set de seaborn
datasets = sns.get_dataset_names()

# Titre de l'application
st.title('Manipulation de données et création de graphiques')

# Affichage de la liste des datasets
dataset_selected = st.selectbox(
    'Quel dataset voulez-vous utiliser ?',
    datasets
)

# Affichage du dataset sélectionné
df_selected = sns.load_dataset(dataset_selected)

st.dataframe(df_selected)

# Choix de la colonne X et Y
x = st.selectbox(
    'Choississez la colonne X',
    df_selected.columns
)
y = st.selectbox(
    'Choississez la colonne Y',
    df_selected.columns
)


# Choix du type de graphique
graph_type = st.selectbox(
    'Quel type de graphique voulez-vous utiliser ?',
    ['scatterplot', 'barplot', 'lineplot']
)

# Affichage du graphique
graph = getattr(sns, graph_type)(data=df_selected, x='x', y='y')

plt.title(f'{graph_type.capitalize()} de {y} en fonction de {x}')
plt.xlabel(x)
plt.ylabel(y)

st.pyplot(graph.figure)

# Afficher ou non la matrice de corrélation
if st.checkbox('Afficher la matrice de corrélation'):
    # Calcul de la matrice de corrélation
    df_num = df_selected.select_dtypes(include=[np.number])
    corr = df_num.corr()

    # Affichage de la matrice de corrélation
    heatmap = sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm')
    st.pyplot(heatmap.figure)
