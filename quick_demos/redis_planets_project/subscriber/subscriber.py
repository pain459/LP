import redis
import time
from threading import Thread

def handle_message(message):
    print(f"Received message from {message['channel'].decode('utf-8')}: {message['data'].decode('utf-8')}")

def subscribe_to_channels():
    try:
        r = redis.Redis(host='redis', port=6379, db=0)
        planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']

        pubsub = r.pubsub()
        pubsub.subscribe(**{planet: handle_message for planet in planets})

        print("Subscribed to channels. Waiting for messages...")
        while True:
            message = pubsub.get_message()
            if message:
                handle_message(message)
            time.sleep(0.1)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)
        subscribe_to_channels()

if __name__ == "__main__":
    thread = Thread(target=subscribe_to_channels)
    thread.start()
    thread.join()
