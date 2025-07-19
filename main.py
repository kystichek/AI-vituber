#main
from recorder import record_and_transcribe
from ai_handler import get_ai_response
from tts_silero import speak_async
import time
import os
from twitch import get_chat

os.environ['SDL_AUDIODRIVER'] = 'pipewire'
os.environ["PYTHONWARNINGS"] = "ignore"

if __name__ == "__main__":
    try:
        while True:
            text = record_and_transcribe()
            twitch_text = get_chat()

            if twitch_text != None:
                response = get_ai_response(twitch_text)
                speak_async(response)
                twitch_text = None
                continue

            if not text:  # Проверка на пустую строку или None
                continue

            print("👂 Распознано:", text)

            response = get_ai_response(text)
            print("🤖 Ответ:", response)
            speak_async(response)
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\n[ЗАВЕРШЕНО] Работа завершена.")
