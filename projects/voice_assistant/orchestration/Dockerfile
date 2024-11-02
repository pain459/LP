FROM python:3.10-slim

# Install required dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
WORKDIR /app
COPY main.py .

# Run the orchestration script
CMD ["python", "main.py"]
