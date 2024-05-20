import threading
from task_queue import TaskQueue
from tasks import calculate, ping, reverse_string, sum_numbers
import time

def main():
    task_queue = TaskQueue()

    # Submitting tasks with specified priorities
    task_queue.submit_task(calculate, 1)  # Priority: 1 (High)
    task_queue.submit_task(ping, 2)       # Priority: 2
    task_queue.submit_task(reverse_string, 3)  # Priority: 3
    task_queue.submit_task(sum_numbers, 4)  # Priority: 4 (Low)

    # Start processing tasks with 3 worker threads
    task_queue.start_processing(3)

    # Simulate running the system for some time
    time.sleep(15)

    # Stop the worker threads
    task_queue.stop_workers()

    # Wait for all worker threads to finish
    task_queue.join_workers()

if __name__ == '__main__':
    main()
