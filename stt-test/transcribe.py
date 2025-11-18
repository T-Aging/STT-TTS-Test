import os
from dotenv import load_dotenv
import openai

# .env 파일 불러오기
load_dotenv()

# 환경변수에서 API 키 가져오기
openai.api_key = os.getenv("OPENAI_API_KEY")

# 변환할 음성 파일
audio_file_path = "testaudio.m4a"

with open(audio_file_path, "rb") as audio_file:
    transcript = openai.audio.transcriptions.create(
        model="gpt-4o-transcribe",  # 모델 이름 소문자, 하이픈
        file=audio_file
    )

print("=== Transcription ===")
print(transcript.text)