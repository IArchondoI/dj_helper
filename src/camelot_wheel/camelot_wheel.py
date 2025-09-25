"""
Determines if two keys are harmonically compatible based on Camelot notation.
"""


def is_harmonically_compatible(key1: str, key2: str) -> bool:
    camelot_wheel = {
        "A": ["A#", "D"],
        "A#": ["A", "D#"],
        "B": ["C", "E"],
        "C": ["B", "F"],
        "C#": ["D", "F#"],
        "D": ["A", "C#"],
        "D#": ["A#", "G"],
        "E": ["B", "G#"],
        "F": ["C", "A#"],
        "F#": ["C#", "B"],
        "G": ["D#", "A"],
        "G#": ["E", "C"],
    }
    return key2 in camelot_wheel.get(key1, [])
