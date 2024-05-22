from flask import Flask, request, jsonify
import requests
import logging
import random

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='/app/logs/component1.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def create_task():
    """Simulates creating a task with data."""
    # Example task data creation
    task_data = {"data": f"Task data {random.randint(1, 100)}"}
    return task_data

@app.route('/generate_and_submit_task', methods=['POST'])
def generate_and_submit_task():
    """Generates a task and submits it to Component 2."""
    task_data = create_task()
    # URL for Component 2
    url = 'http://component2:5001/submit_task'
    # Set priority to 'Q2'
    response = requests.post(url, json={'priority': 'P2', 'data': task_data['data']})
    logging.info(f"Submitted task to Component 2: {task_data['data']} with response {response.status_code}")
    return jsonify({'status': 'Task submitted', 'response_code': response.status_code})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
