# from vosk import Model, KaldiRecognizer
# import pyaudio

# model = Model("vosk-model-small-ko-0.22")  # 모델 폴더명
# recognizer = KaldiRecognizer(model, 16000)

# p = pyaudio.PyAudio()
# stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4000)
# stream.start_stream()

# print("말을 시작하세요... (Ctrl+C로 종료)")

# try:
#     while True:
#         data = stream.read(4000, exception_on_overflow=False)
#         if recognizer.AcceptWaveform(data):
#             print(recognizer.Result())
#         else:
#             print(recognizer.PartialResult())
# except KeyboardInterrupt:
#     print("종료합니다.")
# finally:
#     stream.stop_stream()
#     stream.close()
#     p.terminate()

# import whisper
# import pyaudio
# import numpy as np

# model = whisper.load_model("base")

# p = pyaudio.PyAudio()
# rate = 16000
# chunk = 1024

# stream = p.open(format=pyaudio.paInt16, channels=1, rate=rate, input=True, frames_per_buffer=chunk)

# print("말을 시작하세요... (Ctrl+C로 종료)")

# frames = []

# try:
#     while True:
#         data = stream.read(chunk, exception_on_overflow=False)
#         frames.append(data)
#         if len(frames) * chunk >= rate * 5:  # 5초 길이 버퍼
#             audio_data = b''.join(frames)
#             # numpy 배열로 변환
#             audio_np = np.frombuffer(audio_data, np.int16).astype(np.float32) / 32768.0
#             # Whisper가 인식할 오디오로 변환
#             result = model.transcribe(audio_np, language='ko')
#             print(result['text'])
#             frames = []  # 버퍼 초기화
# except KeyboardInterrupt:
#     print("종료합니다.")
# finally:
#     stream.stop_stream()
#     stream.close()
#     p.terminate()

import whisper
import pyaudio
import numpy as np

model = whisper.load_model("large")

p = pyaudio.PyAudio()
rate = 16000
chunk = 1024

stream = p.open(format=pyaudio.paInt16, channels=1, rate=rate, input=True, frames_per_buffer=chunk)

print("한국어로 말씀하세요... (Ctrl+C로 종료)")

frames = []

try:
    while True:
        data = stream.read(chunk, exception_on_overflow=False)
        frames.append(data)
        if len(frames) * chunk >= rate * 5:  # 5초 길이 버퍼
            audio_data = b''.join(frames)
            audio_np = np.frombuffer(audio_data, np.int16).astype(np.float32) / 32768.0
            result = model.transcribe(audio_np, language='ko')  # 한국어 인식
            print(result['text'])
            frames = []
except KeyboardInterrupt:
    print("종료합니다.")
finally:
    stream.stop_stream()
    stream.close()
    p.terminate()
