from dataclasses import dataclass
from enum import Enum


class Mode(Enum):
    MAJOR = "M"
    MINOR = "m"


@dataclass(frozen=True)
class MusicalKey:
    key: str
    mode: Mode
    sharp: bool = False

    def __str__(self):
        sharp_symbol = "#" if self.sharp else ""
        return f"{self.key}{sharp_symbol}{self.mode.value}"


@dataclass
class EvaluatedSong:
    """
    Represents a song with additional evaluation details like key and bpm.
    """

    title: str
    artist: str
    key: MusicalKey
    bpm: int
