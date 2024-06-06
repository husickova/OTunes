import streamlit as st
import json
import pandas as pd
import os

# Zkontrolujte aktuální pracovní adresář
current_directory = os.getcwd()
st.write(f"Aktuální pracovní adresář: {current_directory}")

# Zobrazte všechny soubory v aktuálním adresáři
st.write("Soubory v aktuálním adresáři:")
st.write(os.listdir(current_directory))

# Zkontrolujte, zda soubor existuje
file_path = 'streamlit-analytics.json'
if os.path.exists(file_path):
    # Načtení dat ze souboru streamlit-analytics.json
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Převedení dat na pandas DataFrame
    df = pd.DataFrame(data['events'])

    # Streamlit rozhraní pro zobrazení dat
    st.title('Streamlit Analytics Data')
    st.write(df)
else:
    st.error(f'Soubor {file_path} neexistuje.')
