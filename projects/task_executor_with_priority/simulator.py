from task_queue import TaskQueue
from tasks import calculate, ping, reverse_string, sum_numbers
import random
import time

def main():
    task_queue = TaskQueue(max_workers=5)

    tasks = [calculate, ping, reverse_string, sum_numbers]
    num_jobs = 10

    # Submitting a swarm of jobs for each task type
    for _ in range(num_jobs):
        for task in tasks:
            priority = random.randint(1, 5)
            task_queue.submit_task(task, priority)

    # Allow time for some tasks to complete
    time.sleep(10)

    # Shutdown the task queue and print the report
    task_queue.shutdown()

if __name__ == '__main__':
    main()
