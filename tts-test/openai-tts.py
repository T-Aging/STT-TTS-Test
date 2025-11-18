from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

resp = client.audio.speech.create(
    model="gpt-4o-mini-tts",
    voice="alloy",
    input="안녕하세요! 마실이에요!!",
    response_format="mp3"
)

with open("tts.mp3", "wb") as f:
    f.write(resp.read())
