# To be deprecated

from flask import Flask, request, jsonify
import time
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)
executor = ThreadPoolExecutor(max_workers=4)

def process_task(priority, task_data):
    """Simulate task processing with delay based on priority."""
    delay = (5 - priority) * 2  # Higher priority, less delay
    time.sleep(10 - delay)
    # code to component 3
    print(f"Processed task with priority {priority}: {task_data} after {delay} seconds delay")
    return f"Task processed with delay of {delay} seconds"

@app.route('/submit_task', methods=['POST'])
def submit_task():
    data = request.json
    priority = data['priority']
    task_data = data['data']
    executor.submit(process_task, priority, task_data)
    return jsonify({'status': 'Task submitted successfully', 'priority': priority})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
