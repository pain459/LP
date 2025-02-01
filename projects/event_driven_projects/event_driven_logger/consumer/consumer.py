import pika

def callback(ch, method, properties, body):
    print(f'[Consumer] Received: {body.decode()}')


def main():
    # Connect to RabbitMQ
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq')
    )
    channel = connection.channel()

    # Declare queue to listen to
    channel.queue_declare(queue='logs_queue')

    channel.basic.consume(
        queue='logs_queue',
        on_mesage_callback=callback,
        auto_ack=True
    )

    print('[Consumer] waiting for messages. To exit press CTRL+C')


if __name__=='__main__':
    main()
