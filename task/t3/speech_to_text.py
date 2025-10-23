import json

import requests

from task.constants import OPENAI_HOST, OPENAI_API_KEY


# https://platform.openai.com/docs/guides/speech-to-text?lang=curl

# TODO:
# You need to transcribe 'codeus_audio.mp3':
#   - Create Client that will go to transcriptions OpenAI API
#   - Call API and provide file (pay attention that you work with 'multipart/form-data')
#   - Get response with transcription
# ---
# Hints:
#   - Use /v1/audio/transcriptions endpoint
#   - Use whisper-1 or gpt-4o-transcribe model


class OpenAIClient:

    def __init__(self):
        if not OPENAI_API_KEY:
            raise ValueError("OPENAI key cannot be null or empty")

        self._api_key = f"Bearer {OPENAI_API_KEY}"
        self._endpoint = f"{OPENAI_HOST}/v1/audio/transcriptions"

    def call(self, audio_file_path: str, print_response=True, **kwargs):
        headers = {
            "Authorization": self._api_key
        }

        files = {
            'file': open(audio_file_path, 'rb')
        }

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
        else:
            raise Exception(f"HTTP {response.status_code}: {response.text}")


client = OpenAIClient()
client.call(
    model="whisper-1",
    # model="gpt-4o-transcribe",
    audio_file_path="task/t3/codeus_audio.mp3"
)
