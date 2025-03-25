from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'logs',
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

for message in consumer:
    print(f"Received log: {message.value}")
