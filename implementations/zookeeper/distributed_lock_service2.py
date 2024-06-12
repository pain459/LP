from kazoo.client import KazooClient
import time

def distributed_task():
    zk = KazooClient(hosts='127.0.0.1:2181,127.0.0.1:2182,127.0.0.1:2183')
    zk.start()

    lock = zk.Lock("/distributed_lock", "service-2")

    while True:
        print("Service 2 trying to acquire lock")
        with lock:  # This will block until the lock is acquired
            print("Service 2 acquired lock")
            # Simulate some work with the shared resource
            time.sleep(5)
            print("Service 2 releasing lock")
        
        # Sleep before trying to acquire the lock again
        time.sleep(3)

    zk.stop()

if __name__ == "__main__":
    distributed_task()
