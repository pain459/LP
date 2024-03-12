import hazelcast

def main():
    # Connect to the Hazelcast cluster
    config = hazelcast.ClientConfig()
    config.network_config.addresses.append("localhost:5701")
    config.network_config.addresses.append("localhost:5702")
    config.network_config.addresses.append("localhost:5703")

    client = hazelcast.HazelcastClient(config)
    print("Connected to Hazelcast cluster")

    # Get a distributed map from the cluster
    my_map = client.get_map("my-distributed-map").blocking()

    # Perform some operations on the map
    my_map.put("key1", "value1")
    my_map.put("key2", "value2")
    print("Added values to the distributed map")

    # Retrieve and print values from the map
    print("Value for key1:", my_map.get("key1"))
    print("Value for key2:", my_map.get("key2"))

    # Shutdown the client and disconnect from the cluster
    client.shutdown()
    print("Disconnected from Hazelcast cluster")


if __name__ == "__main__":
    main()
