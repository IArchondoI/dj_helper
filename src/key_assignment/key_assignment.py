from src.models.song import Song
from src.models.evaluated_song import EvaluatedSong, MusicalKey, Mode
import random
from typing import List
from src.key_assignment.spotify_key_bpm_fetcher import fetch_key_and_bpm


def assign_random_keys(songs: List[Song]) -> List[EvaluatedSong]:
    """
    Assigns random keys and bpm to a list of songs.
    """
    keys = [
        MusicalKey(key=note, mode=mode, sharp=sharp)
        for note in ["C", "D", "E", "F", "G", "A", "B"]
        for mode in [Mode.MAJOR, Mode.MINOR]
        for sharp in [False, True]
        if not (note == "E" and sharp) and not (note == "B" and sharp)
    ]
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
                        key=MusicalKey(
                            key=spotify_data["key"].replace("#", ""),
                            mode=Mode.MAJOR
                            if "MAJOR" in spotify_data["key"]
                            else Mode.MINOR,
                            sharp="#" in spotify_data["key"],
                        ),
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
