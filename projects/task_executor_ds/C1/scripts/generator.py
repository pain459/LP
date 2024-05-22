from flask import Flask, jsonify
import requests
import logging
import random

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='/app/logs/component1.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def create_task():
    """Simulates creating a task with random priority and data."""
    priorities = ['P0', 'P1', 'P2', 'P3']
    priority = random.choice(priorities)
    task_data = {"data": f"Task data {random.randint(1, 100)}", "priority": priority}
    return task_data

@app.route('/generate_and_submit_task', methods=['POST'])
def generate_and_submit_task():
    """Generates a task and submits it to Component 2."""
    task = create_task()
    url = 'http://component2:5001/submit_task'
    response = requests.post(url, json={'priority': task['priority'], 'data': task['data']})
    logging.info(f"Submitted task to Component 2: {task['data']} with priority {task['priority']} and response {response.status_code}")
    return jsonify({'status': 'Task submitted', 'response_code': response.status_code, 'priority': task['priority']})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
