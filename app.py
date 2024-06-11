import streamlit as st
import streamlit_analytics2 as streamlit_analytics
import datetime
import streamlit.components.v1 as components

# Set the page configuration
st.set_page_config(page_title="OTUNES", page_icon="🎵", layout="centered")

# Add the Plausible script using components.html to ensure it's added to the document head
components.html(
    """
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        var plausibleScript = document.createElement('script');
        plausibleScript.defer = true;
        plausibleScript.setAttribute('data-domain', 'otunes.streamlit.app');
        plausibleScript.src = 'https://plausible.io/js/script.js';
        plausibleScript.onload = function() {
            console.log('Plausible script loaded successfully');
        };
        plausibleScript.onerror = function() {
            console.error('Error loading Plausible script');
            alert('Plausible script failed to load. Please check your network settings.');
        };
        document.head.appendChild(plausibleScript);
    });
    </script>
    """,
    height=0,  # Use height=0 to avoid rendering a large space in the Streamlit app
)

# JavaScript to track goals with enhanced debugging
track_event_script = """
<script>
function trackEvent(event_name) {
    alert("Sending event: " + event_name); // Debugging alert
    console.log("Sending event: " + event_name); // Debugging log
    if (window.plausible) {
        window.plausible(event_name, {props: {source: 'streamlit'}});
        console.log("Event sent: " + event_name);
    } else {
        console.error("Plausible not loaded");
    }
}

// Function to add Plausible event tracking to the select box
function addPlausibleTracking() {
    const selectBox = document.querySelector('select');
    if (selectBox) {
        selectBox.setAttribute('plausible-event-name', 'Genre+Selection');
        selectBox.addEventListener('change', function() {
            const selectedOption = selectBox.options[selectBox.selectedIndex].text;
            const eventNameMap = {
                'OTUNES POP': 'OTUNES_POP',
                'OTUNES ROCK': 'OTUNES_ROCK',
                'OTUNES HIPHOP': 'OTUNES_HIPHOP',
                'OTUNES ELECTRO': 'OTUNES_ELECTRO',
                'OTUNES COUNTRY': 'OTUNES_COUNTRY'
            };
            const eventName = eventNameMap[selectedOption];
            if (eventName) {
                trackEvent(eventName);
            } else {
                console.error("Event name mapping not found for: " + selectedOption);
            }
        });
        console.log('Plausible tracking added to select box');
    } else {
        console.error('Select box not found');
    }
}

// Wait for the DOM to load before adding the tracking
document.addEventListener('DOMContentLoaded', addPlausibleTracking);
</script>
"""

st.markdown(track_event_script, unsafe_allow_html=True)

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
    genre = st.selectbox('Select a Genre:', ('CHOOSE YOUR FAVORITE CHANNEL:', 'OTUNES POP', 'OTUNES ROCK', 'OTUNES HIPHOP', 'OTUNES ELECTRO', 'OTUNES COUNTRY'))

    # Dictionary of playlist IDs
    playlists = {
        'OTUNES POP': "PLatjrwfoBSuyTmoyyTTIXZUU1ZpF5dBBR",
        'OTUNES ROCK': "PLatjrwfoBSuynTvtU_VMg24Lnf
