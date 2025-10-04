import requests
from src.key_assignment.mistral_credentials import MISTRAL_API_KEY


def fetch_key_and_bpm(song_title: str, artist_name: str) -> dict:
    """
    Fetch the key and BPM of a song using Mistral's medium model.
    """
    prompt = (
        f"what key and BPM is the following song written in?\n"
        f"Song: {song_title}\n"
        f"Artist: {artist_name}\n\n"
        "Please answer in the following format, with no further text or observations:"
        'Key: [str] e.g. "G"\n'
        'Sharp: [bool] e.g. "True"\n'
        'Major/Minor: [str] e.g. "Major"\n'
        "BPM: [int] e.g. 120\n"
        "If the song is in a flat key, return the sharp variant"
        "(e.g. Db is C# for practical purposes)"
    )

    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json",
    }

    response = requests.post(
        "https://api.mistral.ai/v1/models/medium",
        json={"prompt": prompt},
        headers=headers,
    )

    if response.status_code != 200:
        raise ValueError(
            f"Mistral API error: {response.status_code} - {response.text}"
        )

    data = response.json()
    return {
        "key": data["key"],
        "sharp": data["sharp"],
        "major_minor": data["major_minor"],
        "bpm": data["bpm"],
    }
