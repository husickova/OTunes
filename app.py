import streamlit as st
import streamlit_analytics
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
            font-size: 18px; /* Customize font size */
        }
        .title-text {
            text-align: center;
            font-family: 'Open Sans', sans-serif; /* Customize font family */
            font-size: 36px; /* Customize font size for title */
            font-weight: 700; /* Bold font weight */
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
    st.markdown('<h3 class="center-text">Neverending music channels full of music you love.</h3>', unsafe_allow_html=True)
    st.markdown('<p class="center-text">Choose your favorite channel:</p>', unsafe_allow_html=True)
    
    # Selection for genres 
    genre = st.selectbox('', ('Choose', 'OTunes POP', 'OTunes ROCK', 'OTunes HIPHOP', 'OTunes ELECTRO', 'OTunes COUNTRY'))

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
        playlist_url = f"https://www.youtube.com/embed/videoseries?list={playlists[genre]}&start={time_offset}&autoplay=1"
        playlist_embed_code = f'''
        <iframe width="100%" height="380" src="{playlist_url}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        '''

        st.markdown(playlist_embed_code, unsafe_allow_html=True)

    st.markdown('<p class="center-text">School project at DAB/VŠE Prague for TV Óčko.</p>', unsafe_allow_html=True)
