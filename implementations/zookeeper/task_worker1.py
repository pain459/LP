from kazoo.client import KazooClient
import time

def process_task(task_id):
    print(f"Service 1 processing task {task_id}")
    time.sleep(10)  # Simulate task processing
    print(f"Service 1 finished task {task_id}")

def distributed_task_processing():
    zk = KazooClient(hosts='127.0.0.1:2181,127.0.0.1:2182,127.0.0.1:2183')
    zk.start()

    lock = zk.Lock("/task_lock", "service-1")

    while True:
        task_id = get_next_task()  # Function to get the next task from the queue
        if task_id is None:
            print("Service 1: No more tasks")
            break

        print("Service 1 trying to acquire lock for task", task_id)
        with lock:  # This will block until the lock is acquired
            process_task(task_id)

        # Sleep before trying to acquire the lock for the next task
        time.sleep(1)

    zk.stop()

def get_next_task():
    # time.sleep(5)
    # Simulate getting the next task from a queue (return None when no tasks are left)
    return 1  # For demonstration, always return task 1

if __name__ == "__main__":
    distributed_task_processing()
