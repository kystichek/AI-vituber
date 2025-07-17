import wave
from piper import PiperVoice
from pygame import mixer

def speak(text):
    mixer.init()
    voice = PiperVoice.load("ru_RU-ruslan-medium.onnx")
    with wave.open("test.wav", "wb") as wav_file:
        voice.synthesize_wav(text, wav_file)


    mixer.music.load("test.wav")
    mixer.music.play()
