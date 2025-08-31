import json
from typing import Any

import requests

from task.constants import OPENAI_HOST, OPENAI_API_KEY

# https://platform.openai.com/docs/guides/speech-to-text?lang=curl

#TODO:
# You need to transcribe 'codeus_audio.mp3':
#   - Create Client that will go to transcriptions OpenAI API
#   - Call API and provide file (pay attention that you work with 'multipart/form-data')
#   - Get response with transcription
# ---
# Hints:
#   - Use /v1/audio/transcriptions endpoint
#   - Use whisper-1 or gpt-4o-transcribe

class OpenAIClient:
    def __init__(self, endpoint: str):
        api_key = OPENAI_API_KEY
        if not api_key:
            raise ValueError("API key cannot be null or empty")
        self._api_key = "Bearer " + api_key
        self._endpoint = endpoint

    def call(self, audio_file_path: str,  print_response=True, **kwargs) -> dict[str, Any]:
        headers = {
            "Authorization": self._api_key,
        }

        files = {'file': open(audio_file_path, 'rb')}

        response = requests.post(
            url=self._endpoint,
            headers=headers,
            files=files,
            data=kwargs
        )

        files['file'].close()

        if response.status_code == 200:
            data = response.json()
            if print_response:
                print(json.dumps(data, indent=2))
            return data

        raise Exception(f"HTTP {response.status_code}: {response.text}")


def main(model_name: str, audio_file_path: str):
    client = OpenAIClient(
        endpoint=OPENAI_HOST + "/v1/audio/transcriptions",
    )

    response = client.call(
        model=model_name,
        audio_file_path=audio_file_path,
    )

    return response


result = main(
    model_name="gpt-4o-transcribe",  # Use whisper-1 or gpt-4o-transcribe
    audio_file_path="codeus_audio.mp3"
)