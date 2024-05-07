import pika
from concurrent.futures import ThreadPoolExecutor
import time
import random

def process_message(body):
    print(f" [x] Received {body}")
    time.sleep(random.uniform(0.2, 0.3))
    print(" [x] Done")

def callback(ch, method, properties, body):
    executor.submit(process_message, body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

executor = ThreadPoolExecutor(max_workers=5)  # Adjust number of workers as needed

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
