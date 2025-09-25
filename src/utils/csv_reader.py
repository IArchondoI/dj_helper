import csv
from typing import List
from src.models.song import Song


def read_songs_from_csv(file_path: str) -> List[Song]:
    """
    Reads a CSV file and transforms it into a list of Song dataclasses.
    """
    songs = []
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            songs.append(Song(title=row["title"], artist=row["artist"]))
    return songs
