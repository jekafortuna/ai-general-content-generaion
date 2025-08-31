import json
from datetime import datetime
from typing import Any

import requests

from task.constants import OPENAI_HOST, OPENAI_API_KEY


class OpenAIClient:

    def __init__(self, endpoint: str):
        api_key = OPENAI_API_KEY
        if not api_key:
            raise ValueError("API key cannot be null or empty")

        self._api_key = "Bearer " + api_key
        self._endpoint = endpoint

    def call(self, print_request=True, print_response=True, **kwargs) -> dict[str, Any]:
        headers = {
            "Authorization": self._api_key,
            "Content-Type": "application/json"
        }

        output_file: str = f"{datetime.now()}.mp3"

        if print_request:
            print(json.dumps(kwargs, indent=2))

        response = requests.post(url=self._endpoint, headers=headers, json=kwargs)

        if response.status_code == 200:
            with open(output_file, 'wb') as f:
                f.write(response.content)

            if print_response:
                print(f"Audio saved to {output_file}")

            return {"message": f"Audio saved to {output_file}", "file": output_file}

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


def main(model_name: str, text: str, voice: str = Voice.echo, **kwargs):
    client = OpenAIClient(
        endpoint=OPENAI_HOST + "/v1/audio/speech",
    )

    response = client.call(
        model=model_name,
        input=text,
        voice=voice,
        **kwargs
    )

    return response


if __name__ == "__main__":
    main(
        model_name="gpt-4o-mini-tts",
        text="Why can't we say that black is white?",
        voice=Voice.coral,
        instructions="Speak in a cheerful and positive tone.",
    )
