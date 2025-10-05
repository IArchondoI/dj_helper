from mistralai import Mistral
from src.key_assignment.mistral_credentials import MISTRAL_API_KEY
import re
import json


def fetch_key_and_bpm(song_title: str, artist_name: str) -> dict:
    """
    Fetch the key and BPM of a song using Mistral's medium model.
    """
    prompt = (
        f"You are an expert in music and can determine a song's key based on your knowledge\n"
        f"What key and BPM is the following song written in?\n"
        f"Song: {song_title}\n"
        f"Artist: {artist_name}\n\n"
        "Respond **only** with a valid JSON object. Do not include any extra text.\n"
        "{\n"
        '  "Key"[str]: e.g. "GM" or "Cm",\n'
        '  "Sharp"[bool]: e.g. true,\n'
        '  "BPM"[int]: e.g. 120\n'
        '  "Source"[URL]: e.g. https://songbpm.com/@vicco/nochentera-yeNxZituGU\n'
        "}\n"
        "If the song is in a flat key, return the sharp variant."
    )

    client = Mistral(api_key=MISTRAL_API_KEY)
    model = "mistral-large-latest"
    chat_response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "user",
                "content": f"{prompt}",
            },
        ],
    )

    # Extract the text the model returned
    response_text = chat_response.choices[0].message.content

    # Sometimes the model includes newlines or extra spaces
    clean_text = re.sub(
        r"^```json\s*|\s*```$", "", str(response_text), flags=re.MULTILINE
    ).strip()

    # Convert to Python dict
    return json.loads(clean_text)
