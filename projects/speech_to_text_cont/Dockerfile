# Base Python image with CUDA for GPU support, if available
FROM nvidia/cuda:11.6.0-cudnn8-runtime-ubuntu20.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Install Whisper and other Python dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy project files
COPY . /app
WORKDIR /app

# Command to run the main script
CMD ["python3", "main.py"]
