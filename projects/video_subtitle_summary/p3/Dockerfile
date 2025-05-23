# Use NVIDIA CUDA base image for GPU support
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04

# Set environment variable for timezone
ENV TZ=Etc/UTC

# Add deadsnakes PPA and install Python 3.10
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y python3.10 python3.10-distutils python3-pip tzdata curl && \
    rm -rf /var/lib/apt/lists/*

# Install pip for Python 3.10
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10

# Set up the working directory
WORKDIR /app

# Copy requirements and install transformers
COPY requirements.txt ./
RUN python3.10 -m pip install --no-cache-dir transformers

# Install CUDA-compatible PyTorch directly
RUN python3.10 -m pip install torch --index-url https://download.pytorch.org/whl/cu118

# Copy the summarization script
COPY generate_summary.py ./

# Create input and output directories
RUN mkdir -p /app/input /app/output

# Set the command to run the script
CMD ["python3.10", "/app/generate_summary.py"]
