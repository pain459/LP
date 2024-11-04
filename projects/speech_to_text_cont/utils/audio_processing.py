import sounddevice as sd
from scipy.io.wavfile import write
import config

def record_audio(duration):
    print("Recording audio...")
    audio = sd.rec(int(duration * config.SAMPLE_RATE), samplerate=config.SAMPLE_RATE, channels=1)
    sd.wait()  # Wait until the recording is finished
    audio_path = "recorded_audio.wav"
    write(audio_path, config.SAMPLE_RATE, audio)  # Save as WAV file
    print("Recording complete.")
    return audio_path
