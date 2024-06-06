import streamlit as st
import pandas as pd
from datetime import datetime

# CSV file for logging usage data
LOG_FILE = 'usage_log.csv'

# Function to log usage data
def log_usage(action):
    if action not in ['start', 'stop']:
        return
    # Load existing data
    try:
        df = pd.read_csv(LOG_FILE)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['timestamp', 'action'])
    # Append new data
    new_data = pd.DataFrame({'timestamp': [datetime.now()], 'action': [action]})
    df = pd.concat([df, new_data], ignore_index=True)
    # Save to CSV
    df.to_csv(LOG_FILE, index=False)

# CSS styles to center the text
st.markdown(
    """
    <style>
    .center-text {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# URL of the logo image
logo_url = "https://github.com/husickova/OTunes/blob/1f9b0eadead3466179d38feb98ad0af8e625696e/images/logo.png"

# Streamlit interface
st.markdown(f'<img src="{logo_url}" class="center-text" alt="OTunes Logo" width="200">', unsafe_allow_html=True)
st.markdown('<h2 class="center-text">Neverending music channels full of music you love.</h2>', unsafe_allow_html=True)
st.markdown('<p class="center-text">Choose your favorite channel:</p>', unsafe_allow_html=True)

# Selection for genres
genre = st.selectbox('Channels:', ('Choose', 'OTunes POP', 'OTunes ROCK', 'OTunes HIPHOP', 'OTunes ELECTRO', 'OTunes COUNTRY'))

if genre == 'OTunes POP':
    # Embed YouTube Music Player for Pop
    pop_playlist_url = "https://www.youtube.com/embed?listType=playlist&list=PLatjrwfoBSuxxjxuA4VqoDPhe_bWEGSJ-&autoplay=1"
    pop_playlist_embed_code = f'''
    <iframe width="100%" height="380" src="{pop_playlist_url}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    '''

    st.markdown(pop_playlist_embed_code, unsafe_allow_html=True)
    log_usage('start')
    log_usage('stop')

elif genre == 'OTunes ROCK':
    # Embed YouTube Music Player for Rock
    rock_playlist_url = "https://www.youtube.com/embed?listType=playlist&list=PLatjrwfoBSuxGIzdXo07_4-SAe-ZltkNE&autoplay=1"
    rock_playlist_embed_code = f'''
    <iframe width="100%" height="380" src="{rock_playlist_url}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    '''

    st.markdown(rock_playlist_embed_code, unsafe_allow_html=True)
    log_usage('start')
    log_usage('stop')

elif genre == 'OTunes ELECTRO':
    # Embed YouTube Music Player for Electro
    electro_playlist_url = "https://www.youtube.com/embed?listType=playlist&list=PLatjrwfoBSuz9XAw-X-y5EsF-O62ZrAIf&autoplay=1"
    electro_playlist_embed_code = f'''
    <iframe width="100%" height="380" src="{electro_playlist_url}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    '''

    st.markdown(electro_playlist_embed_code, unsafe_allow_html=True)
    log_usage('start')
    log_usage('stop')

elif genre == 'OTunes HIPHOP':
    # Embed YouTube Music Player for HipHop
    hiphop_playlist_url = "https://www.youtube.com/embed?listType=playlist&list=PLatjrwfoBSuz-zbfooyidyyiwooJWfSG4&autoplay=1"
    hiphop_playlist_embed_code = f'''
    <iframe width="100%" height="380" src="{hiphop_playlist_url}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    '''

    st.markdown(hiphop_playlist_embed_code, unsafe_allow_html=True)
    log_usage('start')
    log_usage('stop')

elif genre == 'OTunes COUNTRY':
    # Embed YouTube Music Player for Country
    country_playlist_url = "https://www.youtube.com/embed?listType=playlist&list=PLatjrwfoBSuzQjOKCrPtE6Vbo3rdF1TsZ&autoplay=1"
    country_playlist_embed_code = f'''
    <iframe width="100%" height="380" src="{country_playlist_url}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    '''

    st.markdown(country_playlist_embed_code, unsafe_allow_html=True)
    log_usage('start')
    log_usage('stop')
