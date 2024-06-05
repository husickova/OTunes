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

# Streamlit interface
st.title('OTunes for TV Óčko')
st.subheader('Neverending playlists full of music you love.')


# Embed YouTube Music Player
youtube_music_playlist_url = "https://www.youtube.com/embed?listType=playlist&list=PLatjrwfoBSuz9av_uyCwqwyBJuggomNcg&autoplay=1"
youtube_music_embed_code = f'''
<iframe width="100%" height="380" src="{youtube_music_playlist_url}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
'''

st.markdown(youtube_music_embed_code, unsafe_allow_html=True)

log_usage('start')
st.write('Listen and enjoy!')

log_usage('stop')
