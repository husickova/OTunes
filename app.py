import streamlit as st
import streamlit_analytics2 as streamlit_analytics
import datetime
from bs4 import BeautifulSoup
import pathlib
import shutil

# Google Analytics Injection
GA_ID = "google_analytics"
GA_SCRIPT = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-16H3MEHP7P"></script>
<script id='google_analytics'>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-16H3MEHP7P');
</script>
"""

def inject_ga():
    index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
    soup = BeautifulSoup(index_path.read_text(), features="html.parser")
    if not soup.find(id=GA_ID):
        bck_index = index_path.with_suffix('.bck')
        if bck_index.exists():
            shutil.copy(bck_index, index_path)
        else:
            shutil.copy(index_path, bck_index)
        html = str(soup)
        new_html = html.replace('<head>', '<head>\n' + GA_SCRIPT)
        index_path.write_text(new_html)

inject_ga()

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

    # Dictionary of playlist IDs
    playlists = {
        'OTUNES POP': "PLatjrwfoBSuyTmoyyTTIXZUU1ZpF5dBBR",
        'OTUNES ROCK': "PLatjrwfoBSuynTvtU_VMg24LnfZ7Q2icD",
        'OTUNES ELECTRO': "PLatjrwfoBSuxp0YTB4n77ApNaq-xJpvYl",
        'OTUNES HIPHOP': "PLatjrwfoBSuwufuOh0Ofi3KnpEwRq8i2i",
        'OTUNES COUNTRY': "PLatjrwfoBSuwbFst7WVhR3XYC1bsw65hx"
    }

    # Get current hour
    current_hour = datetime.datetime.now().hour

    # Determine the starting video index based on the current hour
    if 0 <= current_hour < 3:
        video_index = 0
    elif 3 <= current_hour < 5:
        video_index = 29
    elif 5 <= current_hour < 7:
        video_index = 49
    elif 7 <= current_hour < 9:
        video_index = 69
    elif 9 <= current_hour < 11:
        video_index = 89
    elif 11 <= current_hour < 13:
        video_index = 99
    elif 13 <= current_hour < 15:
        video_index = 109
    elif 15 <= current_hour < 17:
        video_index = 119
    elif 17 <= current_hour < 19:
        video_index = 139
    elif 19 <= current_hour < 21:
        video_index = 149
    elif 21 <= current_hour < 23:
        video_index = 159
    elif 23 <= current_hour < 24:
        video_index = 169
    else:
        video_index = 0

    # Embed YouTube Music Player based on selected genre
    if genre in playlists:
        playlist_id = playlists[genre]
        video_url = f"https://www.youtube.com/embed?listType=playlist&list={playlist_id}&index={video_index}&autoplay=1"
        video_embed_code = f'''
        <iframe width="100%" height="380" src="{video_url}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        '''

        st.markdown(video_embed_code, unsafe_allow_html=True)

    st.markdown('<p class="center-text">SCHOOL PROJECT AT DAB/VŠE PRAGUE FOR TV ÓČKO</p>', unsafe_allow_html=True)
