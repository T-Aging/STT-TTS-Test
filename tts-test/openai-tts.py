from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

resp = client.audio.speech.create(
    model="gpt-4o-mini-tts",
    voice="sage",
    input="안녕하세요 마실이에요!! 아이스 아메리카노를 추천할게요! 피곤하시면 달달한 음료는 어떠세요? 레몬 유자 티 추천드려요!",
    response_format="mp3"
)

with open("tts_sage.mp3", "wb") as f:
    f.write(resp.read())
