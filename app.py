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

    # Dictionary of playlist URLs and their lengths in seconds
    playlists = {
        'OTUNES POP': {"id": "PLatjrwfoBSuxxjxuA4VqoDPhe_bWEGSJ-", "length": 3600},  # example length in seconds
        'OTUNES ROCK': {"id": "PLatjrwfoBSuxGIzdXo07_4-SAe-ZltkNE", "length": 5400},
        'OTUNES ELECTRO': {"id": "PLatjrwfoBSuz9XAw-X-y5EsF-O62ZrAIf", "length": 7200},
        'OTUNES HIPHOP': {"id": "PLatjrwfoBSuz-zbfooyidyyiwooJWfSG4", "length": 4800},
        'OTUNES COUNTRY': {"id": "PLatjrwfoBSuzQjOKCrPtE6Vbo3rdF1TsZ", "length": 6000}
    }

    # Function to calculate time offset
    def calculate_time_offset(playlist_length):
        now = datetime.datetime.now()
        seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
        loop_offset = int(seconds_since_midnight) % playlist_length
        return loop_offset

    # Embed YouTube Music Player based on genre and offset
    if genre in playlists:
        playlist_id = playlists[genre]["id"]
        playlist_length = playlists[genre]["length"]
        time_offset = calculate_time_offset(playlist_length)
        
        # Generate YouTube embed code with a script to control playback
        playlist_embed_code = f'''
        <iframe id="ytplayer" type="text/html" width="100%" height="380"
        src="https://www.youtube.com/embed/videoseries?list={playlist_id}&start={time_offset}&autoplay=1"
        frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        
        <script>
        function onYouTubeIframeAPIReady() {{
            var player = new YT.Player('ytplayer', {{
                events: {{
                    'onReady': function(event) {{
                        event.target.seekTo({time_offset}, true);
                    }}
                }}
            }});
        }}

        var tag = document.createElement('script');
        tag.src = "https://www.youtube.com/iframe_api";
        var firstScriptTag = document.getElementsByTagName('script')[0];
        firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
        </script>
        '''

        st.markdown(playlist_embed_code, unsafe_allow_html=True)

    st.markdown('<p class="center-text">SCHOOL PROJECT AT DAB/VŠE PRAGUE FOR TV ÓČKO</p>', unsafe_allow_html=True)
