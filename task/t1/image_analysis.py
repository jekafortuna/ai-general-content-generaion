import base64

from task.client import OpenAIClient
from task.constants import OPENAI_HOST

# https://platform.openai.com/docs/guides/images-vision?api-mode=chat#analyze-images
# https://platform.openai.com/docs/guides/images-vision?api-mode=chat&format=base64-encoded#analyze-images

#TODO:
# You need to analyse these 2 images:
#   - https://a-z-animals.com/media/2019/11/Elephant-male-1024x535.jpg
#   - in this folder we have 'banner.png', load it as encoded data (see documentation)
# ---
# Hints:
#   - Use OpenAIClient to connect to OpenAI API
#   - Use /v1/chat/completions endpoint
#   - Function to encode image to base64 you can find in documentation
# ---
# In the end load both images (url and base64 encoded 'banner.png'), ask "Generate poem based on images" and se what will happen?


