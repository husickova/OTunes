import streamlit as st
import streamlit_analytics
import random

# Initialize streamlit-analytics
with streamlit_analytics.track():
    # CSS styles to center the text and customize font
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&display=swap');

        .center-text {
            text-align: center;
            font-family: 'Open Sans', sans-serif; /* Customize font family */
            font-size: 16px; /* Customize font size */
            text-transform: uppercase; /* Transform text to uppercase */
        }
        .title-text {
            text-align: center;
            font-family: 'Open Sans', sans-serif; /* Customize font family */
            font-size: 48px; /* Customize font size for title */
            font-weight: 700; /* Bold font weight */
            text-transform: uppercase; /* Transform text to uppercase */
            margin-top: -50px; /* Reduce top margin */
        }
        .subtitle-text {
            text-align: center;
            font-family: 'Open Sans', sans-serif; /* Customize font family */
            font-size: 28px; /* Customize font size for subtitle */
            text-transform: uppercase; /* Transform text to uppercase */
        }
        .red-text {
            color: red; /* Red color for "O" */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Streamlit interface
    st.markdown('<h1 class="title-text"><span class="red-text">O</span>TUNES</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="subtitle-text">NEVERENDING MUSIC CHANNELS FULL OF MUSIC YOU LOVE</h2>', unsafe_allow_html=True)
    
    # Selection for genres 
    genre = st.selectbox('', ('CHOOSE YOUR FAVORITE CHANNEL:', 'OTUNES POP', 'OTUNES ROCK', 'OTUNES HIPHOP', 'OTUNES ELECTRO', 'OTUNES COUNTRY'))

    # Dictionary of playlist URLs, their lengths in seconds, and song lengths
    playlists = {
        'OTUNES POP': {"id": "PLatjrwfoBSuxxjxuA4VqoDPhe_bWEGSJ-", "lengths": [210, 180, 240, 200, 220, 230, 250, 210, 200]},  # example lengths in seconds
        'OTUNES ROCK': {"id": "PLatjrwfoBSuxGIzdXo07_4-SAe-ZltkNE", "lengths": [250, 260, 240, 230, 220, 210, 260, 240, 230]},
        'OTUNES ELECTRO': {"id": "PLatjrwfoBSuz9XAw-X-y5EsF-O62ZrAIf", "lengths": [300, 320, 310, 290, 310, 300, 330, 310, 320]},
        'OTUNES HIPHOP': {"id": "PLatjrwfoBSuz-zbfooyidyyiwooJWfSG4", "lengths": [260, 270, 280, 250, 260, 270, 280, 290, 300]},
        'OTUNES COUNTRY': {"id": "PLatjrwfoBSuzQjOKCrPtE6Vbo3rdF1TsZ", "lengths": [240, 230, 220, 210, 200, 190, 180, 170, 160]}
    }

    # Function to calculate random song offset
    def calculate_random_song_offset(song_lengths):
        song_index = random.randint(0, len(song_lengths) - 1)
        time_offset = sum(song_lengths[:song_index])
        return time_offset

    # Embed YouTube Music Player based on genre and offset
    if genre in playlists:
        playlist_id = playlists[genre]["id"]
        song_lengths = playlists[genre]["lengths"]
        time_offset = calculate_random_song_offset(song_lengths)
        playlist_url = f"https://www.youtube.com/embed/videoseries?list={playlist_id}&start={time_offset}&autoplay=1"
        playlist_embed_code = f'''
        <iframe width="100%" height="380" src="{playlist_url}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        '''

        st.markdown(playlist_embed_code, unsafe_allow_html=True)

    st.markdown('<p class="center-text">SCHOOL PROJECT AT DAB/VŠE PRAGUE FOR TV ÓČKO</p>', unsafe_allow_html=True)
