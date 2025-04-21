import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables
load_dotenv()
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="playlist-modify-public user-read-recently-played"
), requests_timeout=30)

def create_playlist_from_recent_tracks():
    user_id = sp.current_user()["id"]
    recent_tracks = sp.current_user_recently_played(limit=10)
    track_uris = [item["track"]["uri"] for item in recent_tracks["items"]]

    playlist = sp.user_playlist_create(user=user_id, name="Mood Booster 🎶", public=True)
    sp.playlist_add_items(playlist["id"], track_uris)
    print("Playlist created:", playlist["external_urls"]["spotify"])

if __name__ == "__main__":
    create_playlist_from_recent_tracks()
