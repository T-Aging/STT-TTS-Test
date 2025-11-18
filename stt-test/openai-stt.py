from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# voice.wav 읽기
audio_file = open("voice.wav", "rb")

resp = client.audio.transcriptions.create(
    model="gpt-4o-transcribe",
    file=audio_file,
    response_format="text"   # "text", "json" 등 가능
)

print(resp)
