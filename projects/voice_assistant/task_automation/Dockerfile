FROM python:3.10-slim

# Install necessary libraries
RUN pip install requests

# Copy application code
WORKDIR /app
COPY main.py .

# Run the task automation service
CMD ["python", "main.py"]
