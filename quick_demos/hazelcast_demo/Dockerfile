FROM python:3.9-slim

WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files
COPY . .

# Default command (can be overridden in docker-compose)
CMD ["python", "sensor.py"]
