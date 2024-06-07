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

    # Dictionary of playlist video URLs and lengths in seconds
    playlists = {
        'OTUNES POP': {
            "id": "PLatjrwfoBSuxxjxuA4VqoDPhe_bWEGSJ-",
            "videos": [
                {"id": "dQw4w9WgXcQ", "length": 210},
                {"id": "3JZ_D3ELwOQ", "length": 180},
                {"id": "M3mJkSqZbX4", "length": 240}
            ]
        },
        'OTUNES ROCK': {
            "id": "PLatjrwfoBSuxGIzdXo07_4-SAe-ZltkNE",
            "videos": [
                {"id": "s6b33PTbGxk", "length": 250},
                {"id": "3f3K2sEHuIM", "length": 260},
                {"id": "fJ9rUzIMcZQ", "length": 240}
            ]
        },
        'OTUNES ELECTRO': {
            "id": "PLatjrwfoBSuz9XAw-X-y5EsF-O62ZrAIf",
            "videos": [
                {"id": "2vjPBrBU-TM", "length": 300},
                {"id": "fJ9rUzIMcZQ", "length": 320},
                {"id": "LsoLEjrDogU", "length": 310}
            ]
        },
        'OTUNES HIPHOP': {
            "id": "PLatjrwfoBSuzzSWGNLKpYmKu7F_vm-VOF&si=-MNML2mnfrmftrc2",
            "videos": [
                {"id": "fPO76Jlnz6c", "length": 260},
                {"id": "3eOuK-pYhy4", "length": 270},
                {"id": "hHUbLv4ThOo", "length": 280}
            ]
        },
        'OTUNES COUNTRY': {
            "id": "PLatjrwfoBSuzQjOKCrPtE6Vbo3rdF1TsZ",
            "videos": [
                {"id": "CjxugyZCfuw", "length": 240},
                {"id": "5L6xyaeiV58", "length": 230},
                {"id": "DJ6Ggs8fs8g", "length": 220}
            ]
        }
    }

    # Function to calculate random video and offset
    def calculate_random_video_and_offset(videos):
        total_length = sum(video["length"] for video in videos)
        random_offset = random.randint(0, total_length - 1)
        cumulative_length = 0

        for video in videos:
            cumulative_length += video["length"]
            if cumulative_length > random_offset:
                start_time = random_offset - (cumulative_length - video["length"])
                return video["id"], start_time

    # Embed YouTube Music Player based on genre and offset
    if genre in playlists:
        playlist = playlists[genre]
        video_id, start_time = calculate_random_video_and_offset(playlist["videos"])
        video_url = f"https://www.youtube.com/embed/{video_id}?start={start_time}&autoplay=1&list={playlist['id']}"
        video_embed_code = f'''
        <iframe width="100%" height="380" src="{video_url}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        '''

        st.markdown(video_embed_code, unsafe_allow_html=True)

    st.markdown('<p class="center-text">SCHOOL PROJECT AT DAB/VŠE PRAGUE FOR TV ÓČKO</p>', unsafe_allow_html=True)
