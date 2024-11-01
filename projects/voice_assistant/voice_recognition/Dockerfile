FROM python:3.10-slim

# Install necessary libraries
RUN apt-get update && \
    apt-get install -y portaudio19-dev && \
    pip install SpeechRecognition pyaudio

# Copy application code
WORKDIR /app
COPY main.py .

# Run the main voice recognition script
CMD ["python", "main.py"]
