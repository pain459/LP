# Use the official Python image as base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container at /app
COPY your_script.py /app/your_script.py

# Copy the entrypoint script into the container at /app
COPY entrypoint.sh /app/entrypoint.sh

# Install any dependencies specified in requirements.txt
RUN pip install moviepy loguru

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Set CPU and memory limits
ENV CPU_LIMIT 4
ENV MEMORY_LIMIT 1G

# Health check
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
  CMD curl -f http://localhost:80 || exit 1

# Run the entrypoint script when the container launches
ENTRYPOINT ["/app/entrypoint.sh"]
