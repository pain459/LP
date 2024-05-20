import time
import logging
from concurrent.futures import ThreadPoolExecutor
from itertools import count
import random
from collections import defaultdict

# Set up logging
logging.basicConfig(filename='task_log.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

class TaskQueue:
    def __init__(self, max_workers=10):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        self._counter = count()
        self.results = defaultdict(list)

    def submit_task(self, task_func, priority):
        """Submit a task along with its priority."""
        count_value = next(self._counter)
        delay = (5 - priority) * 0.1
        time.sleep(delay)  # Simulate CPU time allocation by priority
        future = self.executor.submit(self.run_task, task_func, priority, count_value)
        future.add_done_callback(self.task_complete)

    def run_task(self, task_func, priority, count_value):
        """Run a task, measure its time, and log the result."""
        start_time = time.time()
        result = task_func()
        end_time = time.time()
        duration = end_time - start_time
        return priority, count_value, duration, result

    def task_complete(self, future):
        """Handle task completion, logging, and result aggregation."""
        priority, count_value, duration, result = future.result()
        self.results[priority].append(duration)
        logging.info(f'Task {count_value} with priority {priority} completed in {duration:.2f} seconds')

    def shutdown(self):
        """Shut down the executor and print the report."""
        self.executor.shutdown(wait=True)
        self.print_report()

    def print_report(self):
        """Print a summary report of task performance by priority."""
        for priority, durations in sorted(self.results.items()):
            total_time = sum(durations)
            average_time = total_time / len(durations)
            logging.info(f'Priority {priority}: Average execution time: {average_time:.2f} seconds, Total execution time: {total_time:.2f} seconds')
