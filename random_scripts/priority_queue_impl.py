import queue
import threading
import time
import random

# Create priority queues
priority_queues = {
    1: queue.PriorityQueue(),
    2: queue.PriorityQueue(),
    3: queue.PriorityQueue(),
    4: queue.PriorityQueue()
}

# Message source function
def message_source(priority, interval=1):
    task_count = 1
    while True:
        task = f"Task {task_count} for priority {priority}"
        priority_queues[priority].put(task)
        print(f"Enqueued: {task}")
        task_count += 1
        time.sleep(interval)

# Start message sources for each priority queue
for priority in range(1, 5):
    threading.Thread(target=message_source, args=(priority, random.uniform(1, 3)), daemon=True).start()

# Backend worker function
def backend_worker():
    weights = {1: 5, 2: 3, 3: 2, 4: 1}  # Adjust weights as needed
    total_weight = sum(weights.values())
    
    while True:
        for priority in sorted(priority_queues.keys()):
            weight = weights[priority]
            for _ in range(weight):
                if not priority_queues[priority].empty():
                    task = priority_queues[priority].get()
                    process_task(task, priority)
                    time.sleep(random.uniform(0.1, 0.5))  # Simulate task processing time

def process_task(task, priority):
    print(f"Processing {task} from priority {priority}")
    with open("task_log.txt", "a") as log_file:
        log_file.write(f"Completed {task} from priority {priority}\n")

# Start the backend worker in a separate thread
worker_thread = threading.Thread(target=backend_worker, daemon=True)
worker_thread.start()

# Keep the main thread alive to let daemon threads run
while True:
    time.sleep(1)
