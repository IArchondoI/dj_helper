import csv
from typing import List, Tuple
from src.models.song import Song
from src.models.evaluated_song import EvaluatedSong, MusicalKey, Mode
from pathlib import Path


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


def load_songs_from_csv(
    file_path: Path,
) -> Tuple[List[Song], List[EvaluatedSong]]:
    """Load songs from a CSV file."""
    songs = []
    evaluated_songs = []

    with open(file_path, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            title = row.get("title")
            artist = row.get("artist")
            key = row.get("key")
            bpm = row.get("bpm")

            if title and artist:
                # Transform key and bpm into MusicalKey dataclass
                if key and bpm:
                    mode = Mode.MAJOR if "MAJOR" in key else Mode.MINOR
                    base_key = key.replace("_MAJOR", "").replace("_MINOR", "")
                    sharp = "#" in base_key
                    base_key = base_key.replace("#", "")
                    evaluated_songs.append(
                        EvaluatedSong(
                            title=title,
                            artist=artist,
                            key=MusicalKey(
                                key=base_key, mode=mode, sharp=sharp
                            ),
                            bpm=int(float(bpm)),
                        )
                    )
                else:
                    songs.append(Song(title=title, artist=artist))

    return songs, evaluated_songs
