from recorder import record_and_transcribe
from ai_handler import get_ai_response
from tts_silero import speak

if __name__ == "__main__":
    try:
        while True:
            text = record_and_transcribe()
            if not text.strip():
                print("Ничего не распознано.")
                continue

            print("👂 Распознано:", text)
            response = get_ai_response(text)
            print("🤖 Ответ:", response)
            speak(response)

    except KeyboardInterrupt:
        print("\n[ЗАВЕРШЕНО] Работа завершена.")

