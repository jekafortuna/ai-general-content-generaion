import json
from datetime import datetime

import requests

from task.constants import OPENAI_HOST, OPENAI_API_KEY

# https://platform.openai.com/docs/guides/text-to-speech
# Request:
# curl https://api.openai.com/v1/audio/speech \
#   -H "Authorization: Bearer $OPENAI_API_KEY" \
#   -H "Content-Type: application/json" \
#   -d '{
#     "model": "gpt-4o-mini-tts",
#     "input": "Why can't we say that black is white?",
#     "voice": "coral",
#     "instructions": "Speak in a cheerful and positive tone."
#   }' \
# Response:
#   bytes with audio

#TODO:
# You need to convert text to speech:
#   - Create Client that will go to speech OpenAI API
#   - Call API
#   - Get response and save as .mp3 file
# ---
# Hints:
#   - Use /v1/audio/speech endpoint
#   - Use gpt-4o-mini-tts model

class OpenAIClient:
    def __init__(self):
        if not OPENAI_API_KEY:
            raise ValueError("OPENAI key cannot be null or empty")

        self._api_key = f"Bearer {OPENAI_API_KEY}"
        self._endpoint = f"{OPENAI_HOST}/v1/audio/speech"

    def call(self, print_request=True, **kwargs):
        headers = {
            "Authorization": self._api_key,
            "Content-Type": "application/json"
        }

        output_file = f"{datetime.now()}.mp3"

        if print_request:
            print(json.dumps(kwargs, indent=2))

        response = requests.post(
            url=self._endpoint,
            headers=headers,
            json=kwargs
        )

        if response.status_code == 200:
            with open(output_file, "wb") as audio:
                audio.write(response.content)
            print(f"Audio saved to {output_file}")
        else:
            raise Exception(f"HTTP {response.status_code}: {response.text}")


class Voice:
    alloy: str = 'alloy'
    ash: str = 'ash'
    ballad: str = 'ballad'
    coral: str = 'coral'
    echo: str = 'echo'
    fable: str = 'fable'
    nova: str = 'nova'
    onyx: str = 'onyx'
    sage: str = 'sage'
    shimmer: str = 'shimmer'


client = OpenAIClient()
client.call(
    model="gpt-4o-mini-tts",
    input="Look, if you had one shot or one opportunity to seize everything you ever wanted "
          "in one moment. Would you capture it or just let it slip? Yo",
    voice="onyx",
    instructions="Deliver this with powerful motivation and urgency, building intensity throughout."
)