import streamlit as st
import datetime

# CSS styles to center the text and logo
st.markdown(
    """
    <style>
    .center-text {
        text-align: center;
    }
    .center-image {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 60%; /* Increase size by 50% */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# URL of the logo image
logo_url = "https://github.com/husickova/OTunes/blob/main/images/logo.png?raw=true"

# Streamlit interface
st.markdown(f'<img src="{logo_url}" class="center-image" alt="OTunes Logo">', unsafe_allow_html=True)
st.markdown('<h2 class="center-text">Neverending music channels full of music you love.</h2>', unsafe_allow_html=True)
st.markdown('<p class="center-text">Choose your favorite channel:</p>', unsafe_allow_html=True)

# Selection for genres
genre = st.selectbox('Channels:', ('Choose', 'OTunes POP', 'OTunes ROCK', 'OTunes HIPHOP', 'OTunes ELECTRO', 'OTunes COUNTRY'))

# Function to calculate time offset
def calculate_time_offset():
    now = datetime.datetime.now()
    seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
    return int(seconds_since_midnight)

# Calculate offset
time_offset = calculate_time_offset()

# Dictionary of playlist URLs
playlists = {
    'OTunes POP': "PLatjrwfoBSuxxjxuA4VqoDPhe_bWEGSJ-",
    'OTunes ROCK': "PLatjrwfoBSuxGIzdXo07_4-SAe-ZltkNE",
    'OTunes ELECTRO': "PLatjrwfoBSuz9XAw-X-y5EsF-O62ZrAIf",
    'OTunes HIPHOP': "PLatjrwfoBSuz-zbfooyidyyiwooJWfSG4",
    'OTunes COUNTRY': "PLatjrwfoBSuzQjOKCrPtE6Vbo3rdF1TsZ"
}

# Embed YouTube Music Player based on genre and offset
if genre in playlists:
    playlist_url = f"https://www.youtube.com/embed?listType=playlist&list={playlists[genre]}&start={time_offset}&autoplay=1"
    playlist_embed_code = f'''
    <iframe width="100%" height="380" src="{playlist_url}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    '''

    st.markdown(playlist_embed_code, unsafe_allow_html=True)
