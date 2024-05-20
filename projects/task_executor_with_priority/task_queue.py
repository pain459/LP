import queue
import threading
import time

class TaskQueue:
    def __init__(self):
        self.task_queue = queue.PriorityQueue()
        self.workers = []

    def submit_task(self, task_func, priority):
        """Submit a task along with its priority."""
        self.task_queue.put((priority, task_func))

    def worker(self):
        """Worker thread to process tasks."""
        while True:
            priority, task_func = self.task_queue.get()
            if task_func is None:  # Sentinel value to stop processing
                self.task_queue.task_done()
                break
            start_time = time.time()
            print(f"Processing task with priority: {priority}")
            task_func()
            end_time = time.time()
            duration = end_time - start_time
            print(f"Task with priority {priority} completed in {duration:.2f} seconds")
            self.task_queue.task_done()

    def start_processing(self, num_workers):
        """Start the specified number of worker threads."""
        for _ in range(num_workers):
            thread = threading.Thread(target=self.worker)
            thread.start()
            self.workers.append(thread)

    def stop_workers(self):
        """Stop all workers by inserting a sentinel None task for each worker."""
        for _ in self.workers:
            self.submit_task(None, 0)

    def join_workers(self):
        """Wait for all worker threads to finish."""
        for worker in self.workers:
            worker.join()
