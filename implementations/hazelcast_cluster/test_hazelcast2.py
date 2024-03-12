import hazelcast


def map_operations(client):
    my_map = client.get_map("my-distributed-map").blocking()

    # Put some key-value pairs into the distributed map
    my_map.put("key1", "value1")
    my_map.put("key2", "value2")
    my_map.put("key3", "value3")

    # Retrieve and print values from the map
    print("Value for key1:", my_map.get("key1"))
    print("Value for key2:", my_map.get("key2"))
    print("Value for key3:", my_map.get("key3"))


def atomic_operations(client):
    atomic_long = client.get_atomic_long("my-atomic-long").blocking()

    # Increment the atomic long value
    print("Current value of atomic long:", atomic_long.get())
    atomic_long.increment_and_get()
    print("Incremented value of atomic long:", atomic_long.get())


def distributed_locks(client):
    my_lock = client.get_lock("my-distributed-lock").blocking()

    # Acquire the lock and perform some critical operations
    my_lock.lock()
    print("Lock acquired successfully")

    # Simulate critical section
    try:
        # Perform critical operations here
        pass
    finally:
        # Release the lock when done
        my_lock.unlock()
        print("Lock released")


def main():
    config = hazelcast.ClientConfig()
    config.network_config.addresses.append("localhost:5701")
    config.network_config.addresses.append("localhost:5702")
    config.network_config.addresses.append("localhost:5703")

    client = hazelcast.HazelcastClient(config)
    print("Connected to Hazelcast cluster")

    # Perform map operations
    print("\nMap Operations:")
    map_operations(client)

    # Perform atomic operations
    print("\nAtomic Operations:")
    atomic_operations(client)

    # Perform distributed locks
    print("\nDistributed Locks:")
    distributed_locks(client)

    # Shutdown the client and disconnect from the cluster
    client.shutdown()
    print("\nDisconnected from Hazelcast cluster")


if __name__ == "__main__":
    main()
