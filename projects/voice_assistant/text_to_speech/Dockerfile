FROM python:3.10-slim

# Install necessary libraries
RUN pip install pyttsx3

# Copy application code
WORKDIR /app
COPY main.py .

# Run the text-to-speech service
CMD ["python", "main.py"]
