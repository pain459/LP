# Use a base Python image
FROM python:3.10-slim

# Install ffmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Set up the working directory
WORKDIR /app

# Copy the requirements file if you plan to add additional Python packages
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script
COPY extract_audio.py ./

# Directories for input video files and output audio files
RUN mkdir -p /app/input /app/output

# Set the command to run the script when the container starts
CMD ["python", "extract_audio.py"]
