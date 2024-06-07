import streamlit as st
import streamlit_analytics2 as streamlit_analytics
import datetime
from streamlit_player import st_player

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
        'OTUNES POP': [
            {"id": "dQw4w9WgXcQ", "title": "Rick Astley - Never Gonna Give You Up"},
            {"id": "3JZ_D3ELwOQ", "title": "Michael Jackson - Beat It"},
            {"id": "M3mJkSqZbX4", "title": "Bon Jovi - Livin' on a Prayer"}
        ],
        'OTUNES ROCK': [
            {"id": "s6b33PTbGxk", "title": "Queen - We Will Rock You"},
            {"id": "3f3K2sEHuIM", "title": "AC/DC - Thunderstruck"},
            {"id": "fJ9rUzIMcZQ", "title": "Queen - Bohemian Rhapsody"}
        ],
        'OTUNES ELECTRO': [
            {"id": "2vjPBrBU-TM", "title": "Avicii - Wake Me Up"},
            {"id": "fJ9rUzIMcZQ", "title": "Daft Punk - One More Time"},
            {"id": "LsoLEjrDogU", "title": "Calvin Harris - Summer"}
        ],
        'OTUNES HIPHOP': [
            {"id": "fPO76Jlnz6c", "title": "Tupac - California Love"},
            {"id": "3eOuK-pYhy4", "title": "Dr. Dre - Still D.R.E."},
            {"id": "hHUbLv4ThOo", "title": "Snoop Dogg - Drop It Like It's Hot"}
        ],
        'OTUNES COUNTRY': [
            {"id": "CjxugyZCfuw", "title": "Billy Ray Cyrus - Achy Breaky Heart"},
            {"id": "5L6xyaeiV58", "title": "Dolly Parton - Jolene"},
            {"id": "DJ6Ggs8fs8g", "title": "Johnny Cash - Ring of Fire"}
        ]
    }

    # Get current hour
    current_hour = datetime.datetime.now().hour

    # Embed YouTube Music Player based on genre and current hour
    if genre in playlists:
        playlist = playlists[genre]
        video_index = current_hour % len(playlist)  # Ensure the index is within the playlist range
        selected_video = playlist[video_index]
        video_url = f"https://www.youtube.com/watch?v={selected_video['id']}"

        st.markdown(f"Current hour: {current_hour}")
        st.markdown(f"Playing video index: {video_index}")
        st.markdown(f"Playing video: {selected_video['title']}")
        st.markdown(f"Video URL: {video_url}")

        st_player(video_url)

    st.markdown('<p class="center-text">SCHOOL PROJECT AT DAB/VŠE PRAGUE FOR TV ÓČKO</p>', unsafe_allow_html=True)
