import random
from typing import List, Dict


def assign_random_keys(songs: List[str]) -> List[Dict[str, str]]:
    """
    Assigns random keys to a list of songs.
    """
    keys = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    return [{"song": song, "key": random.choice(keys)} for song in songs]
