FROM python:3.9-slim

WORKDIR /app

# Install necessary packages
RUN apt-get update && apt-get install -y curl

# Copy the requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy scripts to container
COPY scripts/ .

# Setup log directory
RUN mkdir /app/logs
VOLUME /app/logs

CMD ["python", "generator.py"]
