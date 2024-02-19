# Use the official Python image as base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container at /app
COPY main.py /app/main.py

# Copy the entrypoint script into the container at /app
COPY entrypoint.sh /app/entrypoint.sh

# Install any dependencies specified in requirements.txt
RUN pip install moviepy loguru

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Run the entrypoint script when the container launches
ENTRYPOINT ["/app/entrypoint.sh"]
