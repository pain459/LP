import pika

# Connection parameters
connection_params = pika.ConnectionParameters('localhost')
queue_name = 'hello'


# Publish a message
def publish_message(message):
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.basic_publish(exchange='', routing_key=queue_name, body=message)
    print(" [x] Sent %r" % message)
    connection.close()


# Consume messages
def consume_messages():
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


# if __name__ == '__main__':
#     # Publish a message
#     publish_message('Hello, RabbitMQ!')
#
#     # Consume messages
#     consume_messages()
