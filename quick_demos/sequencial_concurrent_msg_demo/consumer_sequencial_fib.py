import pika
import time

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def callback(ch, method, properties, body, messages_processed, total_messages):
    print(f" [x] Received {body}")
    n = int(body.decode().split()[1])
    result = fibonacci(n)
    print(f" [x] Result {result}")
    ch.basic_ack(delivery_tag=method.delivery_tag)
    messages_processed[0] += 1
    if messages_processed[0] == total_messages:
        end_time = time.time()
        total_time = end_time - start_time
        print(f"Total time taken: {total_time} seconds")
        connection.close()

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
channel.basic_qos(prefetch_count=1)

total_messages = 1000  # Set this to the number of messages expected to process
messages_processed = [0]  # List to allow modifications within callback
start_time = time.time()

channel.basic_consume(queue='task_queue', on_message_callback=lambda ch, method, properties, body: callback(ch, method, properties, body, messages_processed, total_messages))

print(' [*] Waiting for messages. To exit press CTRL+C')
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
    connection.close()
