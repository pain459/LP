import requests
import random
import time
import logging

# Configure logging
logging.basicConfig(filename='/app/logs/component1.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def create_task():
    """Simulates the creation of a complex task with random complexity."""
    complexity = random.choice(['low', 'medium', 'high'])
    task_data = f"Task with {complexity} complexity"
    priority = {'low': 5, 'medium': 3, 'high': 1}[complexity]
    logging.info(f"Created task: {task_data} with priority {priority}")
    return task_data, priority

def submit_task(task_data, priority):
    """Submits a task to Component 2 with the designated priority, with retry mechanism."""
    url = 'http://component2:5001/submit_task'
    data = {'data': task_data, 'priority': priority}
    retries = 5
    wait = 5  # seconds to wait before retrying
    for attempt in range(retries):
        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                logging.info(f"Successfully submitted task: {task_data} to Component 2")
                return response
            else:
                logging.warning(f"Failed to submit task, status code: {response.status_code}")
        except requests.exceptions.ConnectionError as e:
            logging.error(f"Connection failed: {e}, retrying in {wait} seconds...")
            time.sleep(wait)
    logging.error(f"Failed to submit task after {retries} attempts")
    return None

if __name__ == '__main__':
    while True:
        task_data, priority = create_task()
        response = submit_task(task_data, priority)
        time.sleep(10)  # Interval between task generations
