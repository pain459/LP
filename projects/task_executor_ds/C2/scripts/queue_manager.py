from flask import Flask, request, jsonify
import requests
from concurrent.futures import ThreadPoolExecutor
import logging
import queue

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, filename='/app/logs/c2.log', format='%(asctime)s - %(levelname)s - %(message)s')

# Priority queues for tasks
task_queues = {
    'P0': queue.PriorityQueue(),
    'P1': queue.PriorityQueue(),
    'P2': queue.PriorityQueue(),
    'P3': queue.PriorityQueue()
}

executor = ThreadPoolExecutor(max_workers=10)

def forward_task_to_c3(task_data):
    """Forwards the task to Component 3 and logs the response."""
    try:
        url = 'http://component3:5002/execute'
        response = requests.post(url, json=task_data)
        response.raise_for_status()  # Check for HTTP request errors
        logging.info(f"Successfully forwarded task to C3: {task_data} with response {response.status_code}")
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Error forwarding task to C3: {str(e)}")
        return {"status": "Failed to forward task", "error": str(e)}

@app.route('/submit_task', methods=['POST'])
def submit_task():
    data = request.json
    priority = data['priority']  # Assume 'P0' to 'P3'
    task_data = data['data']
    task_queues[priority].put(task_data)
    logging.info(f"Task received: {task_data} for priority queue {priority}")
    future = executor.submit(forward_task_to_c3, {'priority': priority, 'data': task_data})
    result = future.result()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
