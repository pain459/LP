import argparse
import whisper
from pyspark.sql import SparkSession
from utils.transcriber import transcribe_audio

def transcribe_with_spark(file_path, model):
    # Initialize Spark session
    spark = SparkSession.builder \
        .appName("SpeechToText") \
        .getOrCreate()

    # Load audio files as an RDD
    audio_rdd = spark.sparkContext.parallelize([file_path])

    # Process files in parallel using Spark
    transcriptions = audio_rdd.map(lambda path: transcribe_audio(path, model)).collect()

    for text in transcriptions:
        print("Transcription:", text)

    spark.stop()

def main():
    parser = argparse.ArgumentParser(description="Speech-to-text with Whisper and Spark")
    parser.add_argument("-f", "--file", type=str, help="Path to an audio file for transcription")
    args = parser.parse_args()

    # Load Whisper model
    model = whisper.load_model("base")

    # If file is provided, process it with Spark
    if args.file:
        transcribe_with_spark(args.file, model)

if __name__ == "__main__":
    main()
