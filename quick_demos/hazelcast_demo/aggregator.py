import time
import hazelcast

def main():
    # Connect to the Hazelcast cluster
    client = hazelcast.HazelcastClient(cluster_members=["hazelcast:5701"])
    topic = client.get_topic("sensor_readings")

    total = 0.0
    count = 0

    # Listener function that processes incoming sensor messages
    def listener(message):
        nonlocal total, count
        reading = message.message_object.get("reading")
        total += reading
        count += 1
        avg = total / count
        print(f"Received reading: {reading:.2f}, running average: {avg:.2f}")

    # Register the listener on the distributed topic
    topic.add_listener(on_message=listener)

    print("Aggregator started and waiting for sensor readings...")
    # Keep the aggregator running indefinitely
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
