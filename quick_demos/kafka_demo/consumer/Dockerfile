FROM python:3.10-slim

# Install netcat for waiting on Kafka
RUN apt-get update && apt-get install -y netcat-traditional && apt-get clean

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY consumer.py .
COPY wait-for-kafka.sh .
RUN chmod +x wait-for-kafka.sh

CMD ["./wait-for-kafka.sh"]
