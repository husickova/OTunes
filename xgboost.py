# ===== BLOCK: main =====

# ===== CODE: imports =====

import pandas as pd
import numpy as np
import requests
import base64
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBRegressor
from datetime import datetime, timedelta

# ===== CODE: Load&Preprocess =====

import pandas as pd
import numpy as np
import requests
import base64
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBRegressor
from datetime import datetime, timedelta

# Load the dataset
df = pd.read_csv('in/tables/final_combined_output.csv')

# Preprocess data
df.dropna(inplace=True)  # Handling missing values

# Convert 'day_of_week' to numerical values
label_encoder = LabelEncoder()
df['day_of_week'] = label_encoder.fit_transform(df['day_of_week'])

# Define features and target
features = df[['danceability', 'energy', 'key', 'loudness', 'speechiness', 'acousticness',
               'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature',
               'day_of_week', 'is_holiday', 'temperature_2m_mean', 'rain_sum', 'snowfall_sum',
               'wind_speed_10m_max']]
target = df['popularity']

# Ensure all feature columns are of type float
features = features.astype(float)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Train XGBoost model
model = XGBRegressor()
model.fit(X_train, y_train)

# Predict popularity
df['predicted_popularity'] = model.predict(features)

# Define genres and ordering rule
genres = ['Pop', 'Hip-Hop', 'Country', 'Rock', 'Electronic']
ordering_rule = [1.0, 1.0, 2.0, 2.0, 2.0, 2.0, 1.0, 1.0, 1.0, 2.0]

def generate_playlist(df, genre, ordering_rule, date, current_track_ids, previous_track_ids):
    genre_df = df[df['genre'] == genre].sort_values(by='predicted_popularity', ascending=False)
    genre_df = genre_df[~genre_df['track_id'].isin(current_track_ids)]
    
    # Create a list of tracks that are not in the previous day's playlist
    new_tracks = genre_df[~genre_df['track_id'].isin(previous_track_ids)]
    
    # Determine the number of new songs to add
    num_new_songs = np.random.randint(10, 21)
    num_old_songs = 100 - num_new_songs
    
    # Get the new tracks and the old tracks from the previous playlist
    new_tracks = new_tracks.head(num_new_songs)
    old_tracks = df[df['track_id'].isin(previous_track_ids)].head(num_old_songs)
    
    # Combine the new tracks and old tracks
    combined_tracks = pd.concat([new_tracks, old_tracks]).sort_values(by='predicted_popularity', ascending=False)
    
    # Ensure no duplicates and no consecutive songs are from the same artist
    playlist = []
    added_tracks = set()
    added_artists = set()

    for _, track in combined_tracks.iterrows():
        if track['track_id'] not in added_tracks and track['artist_name'] not in added_artists:
            playlist.append(track)
            added_tracks.add(track['track_id'])
            added_artists.add(track['artist_name'])
            if len(added_artists) > 1:
                added_artists.remove(playlist[-2]['artist_name'])  # Allow the artist of the second last track to be added again

    # Fill the playlist to 100 songs if there are duplicates removed
    if len(playlist) < 100:
        remaining_tracks = genre_df[~genre_df['track_id'].isin(added_tracks)]
        for _, track in remaining_tracks.iterrows():
            if track['track_id'] not in added_tracks and track['artist_name'] not in added_artists:
                playlist.append(track)
                added_tracks.add(track['track_id'])
                added_artists.add(track['artist_name'])
                if len(added_artists) > 1:
                    added_artists.remove(playlist[-2]['artist_name'])  # Allow the artist of the second last track to be added again
            if len(playlist) >= 100:
                break

    playlist_df = pd.DataFrame(playlist).head(100)
    playlist_df['position'] = range(1, len(playlist_df) + 1)

    return playlist_df

# Define Spotify API credentials and function to refresh access token
playlist_ids = {
    'Electronic': '6oQkWFEnlrUwJgT0mhLFrT',
    'Rock': '3V2BzWCLA1PCwrDtqGQQuD',
    'Country': '3p42i1uBUrUVS3tyPCNiBr',
    'Pop': '0k6moem5uH1Azl6ljzh0oY',
    'Hip_Hop': '3Bwe7tqWapdwkUaKb6BsmF'
}

access_token = "BQCRi2rffR86N5y8GgCtXALUubTwiTUbjBqMdMuIvARytFSndsB1_x8HOAR2OgkkSKvwZBQc2v95m8J2YFzpisLzAXMh0Ye46NJeKY9dkjjKP8oCSinR_6kvSegdfOtpYqAgiUxqCJkZ7D_NeZ3LS7kYH8QTZqTsMsPDsEaA6fQOwcXQtTLp0lBbHQsTXpR3ohUxxceMnD9fHMDFScFdrUjjKnKdyr5IsfY3eRRrZQ"
refresh_token = "AQCNbGvLhgz4lGUFCcwRKIRipi0YxNQYtxX0LIJ0Eqrj8hj8zQjrkytcNuGXjlKF-3M0KEz9D5J0tHh8CbIic8_dC1rdPLRSxxbAvcrNA5qRDEgFY4tMHjekNhzVDjH4CP8"
client_id = "fe7934b517144f1fa30fa04139380905"
client_secret = "dd4c5d1bd6804acf883481dd5dc97748"

def refresh_access_token(client_id, client_secret, refresh_token):
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {base64.b64encode(f'{client_id}:{client_secret}'.encode()).decode()}"
    }
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }
    
    response = requests.post(url, headers=headers, data=data)
    return response.json().get('access_token')  # Return only the access token

access_token = refresh_access_token(client_id, client_secret, refresh_token)

