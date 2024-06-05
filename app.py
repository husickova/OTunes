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

# Streamlit interface
st.markdown('<h1 class="center-text">OTunes pro TV Óčko</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="center-text">Nekonečné hudební playlisty co tě budou bavit.</h2>', unsafe_allow_html=True)
st.markdown('<p class="center-text">Vyber si oblíbený žánr:</p>', unsafe_allow_html=True)

# Selection for genres
genre = st.selectbox('žánr:', ('Vyberte', 'Random', 'Pop', 'Rock', 'HipHop', 'Electro', 'Country'))

if genre == 'Random':
    # Embed YouTube Music Player for Random
    youtube_music_playlist_url = "https://www.youtube.com/embed?listType=playlist&list=PLatjrwfoBSuz9av_uyCwqwyBJuggomNcg&autoplay=1"
    youtube_music_embed_code = f'''
    <iframe width="100%" height="380" src="{youtube_music_playlist_url}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    '''

    st.markdown(youtube_music_embed_code, unsafe_allow_html=True)
    log_usage('start')
    log_usage('stop')

elif genre == 'Pop':
    # Embed YouTube Music Player for Pop
    pop_playlist_url = "https://www.tunemymusic.com/share/bscxrl6ekk"
    pop_playlist_embed_code = f'''
    <iframe width="100%" height="380" src="{pop_playlist_url}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    '''

    st.markdown(pop_playlist_embed_code, unsafe_allow_html=True)
    log_usage('start')
    log_usage('stop')

elif genre in ['Rock', 'HipHop', 'Electro', 'Country']:
    st.markdown(f'<p class="center-text">{genre} playlist will be added soon.</p>', unsafe_allow_html=True)
