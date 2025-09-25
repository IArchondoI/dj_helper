from src.models.song import Song
from src.models.evaluated_song import EvaluatedSong, Key
import random
from typing import List


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
