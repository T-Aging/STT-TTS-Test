import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(filename="voice.wav", duration=20, fs=16000):
    print("녹음 시작!")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, recording)
    print("녹음 완료:", filename)

if __name__ == "__main__":
    record_audio()
 