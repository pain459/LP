import requests
import time
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, jsonify
import yaml

# Configuration for logging
log_handler = RotatingFileHandler('monitor.log', maxBytes=104857600, backupCount=5)
log_handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
logger = logging.getLogger('MonitorLogger')
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

# Read API endpoints from the YAML file
with open('endpoints.yaml', 'r') as f:
    api_config = yaml.safe_load(f)

# Flask app setup
app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    return jsonify({'services': service_status})

def check_api(api):
    url = f"http://{api['host']}:{api['port']}"
    try:
        response = requests.get(url)
        return response.status_code == 200
    except Exception as e:
        logger.error(f"Error checking {url}: {str(e)}")
        return False

def monitor_apis():
    global service_status
    while True:
        for api in api_config['apis']:
            genesis_up = check_api(api['genesis'])
            dependents_status = [check_api(dep) for dep in api.get('dependents', [])]
            potentials_status = [check_api(pot) for pot in api.get('potentials', [])]

            if not genesis_up:
                service_status[api['name']] = {
                    'genesis': 'DOWN',
                    'dependents': 'DEGRADED',
                    'potentials': 'DEGRADED'
                }
            elif any(not dep for dep in dependents_status):
                service_status[api['name']] = {
                    'genesis': 'UP',
                    'dependents': 'DOWN',
                    'potentials': 'DEGRADED'
                }
            elif any(not pot for pot in potentials_status):
                service_status[api['name']] = {
                    'genesis': 'UP',
                    'dependents': 'UP',
                    'potentials': 'DEGRADED'
                }
            else:
                service_status[api['name']] = {
                    'genesis': 'UP',
                    'dependents': 'UP',
                    'potentials': 'UP'
                }
        time.sleep(30)

if __name__ == "__main__":
    service_status = {api['name']: {'genesis': 'UNKNOWN', 'dependents': 'UNKNOWN', 'potentials': 'UNKNOWN'} for api in api_config['apis']}
    import threading
    monitor_thread = threading.Thread(target=monitor_apis)
    monitor_thread.start()
    app.run(host='0.0.0.0', port=5000)
