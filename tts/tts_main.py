import sys
sys.path.append('./tts_dia/dia')
from app import app  # 예시: app.py에 TTS 기능이 있으면 변경 필요


def main():
    tts = TTS(speaker="female")  # 여자 목소리로 설정
    print("텍스트를 입력하세요 (종료하려면 빈 줄 입력):")
    
    while True:
        text = input("> ")
        if text.strip() == "":
            print("종료합니다.")
            break
        print(f"입력한 텍스트: {text}")
        tts.speak(text)

if __name__ == "__main__":
    main()
