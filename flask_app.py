from flask import Flask, request, redirect
import spotipy
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)

CLIENT_ID = '0c03bcd06c194e39887207a52ff3d4c1'
CLIENT_SECRET = 'aa2524cc05f3481badc50458d8aeab5b'
REDIRECT_URI = 'https://otunesgit-dcrrmv3ymryxl9haxuvoq3.streamlit.app/callback'

sp_oauth = SpotifyOAuth(client_id=CLIENT_ID,
                        client_secret=CLIENT_SECRET,
                        redirect_uri=REDIRECT_URI,
                        scope='user-modify-playback-state user-read-playback-state')

@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    return redirect(f'/token?access_token={token_info["access_token"]}')

if __name__ == '__main__':
    app.run(port=8888)
