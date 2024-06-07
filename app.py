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

    # Dictionary of playlist IDs and lengths
    playlists = {
        'OTUNES POP': {
            "id": "PLatjrwfoBSuxxjxuA4VqoDPhe_bWEGSJ-",
            "lengths": [210, 180, 240, 230, 250, 220, 300, 260, 280, 270, 310, 290, 250, 330, 240, 260, 230, 300, 310, 280, 270, 220, 290, 320]
        },
        'OTUNES ROCK': {
            "id": "PLatjrwfoBSuxGIzdXo07_4-SAe-ZltkNE",
            "lengths": [250, 260, 240, 220, 300, 220, 300, 260, 280, 270, 310, 290, 250, 330, 240, 260, 230, 300, 310, 280, 270, 220, 290, 320]
        },
        'OTUNES ELECTRO': {
            "id": "PLatjrwfoBSuz9XAw-X-y5EsF-O62ZrAIf",
            "lengths": [300, 320, 310, 300, 320, 310, 300, 320, 310, 300, 320, 310, 300, 320, 310, 300, 320, 310, 300, 320, 310, 300, 320, 310]
        },
        'OTUNES HIPHOP': {
            "id": "PLatjrwfoBSuzzSWGNLKpYmKu7F_vm-VOF&si=-MNML2mnfrmftrc2",
            "lengths": [260, 270, 280, 300, 320, 310, 300, 320, 310, 300, 320, 310, 300, 320, 310, 300, 320, 310, 300, 320, 310, 300, 320, 310]
        },
        'OTUNES COUNTRY': {
            "id": "PLatjrwfoBSuzQjOKCrPtE6Vbo3rdF1TsZ",
            "lengths": [240, 230, 220, 300, 320, 310, 300, 320, 310, 300, 320, 310, 300, 320, 310, 300, 320, 310, 300, 320, 310, 300, 320, 310]
        }
    }

    # Get current hour
    current_hour = datetime.datetime.now().hour
    video_index = current_hour * 10  # Calculate the video index based on the hour

    # Ensure video index is within bounds
    if video_index >= len(playlists[genre]['lengths']):
        video_index = len(playlists[genre]['lengths']) - 1

    # Embed YouTube Music Player based on genre and current hour
    if genre in playlists:
        playlist_id = playlists[genre]["id"]
        video_url = f"https://www.youtube.com/embed?listType=playlist&list={playlist_id}&index={video_index}"

        st.markdown(f"Current hour: {current_hour}")
        st.markdown(f"Playing video index: {video_index}")
        st.markdown(f"Video URL: {video_url}")

        st_player(video_url)

    st.markdown('<p class="center-text">SCHOOL PROJECT AT DAB/VŠE PRAGUE FOR TV ÓČKO</p>', unsafe_allow_html=True)
