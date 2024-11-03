import sounddevice as sd
from scipy.io.wavfile import write
import config

def record_audio(duration=5):
    print("Recording audio...")
    audio = sd.rec(int(duration * config.SAMPLE_RATE), samplerate=config.SAMPLE_RATE, channels=1)
    sd.wait()
    audio_path = "recorded_audio.wav"
    write(audio_path, config.SAMPLE_RATE, audio)
    print("Recording complete.")
    return audio_path
