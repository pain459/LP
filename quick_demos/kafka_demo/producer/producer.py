from kafka import KafkaProducer
import time
import json
import random

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

log_levels = ['INFO', 'DEBUG', 'WARNING', 'ERROR']

while True:
    log = {
        'level': random.choice(log_levels),
        'message': 'This is a log message',
        'timestamp': time.time()
    }
    print(f"Sending: {log}")
    producer.send('logs', log)
    time.sleep(2)
