import base64
import json
from datetime import datetime

import requests

from task.constants import OPENAI_HOST, OPENAI_API_KEY

# https://platform.openai.com/docs/guides/audio?example=audio-in#add-audio-to-your-existing-application

#TODO:
# You need to generate answer in audio format based on the audio message:
#   - Create Client that is similar with OpenAIClients but extracts from message audio (instead of content)
#   - Call API
#   - Get response as base64 content, decode and save as .mp3 file
# ---
# Hints:
#   - Use /v1/chat/completions endpoint
#   - Use gpt-4o-audio-preview model
#   - Use modalities=["text", "audio"]
#   - Use audio={"voice": "ballad", "format": "mp3"}
#   - Similar method to encode audio https://platform.openai.com/docs/guides/images-vision?api-mode=chat&lang=python

