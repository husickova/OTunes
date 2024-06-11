import streamlit as st
import streamlit_analytics2 as streamlit_analytics
import datetime
import streamlit.components.v1 as components

# Add the Plausible script using components.html to ensure it's added to the document head
components.html(
    """
    <script defer data-domain="otunes.streamlit.app" src="https://plausible.io/js/script.js"></script>
    """,
    height=0,  # Use height=0 to avoid rendering a large space in the Streamlit app
)

# JavaScript to track goals with debug alert and log
track_event_script = """
<script>
function trackEvent(event_name) {
    alert("Sending event: " + event_name); // Debugging alert
    console.log("Sending event: " + event_name); // Debugging log
    if (window.plausible) {
        window.plausible(event_name);
    }
}
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
        .red-text
