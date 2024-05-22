from flask import Flask, jsonify, request
import requests
import logging
import random
from math_tasks import (
    recursive_matrix_multiplication,
    recursive_matrix_inversion,
    recursive_solve_linear_system,
    describe_task
)

app = Flask(__name__)

# Setup logging
logging.basicConfig(filename='/app/logs/component1.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

math_functions = [
    (recursive_matrix_multiplication, 'matrix multiplication'),
    (recursive_matrix_inversion, 'matrix inversion'),
    (recursive_solve_linear_system, 'solve linear system')
]

def create_task():
    """Selects a random recursive math function and prepares it as a task."""
    func, description = random.choice(math_functions)
    size = 50  # Standard size for all tasks
    depth = 3  # Depth of recursion
    result = func(size=size, depth=depth)
    task_data = {
        "data": describe_task(result, size, depth),
        "priority": random.choice(['P0', 'P1', 'P2', 'P3'])
    }
    return task_data

@app.route('/generate_and_submit_task', methods=['POST'])
def generate_and_submit_task():
    task = create_task()
    url = 'http://component2:5001/submit_task'
    response = requests.post(url, json={'priority': task['priority'], 'data': task['data']})
    logging.info(f"Submitted task to Component 2: {task['data']} with priority {task['priority']} and response {response.status_code}")
    return jsonify({'status': 'Task submitted', 'response_code': response.status_code, 'priority': task['priority']})

@app.route('/test_math', methods=['GET'])
def test_math_operations():
    try:
        mult_result = recursive_matrix_multiplication(size=10, depth=1)
        inv_result = recursive_matrix_inversion(size=10, depth=1)
        sol_result = recursive_solve_linear_system(size=10, depth=1)
        return jsonify({
            'status': 'success',
            'matrix_multiplication': str(mult_result),
            'matrix_inversion': str(inv_result),
            'solve_linear_system': str(sol_result)
        })
    except Exception as e:
        logging.error(f"Error during math operations: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
