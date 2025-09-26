import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from src.key_assignment.spotify_credentials import (
    SPOTIFY_CLIENT_ID,
    SPOTIFY_CLIENT_SECRET,
)


def fetch_key_and_bpm(song_title, artist_name):
    """
    Fetch the key and BPM of a song using the Spotify API.

    Args:
        song_title (str): The title of the song.
        artist_name (str): The name of the artist.

    Returns:
        dict: A dictionary containing the key and BPM of the song.
    """
    # Authenticate with Spotify
    client_credentials_manager = SpotifyClientCredentials(
        client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET
    )
    sp = spotipy.Spotify(auth_manager=client_credentials_manager)

    # Search for the song
    query = f"track:{song_title} artist:{artist_name}"
    results = sp.search(q=query, type="track", limit=1)

    # Validate search results
    if (
        not results
        or not results.get("tracks")
        or not results["tracks"].get("items")
    ):
        raise ValueError(
            f"Song '{song_title}' by '{artist_name}' not found on Spotify."
        )

    track = results["tracks"]["items"][0]
    track_id = track["id"]

    # Get audio features
    audio_features = sp.audio_features(track_id)

    if not audio_features or not audio_features[0]:
        raise ValueError(
            f"Audio features for '{song_title}' by '{artist_name}' not found."
        )

    return {
        "key": audio_features[0]["key"],
        "bpm": audio_features[0]["tempo"],
    }
