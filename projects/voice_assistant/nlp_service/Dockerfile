FROM python:3.10-slim

# Install necessary libraries
RUN pip install flask

# Copy application code
WORKDIR /app
COPY main.py .

# Run the NLP service
CMD ["python", "main.py"]
