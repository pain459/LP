# Speech-to-Text Project with Docker and Apache Spark

This project converts speech to text using OpenAI's Whisper library, Docker, and Apache Spark. It supports transcription from both audio files and real-time audio recording.

## Features
- File-based transcription for supported formats (MP3, FLAC, WAV).
- Real-time recording-based transcription.
- Distributed processing of large audio files with Apache Spark.

## Project Structure
- `main.py`: Main script for processing audio files or recording audio.
- `Dockerfile`: Dockerfile for Whisper setup.
- `docker-compose.yml`: Sets up both Whisper and Spark containers.
- `spark/`: Directory containing Spark Dockerfile.
- `utils/`: Utility scripts for audio processing and transcription.
- `data/audio_files`: Folder to store audio files for transcription.

## Setup and Usage

### 1. Install Docker and Docker Compose

Make sure Docker and Docker Compose are installed.

### 2. Build and Start Containers

```bash
docker-compose up --build
