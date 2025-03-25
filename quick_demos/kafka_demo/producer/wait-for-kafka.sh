#!/bin/bash

# Wait until Kafka is available
KAFKA_HOST=kafka
KAFKA_PORT=9092

echo "Waiting for Kafka to be available at $KAFKA_HOST:$KAFKA_PORT..."

while ! nc -z $KAFKA_HOST $KAFKA_PORT; do
  sleep 1
done

echo "Kafka is up! Running app..."
python producer.py
