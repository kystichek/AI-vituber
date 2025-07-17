import os
import queue
import sounddevice as sd
import wave
import webrtcvad
import tempfile
from faster_whisper import WhisperModel

samplerate = 16000
blocksize = 160
channels = 1
dtype = "int16"
vad = webrtcvad.Vad(2)
q = queue.Queue()

model = WhisperModel("medium", device="cpu", compute_type="int8")

def callback(indata, frames, time_info, status):
    if status:
        print(status)
    q.put(bytes(indata))

def record_and_transcribe() -> str:
    print("🎤 Говори... (Ctrl+C для выхода)")
    silence = 0
    max_silence_blocks = 30
    speech = bytearray()

    with sd.RawInputStream(samplerate=samplerate, blocksize=blocksize, dtype=dtype,
                           channels=channels, callback=callback):
        while True:
            audio = q.get()
            if vad.is_speech(audio, samplerate):
                speech.extend(audio)
                silence = 0
            elif speech:
                silence += 1
                if silence > max_silence_blocks:
                    break

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        wavfile = f.name
        with wave.open(f, 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(2)
            wf.setframerate(samplerate)
            wf.writeframes(speech)

    segments, _ = model.transcribe(wavfile)
    full_text = "".join([segment.text for segment in segments])
    os.remove(wavfile)
    return full_text.strip()
