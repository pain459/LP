import redis
import time
import logging

logging.basicConfig(level=logging.INFO)

def handle_message(message):
    channel = message['channel']
    data = message['data']

    # Check if the message is of type 'message'
    if message['type'] == 'message':
        if isinstance(channel, bytes):
            channel = channel.decode('utf-8')
        if isinstance(data, bytes):
            data = data.decode('utf-8')

        logging.info(f"Received message from {channel}: {data}")
    else:
        logging.info(f"Received non-message type: {message}")

def subscribe_to_channel(channel):
    try:
        r = redis.Redis(host='redis', port=6379, db=0)  # Use 'redis' as the host
        pubsub = r.pubsub()
        pubsub.subscribe(**{channel: handle_message})

        logging.info(f"Subscribed to channel '{channel}'. Waiting for messages...")
        while True:
            message = pubsub.get_message()
            if message:
                handle_message(message)
            time.sleep(0.1)
    except Exception as e:
        logging.error(f"Error: {e}")
        time.sleep(5)
        subscribe_to_channel(channel)

if __name__ == "__main__":
    channel = input("Enter the channel name you want to subscribe to: ")
    subscribe_to_channel(channel)
