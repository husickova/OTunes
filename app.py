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

    # Dictionary of playlist URLs and their video IDs
    playlists = {
        'OTUNES POP': {"id": "PLatjrwfoBSuxxjxuA4VqoDPhe_bWEGSJ-", "video_ids": ["dQw4w9WgXcQ", "3JZ_D3ELwOQ", "M3mJkSqZbX4"]},  # example video IDs
        'OTUNES ROCK': {"id": "PLatjrwfoBSuxGIzdXo07_4-SAe-ZltkNE", "video_ids": ["s6b33PTbGxk", "3f3K2sEHuIM", "fJ9rUzIMcZQ"]},
        'OTUNES ELECTRO': {"id": "PLatjrwfoBSuz9XAw-X-y5EsF-O62ZrAIf", "video_ids": ["2vjPBrBU-TM", "fJ9rUzIMcZQ", "LsoLEjrDogU"]},
        'OTUNES HIPHOP': {"id": "PLatjrwfoBSuz-zbfooyidyyiwooJWfSG4", "video_ids": ["fPO76Jlnz6c", "3eOuK-pYhy4", "hHUbLv4ThOo"]},
        'OTUNES COUNTRY': {"id": "PLatjrwfoBSuzQjOKCrPtE6Vbo3rdF1TsZ", "video_ids": ["CjxugyZCfuw", "5L6xyaeiV58", "DJ6Ggs8fs8g"]}
    }

    # Function to select random video ID from playlist
    def get_random_video_id(video_ids):
        return random.choice(video_ids)

    # Embed YouTube Music Player based on genre and video ID
    if genre in playlists:
        playlist_id = playlists[genre]["id"]
        video_ids = playlists[genre]["video_ids"]
        random_video_id = get_random_video_id(video_ids)
        playlist_url = f"https://www.youtube.com/embed/{random_video_id}?list={playlist_id}&autoplay=1"
        playlist_embed_code = f'''
        <iframe width="100%" height="380" src="{playlist_url}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        '''

        st.markdown(playlist_embed_code, unsafe_allow_html=True)

    st.markdown('<p class="center-text">SCHOOL PROJECT AT DAB/VŠE PRAGUE FOR TV ÓČKO</p>', unsafe_allow_html=True)
