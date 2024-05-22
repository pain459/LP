from flask import Flask, request, jsonify
import requests
from concurrent.futures import ThreadPoolExecutor
import queue
import logging

app = Flask(__name__)

# Configure logging to file in the specified log directory
logging.basicConfig(filename='/app/logs/component2.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


# Log function to provide detailed operation logs
def log_task_activity(activity, priority, task_data, response_status=None):
    if response_status:
        logging.info(f"{activity} | Priority: {priority} | Task: {task_data} | Response Status: {response_status}")
    else:
        logging.info(f"{activity} | Priority: {priority} | Task: {task_data}")


# Priority queues dictionary
queues = {
    'P0': queue.PriorityQueue(),
    'P1': queue.PriorityQueue(),
    'P2': queue.PriorityQueue(),
    'P3': queue.PriorityQueue()
}

# Thread pool executor
executor = ThreadPoolExecutor(max_workers=10)

def process_task(priority, task_data):
    """Function to process and forward tasks to Component 3."""
    logging.info(f"Processing task with priority {priority}: {task_data}")
    response = requests.post('http://component3:5002/execute_task', json={'data': task_data})
    logging.info(f"Task forwarded to Component 3 with response: {response.status_code}")

def task_handler():
    """Function to handle tasks from queues based on priority."""
    while True:
        # Check queues starting from highest priority
        for priority in sorted(queues.keys()):
            try:
                task_data = queues[priority].get_nowait()
                executor.submit(process_task, priority, task_data)
                queues[priority].task_done()
            except queue.Empty:
                continue

@app.route('/submit_task', methods=['POST'])
def submit_task():
    data = request.json
    priority = data['priority']  # Assume 'P0' to 'P3'
    task_data = data['data']
    queues[priority].put(task_data)
    logging.info(f"Task received: {task_data} with priority {priority}")
    return jsonify({'status': 'Task queued successfully'})


@app.route('/health', methods=['GET'])
def health():
    return "Component 2 is healthy", 200


if __name__ == '__main__':
    # Example log entry
    logging.info("Component 2 starting up...")
    app.run(debug=True, host='0.0.0.0', port=5001)
