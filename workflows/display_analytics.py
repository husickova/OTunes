import streamlit as st
import json
import pandas as pd

# Načtení dat ze souboru streamlit-analytics.json
with open('streamlit-analytics.json', 'r') as file:
    data = json.load(file)

# Převedení dat na pandas DataFrame
df = pd.DataFrame(data['events'])

# Streamlit rozhraní pro zobrazení dat
st.title('Streamlit Analytics Data')
st.write(df)
