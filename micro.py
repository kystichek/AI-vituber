import wave
import pyaudio
from faster_whisper import WhisperModel

# === Настройки записи ===
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000  # Обязательно 16000 для Whisper
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "audio.wav"

model_size = "tiny"
# === Запись с микрофона ===
p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("🎤 Говори...")

frames = []
for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("🛑 Запись завершена.")

stream.stop_stream()
stream.close()
p.terminate()

# === Сохранение в .wav ===
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

# === Транскрипция через faster-whisper ===
model = WhisperModel(model_size, device="cpu", compute_type="int8")

segments, info = model.transcribe(WAVE_OUTPUT_FILENAME, beam_size=5)

print(f"\n🌐 Язык: {info.language} (вероятность: {info.language_probability:.2f})")
print("📝 Распознанный текст:")
for segment in segments:
    print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")

