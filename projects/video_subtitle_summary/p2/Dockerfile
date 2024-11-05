# Use NVIDIA base image for CUDA support
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04

# Set environment variable for timezone
ENV TZ=Etc/UTC

# Install Python, system dependencies, and tzdata non-interactively
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip ffmpeg tzdata && \
    rm -rf /var/lib/apt/lists/*

# Set up the working directory
WORKDIR /app

# Copy and install requirements with GPU-compatible PyTorch
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the subtitle generation script
COPY generate_subtitles.py ./

# Create input and output directories
RUN mkdir -p /app/input /app/output

# Set the command to run the script
CMD ["python3", "generate_subtitles.py"]
