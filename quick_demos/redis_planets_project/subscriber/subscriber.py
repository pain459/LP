import redis
import time
import logging
from threading import Thread

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

def subscribe_to_channels():
    try:
        r = redis.Redis(host='redis', port=6379, db=0)
        planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']

        pubsub = r.pubsub()
        pubsub.subscribe(**{planet: handle_message for planet in planets})

        logging.info("Subscribed to channels. Waiting for messages...")
        while True:
            message = pubsub.get_message()
            if message:
                handle_message(message)
            time.sleep(0.1)
    except Exception as e:
        logging.error(f"Error: {e}")
        time.sleep(5)
        subscribe_to_channels()

if __name__ == "__main__":
    thread = Thread(target=subscribe_to_channels)
    thread.start()
    thread.join()
