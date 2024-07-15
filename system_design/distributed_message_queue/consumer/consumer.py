from kafka import KafkaConsumer

# Kafka server (use the service name defined in docker-compose.yml)
KAFKA_SERVER = 'kafka:9092'
TOPIC = 'test-topic'

# Initialize Kafka consumer
consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=KAFKA_SERVER,
    auto_offset_reset='earliest',  # Start from the earliest message
    enable_auto_commit=True,
    group_id='my-group')

print("Consumer started. Waiting for messages...")

for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}")
