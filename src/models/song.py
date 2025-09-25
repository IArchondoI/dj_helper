from dataclasses import dataclass


@dataclass
class Song:
    """
    Represents a song with a title and an artist.
    """

    title: str
    artist: str
