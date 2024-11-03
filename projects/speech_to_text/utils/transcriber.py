import whisper

def transcribe_audio(audio_path, model):
    result = model.transcribe(audio_path)
    return result["text"]
