import threading
from task_queue import TaskQueue  # Assuming the priority queue code is in task_queue.py
from tasks import calculate, ping, reverse_string, sum_numbers  # Importing from 1_tasks.py

def main():
    task_queue = TaskQueue()

    # Submitting tasks with specified priorities
    task_queue.submit_task(calculate, 1)  # Priority: 1 (High)
    task_queue.submit_task(ping, 2)       # Priority: 2
    task_queue.submit_task(reverse_string, 3)  # Priority: 3
    task_queue.submit_task(sum_numbers, 4)  # Priority: 4 (Low)

    # Start processing tasks in a separate thread
    processing_thread = threading.Thread(target=task_queue.start_processing)
    processing_thread.start()
    processing_thread.join()

if __name__ == '__main__':
    main()
