import whisper
from utils.audio_processing import record_audio
from utils.transcriber import transcribe_audio

def main():
    audio_path = record_audio()  # Capture or load audio
    text = transcribe_audio(audio_path)
    print("Transcription:", text)

if __name__ == "__main__":
    main()
