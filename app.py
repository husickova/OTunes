import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import schedule
import time
import threading
import pandas as pd
from datetime import datetime

# Spotify API credentials
CLIENT_ID = '0c03bcd06c194e39887207a52ff3d4c1'
CLIENT_SECRET = 'aa2524cc05f3481badc50458d8aeab5b'
REDIRECT_URI = 'https://otunesgit-dcrrmv3ymryxl9haxuvoq3.streamlit.app/#spotify-playlist-scheduler'

# Spotify authentication
scope = 'user-modify-playback-state user-read-playback-state'
sp_oauth = SpotifyOAuth(client_id=CLIENT_ID,
                        client_secret=CLIENT_SECRET,
                        redirect_uri=REDIRECT_URI,
                        scope=scope)

# Playlist URI
playlist_uri = 'spotify:playlist:6oQkWFEnlrUwJgT0mhLFrT'

# CSV file for logging usage data
LOG_FILE = 'usage_log.csv'

# Function to log usage data
def log_usage(action):
    if not action in ['start', 'stop']:
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

# Start playlist function
def start_playlist():
    token_info = sp_oauth.get_cached_token()
    if not token_info:
        auth_url = sp_oauth.get_authorize_url()
        st.write('Please go to this URL and authorize:', auth_url)
        response_code = st.text_input('Enter the authorization code: ')
        if response_code:
            token_info = sp_oauth.get_access_token(response_code)
    if token_info:
        sp = spotipy.Spotify(auth=token_info['access_token'])
        # Get the user's current playback
        playback = sp.current_playback()
        if playback is None or playback['is_playing'] == False:
            # Start playing the playlist
            sp.start_playback(context_uri=playlist_uri)
        log_usage('start')

# Function to run schedule loop
def play_playlist_loop():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Schedule the playlist to start at a specific time
schedule.every().day.at("10:00").do(start_playlist)

# Run the schedule in a separate thread
t = threading.Thread(target=play_playlist_loop)
t.start()

# Streamlit interface
st.title('OTunes for TV Óčko')

if st.button('Play'):
    start_playlist()
    st.write('Otunes started!')

# Log when the user stops using the app
log_usage('stop')

st.write('The playlist will automatically start playing at 10:00 AM every day.')
