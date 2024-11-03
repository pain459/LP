import whisper
import config

def transcribe_audio(audio_path):
    model = whisper.load_model(config.MODEL_SIZE)
    result = model.transcribe(audio_path)
    return result["text"]
