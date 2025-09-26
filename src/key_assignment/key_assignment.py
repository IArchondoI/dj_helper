from src.models.song import Song
from src.models.evaluated_song import EvaluatedSong, Key
import random
from typing import List
from src.key_assignment.spotify_key_bpm_fetcher import fetch_key_and_bpm


def assign_random_keys(songs: List[Song]) -> List[EvaluatedSong]:
    """
    Assigns random keys and bpm to a list of songs.
    """
    keys = list(Key)
    return [
        EvaluatedSong(
            title=song.title,
            artist=song.artist,
            key=random.choice(keys),
            bpm=random.randint(60, 180),
        )
        for song in songs
    ]


def assign_keys(
    songs: List[Song], use_spotipy: bool = False
) -> List[EvaluatedSong]:
    """
    Assigns keys and BPM to a list of songs.

    Args:
        songs (List[Song]): List of songs to evaluate.
        use_spotipy (bool): Whether to use Spotipy for key and BPM assignment.

    Returns:
        List[EvaluatedSong]: List of evaluated songs with keys and BPM.
    """
    if use_spotipy:
        evaluated_songs = []
        for song in songs:
            try:
                spotify_data = fetch_key_and_bpm(song.title, song.artist)
                evaluated_songs.append(
                    EvaluatedSong(
                        title=song.title,
                        artist=song.artist,
                        key=Key(spotify_data["key"]),
                        bpm=spotify_data["bpm"],
                    )
                )
            except ValueError as e:
                print(
                    f"Error fetching data for {song.title} by {song.artist}: {e}"
                )
        return evaluated_songs
    else:
        return assign_random_keys(songs)
