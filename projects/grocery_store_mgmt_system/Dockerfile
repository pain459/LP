# Use an official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /sku_db

# Install SQLite CLI and Python dependencies
RUN apt-get update && apt-get install -y sqlite3 && rm -rf /var/lib/apt/lists/*

# Copy application files
COPY ./sku_db /sku_db

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create volume for SQLite persistence
VOLUME /data

# Run the Python app
CMD ["python", "main.py"]
