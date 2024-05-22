# Dockerfile for Component 2
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install necessary tools
RUN apt-get update && apt-get install -y curl

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the scripts directory into the container
COPY scripts/ .

# Set up a directory for logs
RUN mkdir /app/logs
VOLUME /app/logs

# Command to run the Flask application
CMD ["python", "queue_manager.py"]
