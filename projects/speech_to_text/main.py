import argparse
import whisper
from utils.audio_processing import record_audio
from utils.transcriber import transcribe_audio

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Speech-to-text conversion using OpenAI Whisper")
    parser.add_argument(
        "-f", "--file",
        type=str,
        help="Path to an audio file (MP3, FLAC, WAV) for transcription"
    )
    parser.add_argument(
        "-r", "--record",
        type=int,
        help="Duration in seconds to record audio for transcription"
    )
    args = parser.parse_args()

    # Load the Whisper model
    model = whisper.load_model("base")

    # Check if file input is provided
    if args.file:
        print(f"Transcribing from file: {args.file}")
        text = transcribe_audio(args.file, model)
        print("Transcription:", text)
    
    # Check if recording duration is provided
    elif args.record:
        print(f"Recording audio for {args.record} seconds...")
        audio_path = record_audio(args.record)  # Record for the specified duration
        text = transcribe_audio(audio_path, model)
        print("Transcription:", text)

    else:
        print("Please provide either --file for file input or --record for real-time recording.")

if __name__ == "__main__":
    main()
