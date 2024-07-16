from kafka import KafkaProducer
import time

# Kafka server (use the service name defined in docker-compose.yml)
KAFKA_SERVER = 'kafka:9092'
TOPIC = 'test-topic'

# Initialize Kafka producer
producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

def send_message(topic, message):
    producer.send(topic, value=message.encode('utf-8'))
    producer.flush()
    print(f"Sent message: {message}")

if __name__ == "__main__":
    while True:
        for _ in range(100):  # Send 100 messages at once
            send_message(TOPIC, 'Hello, Kafka!')
        time.sleep(1)  # Send batches every second
