import streamlit as st
import streamlit_analytics2 as streamlit_analytics
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
        'OTUNES POP': "PLatjrwfoBSuxxjxuA4VqoDPhe_bWEGSJ-",
        'OTUNES ROCK': "PLatjrwfoBSuxGIzdXo07_4-SAe-ZltkNE",
        'OTUNES ELECTRO': "PLatjrwfoBSuz9XAw-X-y5EsF-O62ZrAIf",
        'OTUNES HIPHOP': "PLatjrwfoBSuzzSWGNLKpYmKu7F_vm-VOF&si=-MNML2mnfrmftrc2",
        'OTUNES COUNTRY': "PLatjrwfoBSuzQjOKCrPtE6Vbo3rdF1TsZ"
    }

    # User input for video index
    video_index = st.number_input('Enter the index of the video to play:', min_value=0, value=0)

    # Embed YouTube Music Player based on genre and user input index
    if genre in playlists:
        playlist_id = playlists[genre]
        video_url = f"https://www.youtube.com/embed?listType=playlist&list={playlist_id}&index={video_index}"

        st.markdown(f"Playing video index: {video_index}")
        st.markdown(f"Video URL: {video_url}")

        st_player(video_url)

    st.markdown('<p class="center-text">SCHOOL PROJECT AT DAB/VŠE PRAGUE FOR TV ÓČKO</p>', unsafe_allow_html=True)
