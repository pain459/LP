import time
import random
import hazelcast

def main():
    # Connect to the Hazelcast cluster using the service name "hazelcast"
    client = hazelcast.HazelcastClient(cluster_members=["hazelcast:5701"])
    topic = client.get_topic("sensor_readings").blocking()

    # Each sensor gets a unique (random) sensor_id for simulation
    sensor_id = random.randint(1, 1000)
    print(f"Sensor {sensor_id} started and publishing readings...")

    while True:
        # Simulate a temperature reading between 20.0 and 30.0 degrees Celsius
        reading = random.uniform(20.0, 30.0)
        message = {"sensor_id": sensor_id, "reading": reading, "timestamp": time.time()}
        topic.publish(message)
        print(f"Sensor {sensor_id} published reading: {reading:.2f}")
        time.sleep(2)  # Publish a reading every 2 seconds

if __name__ == "__main__":
    main()
