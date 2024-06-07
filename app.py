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

    # Dictionary of playlist video URLs and lengths in seconds
    playlists = {
        'OTUNES POP': {
            "id": "PLatjrwfoBSuxxjxuA4VqoDPhe_bWEGSJ-",
            "videos": [
                {"id": "9U4-PgbN7eM", "length": 0}  # Length set to 0 because it's not used
            ]
        },
        'OTUNES ROCK': {
            "id": "PLatjrwfoBSuxGIzdXo07_4-SAe-ZltkNE",
            "videos": [
                {"id": "s6b33PTbGxk", "length": 250},
                {"id": "3f3K2sEHuIM", "length": 260},
                {"id": "fJ9rUzIMcZQ", "length": 240},
                {"id": "LsoLEjrDogU", "length": 220},
                {"id": "2vjPBrBU-TM", "length": 300},
                {"id": "hQ5EWg2-9JI", "length": 220},
                {"id": "gdZLi9oWNZg", "length": 300},
                {"id": "OpQFFLBMEPI", "length": 260},
                {"id": "yRFEKj3Q9YY", "length": 280},
                {"id": "u6jyAGIIf6k", "length": 270},
                {"id": "5-sfG8BV8wU", "length": 310},
                {"id": "6Q5vRoPlQ0k", "length": 290},
                {"id": "2vMH8lITTCE", "length": 250},
                {"id": "3J6o_WSkgtI", "length": 330},
                {"id": "1P17ct4e5OE", "length": 240},
                {"id": "UceaB4D0jpo", "length": 260},
                {"id": "CevxZvSJLk8", "length": 230},
                {"id": "wXhTHyIgQ_U", "length": 300},
                {"id": "KlyXNRrsk4A", "length": 310},
                {"id": "uJ_1HMAGb4k", "length": 280},
                {"id": "IUhlwOzdYKU", "length": 270},
                {"id": "sCbbMZ-q4-I", "length": 220},
                {"id": "COjCx3SHDEo", "length": 290},
                {"id": "yYcyacLRPNs", "length": 320}
            ]
        },
        'OTUNES ELECTRO': {
            "id": "PLatjrwfoBSuz9XAw-X-y5EsF-O62ZrAIf",
            "videos": [
                {"id": "2vjPBrBU-TM", "length": 300},
                {"id": "fJ9rUzIMcZQ", "length": 320},
                {"id": "LsoLEjrDogU", "length": 310},
                {"id": "2vjPBrBU-TM", "length": 300},
                {"id": "fJ9rUzIMcZQ", "length": 320},
                {"id": "LsoLEjrDogU", "length": 310},
                {"id": "2vjPBrBU-TM", "length": 300},
                {"id": "fJ9rUzIMcZQ", "length": 320},
                {"id": "LsoLEjrDogU", "length": 310},
                {"id": "2vjPBrBU-TM", "length": 300},
                {"id": "fJ9rUzIMcZQ", "length": 320},
                {"id": "LsoLEjrDogU", "length": 310},
                {"id": "2vjPBrBU-TM", "length": 300},
                {"id": "fJ9rUzIMcZQ", "length": 320},
                {"id": "LsoLEjrDogU", "length": 310},
                {"id": "2vjPBrBU-TM", "length": 300},
                {"id": "fJ9rUzIMcZQ", "length": 320},
                {"id": "LsoLEjrDogU", "length": 310},
                {"id": "2vjPBrBU-TM", "length": 300},
                {"id": "fJ9rUzIMcZQ", "length": 320},
                {"id": "LsoLEjrDogU", "length": 310},
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
                {"id": "hHUbLv4ThOo", "length": 280},
                {"id": "2vjPBrBU-TM", "length": 300},
                {"id": "fJ9rUzIMcZQ", "length": 320},
                {"id": "LsoLEjrDogU", "length": 310},
                {"id": "2vjPBrBU-TM", "length": 300},
                {"id": "fJ9rUzIMcZQ", "length": 320},
                {"id": "LsoLEjrDogU", "length": 310},
                {"id": "2vjPBrBU-TM", "length": 300},
                {"id": "fJ9rUzIMcZQ", "length": 320},
                {"id": "LsoLEjrDogU", "length": 310},
                {"id": "2vjPBrBU-TM", "length": 300},
                {"id": "fJ9rUzIMcZQ", "length": 320},
                {"id": "LsoLEjrDogU", "length": 310},
                {"id": "2vjPBrBU-TM", "length": 300},
                {"id": "fJ9rUzIMcZQ", "length": 320},
                {"id": "LsoLEjrDogU", "length": 310},
                {"id": "2vjPBrBU-TM", "length": 300},
                {"id": "fJ9rUzIMcZQ", "length": 320},
                {"id": "LsoLEjrDogU", "length": 310},
                {"id": "2vjPBrBU-TM", "length": 300},
                {"id": "fJ9rUzIMcZQ", "length": 320},
                {"id": "LsoLEjrDogU", "length": 310}
            ]
        },
        'OTUNES COUNTRY': {
            "id": "PLatjrwfoBSuzQjOKCrPtE6Vbo3rdF1TsZ",
            "videos": [
                {"id": "CjxugyZCfuw", "length": 240},
                {"id": "5L6xyaeiV58", "length": 230},
                {"id": "DJ6Ggs8fs8g", "length": 220},
                {"id": "2vjPBrBU-TM", "length": 300},
                {"id": "fJ9rUzIMcZQ", "length": 320},
                {"id": "LsoLEjrDogU", "length": 310},
                {"id": "2vjPBrBU-TM", "length": 300},
                {"id": "fJ9rUzIMcZQ", "length": 320},
                {"id": "LsoLEjrDogU", "length": 310},
                {"id": "2vjPBrBU-TM", "length": 300},
                {"id": "fJ9rUzIMcZQ", "length": 320},
                {"id": "LsoLEjrDogU", "length": 310},
                {"id": "2vjPBrBU-TM", "length": 300},
                {"id": "fJ9rUzIMcZQ", "length": 320},
                {"id": "LsoLEjrDogU", "length": 310},
                {"id": "2vjPBrBU-TM", "length": 300},
                {"id": "fJ9rUzIMcZQ", "length": 320},
                {"id": "LsoLEjrDogU", "length": 310},
                {"id": "2vjPBrBU-TM", "length": 300},
                {"id": "fJ9rUzIMcZQ", "length": 320},
                {"id": "LsoLEjrDogU", "length": 310},
                {"id": "2vjPBrBU-TM", "length": 300},
                {"id": "fJ9rUzIMcZQ", "length": 320},
                {"id": "LsoLEjrDogU", "length": 310}
            ]
        }
    }

    # Get current hour
    current_hour = datetime.datetime.now().hour

    # Embed YouTube Music Player based on selected genre
    if genre in playlists:
        playlist = playlists[genre]
        video_index = 0
        if genre == 'OTUNES POP' and 12 <= current_hour < 24:
            video_index = 99  # Start from the 100th video if current time is between 12:00 and 24:00
        video_id = playlist["videos"][video_index]["id"]
        video_url = f"https://www.youtube.com/embed/{video_id}?autoplay=1&list={playlist['id']}"
        video_embed_code = f'''
        <iframe width="100%" height="380" src="{video_url}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        '''

        st.markdown(video_embed_code, unsafe_allow_html=True)

    st.markdown('<p class="center-text">SCHOOL PROJECT AT DAB/VŠE PRAGUE FOR TV ÓČKO</p>', unsafe_allow_html=True)
