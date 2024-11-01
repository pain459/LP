FROM python:3.10-slim

# Install necessary libraries
RUN pip install requests

# Copy application code
WORKDIR /app
COPY main.py .

# Run the orchestration script
CMD ["python", "main.py"]
