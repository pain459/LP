# Use a base Python image
FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Set up the working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the subtitle generation script
COPY generate_subtitles.py ./

# Create input and output directories
RUN mkdir -p /app/input /app/output

# Set the command to run the script
CMD ["python", "generate_subtitles.py"]
