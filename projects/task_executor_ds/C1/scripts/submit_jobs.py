import requests
from apscheduler.schedulers.background import BackgroundScheduler
import random
import time
from requests.exceptions import ConnectionError

def create_task():
    """Simulates creating a task with varying complexity."""
    # Define a simple task dictionary
    complexity_level = random.choice(['low', 'medium', 'high'])
    task_data = f"Process data with {complexity_level} complexity"
    priority = {'low': 5, 'medium': 3, 'high': 1}[complexity_level]
    return {'data': task_data, 'priority': priority}

def submit_task():
    """Submits a task to Component 2."""
    task = create_task()
    response = requests.post('http://localhost:5001/submit_task', json=task)
    print(f"Submitted task: {task['data']} with priority {task['priority']}, response: {response.status_code}")

def start_job_submission():
    """Starts the scheduler to submit jobs periodically."""
    scheduler = BackgroundScheduler()
    scheduler.add_job(submit_task, 'interval', seconds=10)  # Adjust the interval as needed
    scheduler.start()

    # Keep the script running
    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()

if __name__ == '__main__':
    start_job_submission()