def get_track_uris(playlist_ids):
    track_uris = {}

    for genre, playlist_id in playlist_ids.items():
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?fields=items(track(uri))"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            uris = [item["track"]["uri"].split(':')[-1] for item in data["items"]]
            track_uris[genre] = uris

    return track_uris

# Get current track URIs
current_track_uris = get_track_uris(playlist_ids)


yesterday = datetime.today()
previous_track_uris = get_track_uris(playlist_ids)

# Generate and save playlists
for genre in genres:
    current_track_ids = current_track_uris.get(genre, [])
    previous_track_ids = previous_track_uris.get(genre, [])
    playlist_df = generate_playlist(df, genre, ordering_rule, datetime.today(), current_track_ids, previous_track_ids)
    playlist_df.to_csv(f'out/tables/playlist_{genre}.csv', index=False, columns=['track_id', 'artist_name', 'track_name', 'genre', 'category', 'predicted_popularity', 'position'])

# ===== CODE: Model_Prep&Model_Training =====

# Define features and target
features = df[['danceability', 'energy', 'key', 'loudness', 'speechiness', 'acousticness',
               'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature',
               'day_of_week', 'is_holiday', 'temperature_2m_mean', 'rain_sum', 'snowfall_sum',
               'wind_speed_10m_max']]
target = df['popularity']

# Ensure all feature columns are of type float
features = features.astype(float)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Train XGBoost model
model = XGBRegressor()
model.fit(X_train, y_train)

# Predict popularity
df['predicted_popularity'] = model.predict(features)

# ===== CODE: Playlist_Generation =====

def generate_playlist(df, genre, ordering_rule, date, current_track_ids, previous_track_ids):
    genre_df = df[df['genre'] == genre].sort_values(by='predicted_popularity', ascending=False)
    genre_df = genre_df[~genre_df['track_id'].isin(current_track_ids)]

    # Create a list of tracks that are not in the previous day's playlist
    new_tracks = genre_df[~genre_df['track_id'].isin(previous_track_ids)]
    
    # Determine the number of new songs to add
    num_new_songs = np.random.randint(10, 21)
    num_old_songs = 100 - num_new_songs
    
    # Get the new tracks and the old tracks from the previous playlist
    new_tracks = new_tracks.head(num_new_songs)
    old_tracks = df[df['track_id'].isin(previous_track_ids)].head(num_old_songs)
    
    # Combine the new tracks and old tracks
    combined_tracks = pd.concat([new_tracks, old_tracks]).sort_values(by='predicted_popularity', ascending=False)
    
    # Ensure no duplicates and no consecutive songs are from the same artist
    playlist = []
    added_tracks = set()
    added_artists = set()

    for _, track in combined_tracks.iterrows():
        if track['track_id'] not in added_tracks and track['artist_name'] not in added_artists:
            playlist.append(track)
            added_tracks.add(track['track_id'])
            added_artists.add(track['artist_name'])
            if len(added_artists) > 1:
                added_artists.remove(playlist[-2]['artist_name'])  # Allow the artist of the second last track to be added again

    # Fill the playlist to 100 songs if there are duplicates removed
    if len(playlist) < 100:
        remaining_tracks = genre_df[~genre_df['track_id'].isin(added_tracks)]
        for _, track in remaining_tracks.iterrows():
            if track['track_id'] not in added_tracks and track['artist_name'] not in added_artists:
                playlist.append(track)
                added_tracks.add(track['track_id'])
                added_artists.add(track['artist_name'])
                if len(added_artists) > 1:
                    added_artists.remove(playlist[-2]['artist_name'])  # Allow the artist of the second last track to be added again
            if len(playlist) >= 100:
                break

    playlist_df = pd.DataFrame(playlist).head(100)
    playlist_df['position'] = range(1, len(playlist_df) + 1)

    return playlist_df

# ===== CODE: SpotifyAPI&Check_Playlists =====

def refresh_access_token(client_id, client_secret, refresh_token):
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {base64.b64encode(f'{client_id}:{client_secret}'.encode()).decode()}"
    }
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }
    
    response = requests.post(url, headers=headers, data=data)
    return response.json().get('access_token')

access_token = refresh_access_token(client_id, client_secret, refresh_token)

def get_track_uris(playlist_ids):
    track_uris = {}

    for genre, playlist_id in playlist_ids.items():
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?fields=items(track(uri))"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            uris = [item["track"]["uri"].split(':')[-1] for item in data["items"]]
            track_uris[genre] = uris

    return track_uris

# Get current track URIs
current_track_uris = get_track_uris(playlist_ids)

# Get previous track URIs (assuming yesterday's date)
yesterday = datetime.today()
previous_track_uris = get_track_uris(playlist_ids)

# ===== CODE: Gen&Save =====

playlist_ids = {
    'Electronic': '6oQkWFEnlrUwJgT0mhLFrT',
    'Rock': '3V2BzWCLA1PCwrDtqGQQuD',
    'Country': '3p42i1uBUrUVS3tyPCNiBr',
    'Pop': '0k6moem5uH1Azl6ljzh0oY',
    'Hip_Hop': '3Bwe7tqWapdwkUaKb6BsmF'
}

for genre in genres:
    current_track_ids = current_track_uris.get(genre, [])
    previous_track_ids = previous_track_uris.get(genre, [])
    playlist_df = generate_playlist(df, genre, ordering_rule, datetime.today(), current_track_ids, previous_track_ids)
    playlist_df.to_csv(f'out/tables/playlist_{genre}.csv', index=False, columns=['track_id', 'artist_name', 'track_name', 'genre', 'category', 'predicted_popularity', 'position'])

