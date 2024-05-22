from flask import Flask, jsonify, request
import requests
import logging
import random
from math_tasks import matrix_multiplication, matrix_inversion, solve_linear_system

app = Flask(__name__)

# Setup logging
logging.basicConfig(filename='/app/logs/component1.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

math_functions = [matrix_multiplication, matrix_inversion, solve_linear_system]

def create_task():
    """Selects a random math function and prepares it as a task."""
    func = random.choice(math_functions)
    priority = random.choice(['P0', 'P1', 'P2', 'P3'])
    task_data = {"data": func(), "priority": priority}
    return task_data

@app.route('/generate_and_submit_task', methods=['POST'])
def generate_and_submit_task():
    task = create_task()
    url = 'http://component2:5001/submit_task'
    response = requests.post(url, json={'priority': task['priority'], 'data': task['data']})
    logging.info(f"Submitted task to Component 2: {task['data']} with priority {task['priority']} and response {response.status_code}")
    return jsonify({'status': 'Task submitted', 'response_code': response.status_code, 'priority': task['priority']})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
