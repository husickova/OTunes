import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
from datetime import datetime, timedelta
import schedule
import time
import threading
import os

# Spotify API credentials
CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID', '0c03bcd06c194e39887207a52ff3d4c1')
CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET', 'aa2524cc05f3481badc50458d8aeab5b')
REDIRECT_URI = 'https://otunesgit-dcrrmv3ymryxl9haxuvoq3.streamlit.app/callback'

# Initialize Spotify OAuth
sp_oauth = SpotifyOAuth(client_id=CLIENT_ID,
                        client_secret=CLIENT_SECRET,
                        redirect_uri=REDIRECT_URI,
                        scope='user-modify-playback-state user-read-playback-state')

# Playlist URI
playlist_uri = 'spotify:playlist:6oQkWFEnlrUwJgT0mhLFrT'

# Function to calculate the start position based on the current time
def calculate_start_position():
    now = datetime.now()
    midnight = datetime.combine(now.date(), datetime.min.time())
    elapsed_time = now - midnight
    return int(elapsed_time.total_seconds() * 1000)  # convert to milliseconds

# Function to log usage data
def log_usage(action):
    if action not in ['start', 'stop']:
        return
    # Load existing data
    try:
        df = pd.read_csv('usage_log.csv')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['timestamp', 'action'])
    # Append new data
    new_data = pd.DataFrame({'timestamp': [datetime.now()], 'action': [action]})
    df = pd.concat([df, new_data], ignore_index=True)
    # Save to CSV
    df.to_csv('usage_log.csv', index=False)

# Start playlist function
def start_playlist(token_info, position_ms=0):
    sp = spotipy.Spotify(auth=token_info['access_token'])
    # Get the user's current playback devices
    devices = sp.devices()
    if not devices['devices']:
        st.error('No active devices found. Please open Spotify on a device and try again.')
        return
    # Get the user's current playback
    playback = sp.current_playback()
    if playback is None or not playback['is_playing']:
        # Start playing the playlist from the specified position
        try:
            sp.start_playback(context_uri=playlist_uri, position_ms=position_ms)
            log_usage('start')
        except spotipy.SpotifyException as e:
            st.error(f'Error starting playback: {e}')
    else:
        st.info('Playback is already running.')

# Function to ensure continuous playback
def ensure_continuous_playback(token_info):
    sp = spotipy.Spotify(auth=token_info['access_token'])
    while True:
        playback = sp.current_playback()
        if playback is None or not playback['is_playing']:
            try:
                sp.start_playback(context_uri=playlist_uri, position_ms=calculate_start_position())
            except spotipy.SpotifyException as e:
                st.error(f'Error ensuring continuous playback: {e}')
        time.sleep(30)  # Check every 30 seconds

# Function to run schedule loop
def play_playlist_loop(token_info):
    while True:
        schedule.run_pending()
        time.sleep(1)

# Schedule the playlist to start at a specific time
def schedule_playlist(token_info):
    schedule.every().day.at("00:00").do(start_playlist, token_info, position_ms=0)
    # Run the schedule in a separate thread
    t1 = threading.Thread(target=play_playlist_loop, args=(token_info,))
    t1.start()
    # Ensure continuous playback in a separate thread
    t2 = threading.Thread(target=ensure_continuous_playback, args=(token_info,))
    t2.start()

# Streamlit interface
st.title('OTunes for TV Óčko')

# Get the query parameters
query_params = st.experimental_get_query_params()
code = query_params.get('code')

# Check if we have an access token
token_info = None

if code:
    token_info = sp_oauth.get_access_token(code)
    if not token_info or not token_info.get('access_token'):
        st.write('Failed to fetch access token.')
else:
    token_info = sp_oauth.get_cached_token()

if token_info and token_info.get('access_token'):
    position_ms = calculate_start_position()
    start_playlist(token_info, position_ms=position_ms)  # Automatically start the playlist at the correct position
    log_usage('stop')
    schedule_playlist(token_info)

    # Embed Spotify Player with autoplay
    embed_code = '''
    <iframe src="https://open.spotify.com/embed/playlist/6oQkWFEnlrUwJgT0mhLFrT?autoplay=1" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
    '''
    st.markdown(embed_code, unsafe_allow_html=True)
else:
    auth_url = sp_oauth.get_authorize_url()
    st.write(f'Please go to this URL to authorize: [Authorize]({auth_url})')
