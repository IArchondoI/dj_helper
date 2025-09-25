from dataclasses import dataclass
from enum import Enum


class Key(Enum):
    """
    Enum representing musical keys.
    """

    A = "A"
    A_SHARP = "A#"
    B = "B"
    C = "C"
    C_SHARP = "C#"
    D = "D"
    D_SHARP = "D#"
    E = "E"
    F = "F"
    F_SHARP = "F#"
    G = "G"
    G_SHARP = "G#"


@dataclass
class EvaluatedSong:
    """
    Represents a song with additional evaluation details like key and bpm.
    """

    title: str
    artist: str
    key: Key
    bpm: int
