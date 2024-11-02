# Dockerfile for voice_recognition
FROM python:3.10-slim

# Install necessary libraries and build tools
RUN apt-get update && \
    apt-get install -y gcc portaudio19-dev libasound-dev && \
    pip install SpeechRecognition pyaudio

# Install required dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
WORKDIR /app
COPY main.py .

# Run the main voice recognition script
CMD ["python", "main.py"]
