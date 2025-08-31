import base64
import json
from datetime import datetime

import requests

from task.constants import OPENAI_HOST, OPENAI_API_KEY

# https://platform.openai.com/docs/guides/audio?example=audio-in

#TODO:
# You need to generate answer in audio format based on the audio message:
#   - Create Client that is similar with OpenAIClients but extracts from message audio (instead of content)
#   - Call API
#   - Get response as base64 content, decode and save as .mp3 file
# ---
# Hints:
#   - Use /v1/chat/completions endpoint
#   - Use gpt-4o-mini-tts model
#   - Use modalities=["text", "audio"]
#   - Use audio={"voice": "ballad", "format": "mp3"}
#   - Similar method to encode audio https://platform.openai.com/docs/guides/images-vision?api-mode=chat&lang=python

class OpenAIClient:

    def __init__(self):
        api_key = OPENAI_API_KEY
        if not api_key:
            raise ValueError("API key cannot be null or empty")

        self._api_key = "Bearer " + api_key
        self._endpoint = OPENAI_HOST + "/v1/chat/completions"

    def call(self, print_request=True, print_response=True, **kwargs):
        headers = {
            "Authorization": self._api_key,
            "Content-Type": "application/json"
        }

        if print_request:
            print(json.dumps(kwargs, indent=2))

        response = requests.post(url=self._endpoint, headers=headers, json=kwargs)

        if response.status_code == 200:
            data = response.json()
            if print_response:
                print(json.dumps(data, indent=2))
            choices = data.get("choices", [])
            if choices:
                message = choices[0].get("message", {})
                if message:
                    audio = message.get("audio", {})
                    if audio:
                        audio_data = audio.get("data")
                        if audio_data:
                            audio_bytes = base64.b64decode(audio_data)
                            output_file = f"{datetime.now()}.mp3"

                            with open(output_file, 'wb') as f:
                                f.write(audio_bytes)
        else:
            raise Exception(f"HTTP {response.status_code}: {response.text}")


def _encode_audio(audio_file_path):
    with open(audio_file_path, "rb") as audio_file:
        return base64.b64encode(audio_file.read()).decode("utf-8")


client = OpenAIClient()
client.call(
    model="gpt-4o-audio-preview",
    modalities=["text", "audio"],
    audio={"voice": "ballad", "format": "mp3"},
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_audio",
                    "input_audio": {
                        "data": _encode_audio("question.mp3"),
                        "format": "mp3"
                    }
                }
            ]
        }
    ]
)
