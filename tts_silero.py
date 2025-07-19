# tts_silero_live_play.py
import torch
import numpy as np
import sounddevice as sd
import threading

language = 'ru'
model_id = 'v4_ru'
sample_rate = 48000
speaker = 'baya'
device = torch.device('cpu')

# Загружаем модель один раз
model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model='silero_tts',
                                     language=language,
                                     speaker=model_id)
model.to(device)

def _play_audio(text: str):
    try:
        # Генерация аудио
        audio = model.apply_tts(text=text,
                                speaker=speaker,
                                sample_rate=sample_rate)

        # Преобразуем в NumPy и воспроизводим
        audio_np = audio.numpy()
        sd.play(audio_np, samplerate=sample_rate)
        sd.wait()

    except Exception as e:
        print(f"⚠️ Ошибка воспроизведения: {e}")

def speak(text: str):
    """Синхронный режим"""
    _play_audio(text)

def speak_async(text: str):
    """Асинхронный режим, не блокирует поток"""
    threading.Thread(target=_play_audio, args=(text,), daemon=True).start()
