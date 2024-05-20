import queue
import threading
from tasks import calculate, ping, reverse_string, sum_numbers 

class TaskQueue:
    def __init__(self):
        self.task_queue = queue.PriorityQueue()

    def submit_task(self, task_func, priority):
        """Submit a task along with its priority."""
        self.task_queue.put((priority, task_func))

    def start_processing(self):
        """Process tasks in order of their priorities."""
        while not self.task_queue.empty():
            priority, task_func = self.task_queue.get()
            print(f"Processing task with priority: {priority}")
            task_func()
            self.task_queue.task_done()

# Example usage
task_queue = TaskQueue()
task_queue.submit_task(calculate, 1)  # Lower number -> Higher priority
task_queue.submit_task(ping, 2)
task_queue.submit_task(reverse_string, 3)
task_queue.submit_task(sum_numbers, 4)

# In a real scenario, start_processing would be run in a separate thread or process.
processing_thread = threading.Thread(target=task_queue.start_processing)
processing_thread.start()
processing_thread.join()
