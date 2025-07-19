#recorder
import speech_recognition as sr
import json
import os

# Отключаем предупреждения
os.environ["PYTHONWARNINGS"] = "ignore"
os.environ['SDL_AUDIODRIVER'] = 'pipewire'

recognizer = sr.Recognizer()

def record_and_transcribe():
    try:
        with sr.Microphone() as mic:
            # Настройка чувствительности к шуму
            recognizer.adjust_for_ambient_noise(mic, duration=1)
            pause_threshold = 1.5

            print("Говорите...")
            audio = recognizer.listen(mic)

            # Распознавание с помощью Vosk
            json_result = recognizer.recognize_vosk(audio_data=audio, language='ru-RU')
            result = json.loads(json_result)

            text = result.get("text", "").strip().lower()
            if text:
                print("📝 Распознано:", text)
                return text
            else:
                print("⚠️ Ничего не распознано.")
    except Exception as e:
        print(f"❌ Ошибка распознавания: {e}")
