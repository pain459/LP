import pika
import time


def main():
    # Connect to RabbitMQ
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq')
    )
    channel = connection.channel()


    # Create a queue
    channel.queue_declare(queue='logs_queue')

    count = 0
    while True:
        message = f'Log event number {count}'
        channel.basic_publish(exchange='',
                              routing_key='logs_queue',
                              body=message)
        print(f'[Producer] Sent: {message}')
        count += 1
        time.sleep(3)  # Sleep to simulate periodic events


if __name__ == '__main__':
    main() 