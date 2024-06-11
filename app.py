import streamlit as st
from streamlit.components.v1 import html
import requests
import uuid
import time
import datetime
import streamlit_analytics2 as streamlit_analytics

# Vaše GA4 Measurement ID a API Secret
GA4_MEASUREMENT_ID = "G-ERYGGG3MGS"
GA4_API_SECRET = "kqJ54inxSw2LWiCWDbdmwg"

# Generování unikátního client_id a session_id pro každého uživatele
if 'client_id' not in st.session_state:
    st.session_state['client_id'] = str(uuid.uuid4())
if 'session_id' not in st.session_state:
    st.session_state['session_id'] = str(int(time.time()))

# Google Analytics 4 měřící kód
GA4_SCRIPT = f"""
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_MEASUREMENT_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA4_MEASUREMENT_ID}', {{
    'send_page_view': false,
    'client_id': '{st.session_state['client_id']}'
  }});

  gtag('event', 'page_view', {{
    'page_title': 'Moje aplikace ve Streamlit',
    'page_location': window.location.href,
    'client_id': '{st.session_state['client_id']}',
    'session_id': '{st.session_state['session_id']}'
  }});
</script>
"""

def send_ga4_event(client_id, session_id, event_name, event_params):
    url = f"https://www.google-analytics.com/mp/collect?measurement_id={GA4_MEASUREMENT_ID}&api_secret={GA4_API_SECRET}"
    
    data = {
        "client_id": client_id,
        "events": [{
            "name": event_name,
            "params": {
                **event_params,
                "session_id": session_id
            }
        }]
    }
    
    response = requests.post(url, json=data)
    return response.status_code, response.text

st.title('Moje aplikace ve Streamlit')

st.markdown("Toto je jednoduchá aplikace ve Streamlit s integrovaným sledováním Google Analytics 4.")

# Vložíme GA4 kód do aplikace
html(GA4_SCRIPT, height=0)

# Odeslání page_view události při načtení stránky
try:
    page_view_event = {
        'page_title': 'Moje aplikace ve Streamlit',
        'page_location': 'http://localhost:8501'
    }
    status_code, response_text = send_ga4_event(st.session_state['client_id'], st.session_state['session_id'], 'page_view', page_view_event)
    st.write(f'GA4 Page View Event Status: {status_code}')
    st.write(f'GA4 Page View Response: {response_text}')
except Exception as e:
    st.write(f"Error sending page_view event: {e}")

# Příklad tlačítka, na které přidáme událost sledování
if st.button('Klikněte sem'):
    st.write('Tlačítko bylo kliknuto!')
    
    try:
        # Odeslání události kliknutí do GA4 pomocí Measurement Protocol
        button_click_event = {
            'event_category': 'engagement',
            'event_label': 'Klikněte sem tlačítko'
        }
        status_code, response_text = send_ga4_event(st.session_state['client_id'], st.session_state['session_id'], 'button_click', button_click_event)
        st.write(f'GA4 Button Click Event Status: {status_code}')
        st.write(f'GA4 Button Click Response: {response_text}')
    except Exception as e:
        st.write(f"Error sending button_click event: {e}")
    
    # Odeslání události kliknutí do GA4 pomocí gtag.js
    GA4_CLICK_SCRIPT = f"""
    <script>
      gtag('event', 'button_click', {{
        'event_category': 'engagement',
        'event_label': 'Klikněte sem tlačítko',
        'client_id': '{st.session_state['client_id']}',
        'session_id': '{st.session_state['session_id']}'
      }});
    </script>
    """
    html(GA4_CLICK_SCRIPT, height=0)
    st.experimental_rerun()

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
    
    # Výběr žánru
    genre = st.selectbox('', ('VYBERTE SVŮJ OBLÍBENÝ KANÁL:', 'OTUNES POP', 'OTUNES ROCK', 'OTUNES HIPHOP', 'OTUNES ELECTRO', 'OTUNES COUNTRY'))

    # Slovník ID playlistů
    playlists = {
        'OTUNES POP': "PLatjrwfoBSuyTmoyyTTIXZUU1ZpF5dBBR",
        'OTUNES ROCK': "PLatjrwfoBSuynTvtU_VMg24LnfZ7Q2icD",
        'OTUNES ELECTRO': "PLatjrwfoBSuxp0YTB4n77ApNaq-xJpvYl",
        'OTUNES HIPHOP': "PLatjrwfoBSuwufuOh0Ofi3KnpEwRq8i2i",
        'OTUNES COUNTRY': "PLatjrwfoBSuwbFst7WVhR3XYC1bsw65hx"
    }

    # Získání aktuální hodiny
    current_hour = datetime.datetime.now().hour

    # Určení počátečního indexu videa na základě aktuální hodiny
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

    # Vložení YouTube Music Playeru na základě vybraného žánru
    if genre in playlists:
        playlist_id = playlists[genre]
        video_url = f"https://www.youtube.com/embed?listType=playlist&list={playlist_id}&index={video_index}&autoplay=1"
        video_embed_code = f'''
        <iframe width="100%" height="380" src="{video_url}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        '''

        st.markdown(video_embed_code, unsafe_allow_html=True)

    st.markdown('<p class="center-text">SCHOOL PROJECT AT DAB/VŠE PRAGUE FOR TV ÓČKO</p>', unsafe_allow_html=True)
