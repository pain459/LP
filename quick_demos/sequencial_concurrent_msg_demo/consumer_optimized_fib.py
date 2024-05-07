import pika
from concurrent.futures import ThreadPoolExecutor
import time

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def process_message(body):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    try:
        n = int(body.decode().split()[1])
        result = fibonacci(n)
        print(f" [x] Received {body} - Result: {result}")
    finally:
        connection.close()

def main():
    executor = ThreadPoolExecutor(max_workers=5)
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)
    channel.basic_qos(prefetch_count=1)

    def callback(ch, method, properties, body):
        executor.submit(process_message, body)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue='task_queue', on_message_callback=callback)

    start_time = time.time()
    print(' [*] Waiting for messages. To exit press CTRL+C')
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        executor.shutdown(wait=True)
        end_time = time.time()
        total_time = end_time - start_time
        print(f"Total time taken: {total_time} seconds")
        if not connection.is_closed:
            connection.close()

if __name__ == '__main__':
    main()
