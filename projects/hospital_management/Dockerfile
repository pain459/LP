# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set environment variables
ENV FLASK_APP=run.py
ENV FLASK_ENV=development
ENV PYTHONPATH=/app

# Expose the port the app runs on
EXPOSE 5000

# Run the entrypoint script
ENTRYPOINT ["./entrypoint.sh"]
