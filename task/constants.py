import os

from dotenv import load_dotenv

load_dotenv()

DEFAULT_SYSTEM_PROMPT = "You are an assistant who answers concisely and informatively."

OPENAI_HOST = "https://api.openai.com"
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
