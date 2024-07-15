from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

def send_message(topic, message):
    producer.send(topic, value=message.encode('utf-8'))
    producer.flush()

send_message('test-topic', 'Hello, Kafka!')
