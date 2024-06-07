import streamlit as st
import streamlit_analytics2 as streamlit_analytics
import datetime

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

    # Dictionary of playlist video URLs
    playlists = {
        'OTUNES POP': [
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "https://www.youtube.com/watch?v=3JZ_D3ELwOQ",
            "https://www.youtube.com/watch?v=M3mJkSqZbX4"
        ],
        'OTUNES ROCK': [
            "https://www.youtube.com/watch?v=s6b33PTbGxk",
            "https://www.youtube.com/watch?v=3f3K2sEHuIM",
            "https://www.youtube.com/watch?v=fJ9rUzIMcZQ"
        ],
        'OTUNES ELECTRO': [
            "https://www.youtube.com/watch?v=2vjPBrBU-TM",
            "https://www.youtube.com/watch?v=fJ9rUzIMcZQ",
            "https://www.youtube.com/watch?v=LsoLEjrDogU"
        ],
        'OTUNES HIPHOP': [
            "https://www.youtube.com/watch?v=fPO76Jlnz6c",
            "https://www.youtube.com/watch?v=3eOuK-pYhy4",
            "https://www.youtube.com/watch?v=hHUbLv4ThOo"
        ],
        'OTUNES COUNTRY': [
            "https://www.youtube.com/watch?v=CjxugyZCfuw",
            "https://www.youtube.com/watch?v=5L6xyaeiV58",
            "https://www.youtube.com/watch?v=DJ6Ggs8fs8g"
        ]
    }

    # Get current hour
    current_hour = datetime.datetime.now().hour
    video_index = (current_hour % 10) * 10  # Calculate the video index based on the hour

    # Ensure video index is within bounds
    if video_index >= len(playlists[genre]):
        video_index = len(playlists[genre]) - 1

    # Embed YouTube Music Player based on genre and current hour
    if genre in playlists:
        video_url = playlists[genre][video_index // 10]

        st.markdown(f"Current hour: {current_hour}")
        st.markdown(f"Playing video index: {video_index}")
        st.markdown(f"Video URL: {video_url}")

        st.video(video_url, start_time=0, autoplay=True)

    st.markdown('<p class="center-text">SCHOOL PROJECT AT DAB/VŠE PRAGUE FOR TV ÓČKO</p>', unsafe_allow_html=True)
