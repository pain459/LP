import time
import logging
from concurrent.futures import ThreadPoolExecutor
from itertools import count
from collections import defaultdict

# Set up logging
logging.basicConfig(filename='task_log.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

class TaskQueue:
    def __init__(self, max_workers=10):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        self._counter = count()
        self.results = defaultdict(list)

    def submit_task(self, task_func, priority):
        """Submit a task along with its priority, adjusting delay inversely to priority."""
        count_value = next(self._counter)
        # Inverse the delay to reflect priority: Higher priority number = more delay
        delay = priority  # Simple direct relationship (Priority 1 = 1s, Priority 5 = 5s)
        time.sleep(delay)  # Delay submission based on priority
        # Submit task with delay already included in the start time
        future = self.executor.submit(self.run_task, task_func, priority, count_value, delay)
        future.add_done_callback(self.task_complete)

    def run_task(self, task_func, priority, count_value, initial_delay):
        """Run a task, measure its time including the initial delay, and log the result."""
        start_time = time.time() - initial_delay  # Adjust the start time back by the delay
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
