import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Récupération des données depuis un fichier csv
df = pd.read_csv("./car_prices_clean.csv", delimiter = ',', encoding='utf-8')

##########################################################################################################################
# Implémenter la fonctionnalité de tri du jeu de données
##########################################################################################################################


# Menu déroulant des colonnes
colonnes = st.selectbox( 'Trier sur cette colonne :', ['year', 'make', 'model', 'trim', 'body', 'transmission', 'state', 'condition', 'odometer', 'color', 'interior', 'seller', 'mmr', 'sellingprice','saledate'], index = None, placeholder = 'Choisir une colonne' ) # enlever valeur par défaut

# Menu déroulant ascendant/descendant
asc_desc = st.selectbox('Type de tri', ['Croissant', 'Décroissant'], index = None, placeholder = 'Choisir un ordre')

# Tri selon la colonne sélectionnée
if colonnes :
    df = df.sort_values(by = colonnes)

    # Tri selon croissant/décroissant
    if asc_desc == 'Décroissant':
        df = df.sort_values(by = colonnes, ascending = False)

 

##########################################################################################################################
# Implémenter les fonctionnalités de filtre des lignes 
##########################################################################################################################
 

# Filtrer les lignes 

# On change le type de la colonne 'make'
df['make'] = df['make'].astype('category')

print(df.dtypes)


# Création du input pour la marque 
input_mark = st.text_input ('Marque du véhicule')


# Création du input pour le prix
min_price = df['sellingprice'].min()
max_price = df['sellingprice'].max()

input_price = st.slider ('Prix', value = [min_price, max_price ])

# Création du input pour la date de vente

    # Changement du type
#print(df.dtypes)
df['saledate'] = pd.to_datetime(df['saledate'])
#print(df.dtypes)

   
    # Affichage de la date de vente sans l'heure
column_config = {
    "saledate": st.column_config.DateColumn(
            "saledate",
            help="Date de la vente du véhicule",
            format="DD.MM.YYYY",
            step=1,
        ),
}
st.dataframe(df, use_container_width=True, height=600, 
             hide_index=True,
             column_config=column_config)
    

    # Input
min_date = df['saledate'].min()
max_date = df['saledate'].max()

input_price = st.date_input ('Choisir la date de vente', value = [min_date, max_date], format = 'DD.MM.YYYY')

