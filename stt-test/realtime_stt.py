import sounddevice as sd
import numpy as np
from openai import OpenAI
import threading
import queue
import sys

client = OpenAI()

SAMPLE_RATE = 16000
CHANNELS = 1

audio_queue = queue.Queue()

def audio_callback(indata, frames, time, status):
    """마이크 입력을 queue에 넣음"""
    if status:
        print(status, file=sys.stderr)
    audio_queue.put(indata.copy())

def stream_audio():
    """Queue의 오디오 데이터를 계속 OpenAI 서버로 전송"""
    print("🎤 실시간 음성 인식 시작! 말하세요... (Ctrl+C로 종료)\n")

    stream = client.audio.transcriptions.stream(
        model="gpt-4o-transcribe",
    )

    stream.start()

    try:
        while True:
            chunk = audio_queue.get()
            stream.send(chunk.tobytes())

            for event in stream:
                if event.type == "transcription.partial":
                    print(f"\r📝 {event.text}", end="", flush=True)

                elif event.type == "transcription.completed":
                    print("\n✔ 최종 결과:", event.text)
    except KeyboardInterrupt:
        print("\n🛑 종료합니다...")
        stream.stop()

def main():
    with sd.InputStream(
        callback=audio_callback,
        channels=CHANNELS,
        samplerate=SAMPLE_RATE,
        dtype="int16",
        blocksize=8000,
    ):
        stream_audio()

if __name__ == "__main__":
    main()