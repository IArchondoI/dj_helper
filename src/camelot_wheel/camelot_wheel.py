"""
Determines if two keys are harmonically compatible based on Camelot notation.
"""

from src.models.evaluated_song import MusicalKey
from src.models.evaluated_song import Mode


def is_harmonically_compatible(key1: MusicalKey, key2: MusicalKey) -> bool:
    if key1 == key2:
        return True
    camelot_wheel = {
        MusicalKey("C", Mode.MAJOR): [
            MusicalKey("F", Mode.MAJOR),
            MusicalKey("G", Mode.MAJOR),
            MusicalKey("A", Mode.MINOR),
        ],
        MusicalKey("G", Mode.MAJOR): [
            MusicalKey("C", Mode.MAJOR),
            MusicalKey("D", Mode.MAJOR),
            MusicalKey("E", Mode.MINOR),
        ],
        MusicalKey("D", Mode.MAJOR): [
            MusicalKey("G", Mode.MAJOR),
            MusicalKey("A", Mode.MAJOR),
            MusicalKey("B", Mode.MINOR),
        ],
        MusicalKey("A", Mode.MAJOR): [
            MusicalKey("D", Mode.MAJOR),
            MusicalKey("E", Mode.MAJOR),
            MusicalKey("F#", Mode.MINOR),
        ],
        MusicalKey("E", Mode.MAJOR): [
            MusicalKey("A", Mode.MAJOR),
            MusicalKey("B", Mode.MAJOR),
            MusicalKey("C#", Mode.MINOR),
        ],
        MusicalKey("B", Mode.MAJOR): [
            MusicalKey("E", Mode.MAJOR),
            MusicalKey("F#", Mode.MAJOR),
            MusicalKey("G#", Mode.MINOR),
        ],
        MusicalKey("F#", Mode.MAJOR): [
            MusicalKey("B", Mode.MAJOR),
            MusicalKey("C#", Mode.MAJOR),
            MusicalKey("D#", Mode.MINOR),
        ],
        MusicalKey("C#", Mode.MAJOR): [
            MusicalKey("F#", Mode.MAJOR),
            MusicalKey("G#", Mode.MAJOR),
            MusicalKey("A#", Mode.MINOR),
        ],
        MusicalKey("G#", Mode.MAJOR): [
            MusicalKey("C#", Mode.MAJOR),
            MusicalKey("D#", Mode.MAJOR),
            MusicalKey("F", Mode.MINOR),
        ],
        MusicalKey("D#", Mode.MAJOR): [
            MusicalKey("G#", Mode.MAJOR),
            MusicalKey("A#", Mode.MAJOR),
            MusicalKey("C", Mode.MINOR),
        ],
        MusicalKey("A#", Mode.MAJOR): [
            MusicalKey("D#", Mode.MAJOR),
            MusicalKey("F", Mode.MAJOR),
            MusicalKey("G", Mode.MINOR),
        ],
        MusicalKey("F", Mode.MAJOR): [
            MusicalKey("A#", Mode.MAJOR),
            MusicalKey("C", Mode.MAJOR),
            MusicalKey("D", Mode.MINOR),
        ],
        MusicalKey("A", Mode.MINOR): [
            MusicalKey("D", Mode.MINOR),
            MusicalKey("E", Mode.MINOR),
            MusicalKey("C", Mode.MAJOR),
        ],
        MusicalKey("E", Mode.MINOR): [
            MusicalKey("A", Mode.MINOR),
            MusicalKey("B", Mode.MINOR),
            MusicalKey("G", Mode.MAJOR),
        ],
        MusicalKey("B", Mode.MINOR): [
            MusicalKey("E", Mode.MINOR),
            MusicalKey("F#", Mode.MINOR),
            MusicalKey("D", Mode.MAJOR),
        ],
        MusicalKey("F#", Mode.MINOR): [
            MusicalKey("B", Mode.MINOR),
            MusicalKey("C#", Mode.MINOR),
            MusicalKey("A", Mode.MAJOR),
        ],
        MusicalKey("C#", Mode.MINOR): [
            MusicalKey("F#", Mode.MINOR),
            MusicalKey("G#", Mode.MINOR),
            MusicalKey("E", Mode.MAJOR),
        ],
        MusicalKey("G#", Mode.MINOR): [
            MusicalKey("C#", Mode.MINOR),
            MusicalKey("D#", Mode.MINOR),
            MusicalKey("B", Mode.MAJOR),
        ],
        MusicalKey("D#", Mode.MINOR): [
            MusicalKey("G#", Mode.MINOR),
            MusicalKey("A#", Mode.MINOR),
            MusicalKey("F#", Mode.MAJOR),
        ],
        MusicalKey("A#", Mode.MINOR): [
            MusicalKey("D#", Mode.MINOR),
            MusicalKey("F", Mode.MINOR),
            MusicalKey("C#", Mode.MAJOR),
        ],
        MusicalKey("F", Mode.MINOR): [
            MusicalKey("A#", Mode.MINOR),
            MusicalKey("C", Mode.MINOR),
            MusicalKey("G#", Mode.MAJOR),
        ],
        MusicalKey("C", Mode.MINOR): [
            MusicalKey("F", Mode.MINOR),
            MusicalKey("G", Mode.MINOR),
            MusicalKey("D#", Mode.MAJOR),
        ],
        MusicalKey("G", Mode.MINOR): [
            MusicalKey("C", Mode.MINOR),
            MusicalKey("D", Mode.MINOR),
            MusicalKey("A#", Mode.MAJOR),
        ],
        MusicalKey("D", Mode.MINOR): [
            MusicalKey("G", Mode.MINOR),
            MusicalKey("A", Mode.MINOR),
            MusicalKey("F", Mode.MAJOR),
        ],
    }
    return key2 in camelot_wheel.get(key1, [])
