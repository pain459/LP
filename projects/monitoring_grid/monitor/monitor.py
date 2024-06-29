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
            dependent_up = check_api(api['dependent'])
            potential_up = check_api(api['potential'])
            
            if not genesis_up:
                service_status[api['name']] = {
                    'genesis': 'DOWN',
                    'dependent': 'DEGRADED',
                    'potential': 'DEGRADED'
                }
            elif not dependent_up:
                service_status[api['name']] = {
                    'genesis': 'UP',
                    'dependent': 'DOWN',
                    'potential': 'DEGRADED'
                }
            else:
                service_status[api['name']] = {
                    'genesis': 'UP',
                    'dependent': 'UP',
                    'potential': potential_up and 'UP' or 'DOWN'
                }
        time.sleep(30)

if __name__ == "__main__":
    service_status = {api['name']: {'genesis': 'UNKNOWN', 'dependent': 'UNKNOWN', 'potential': 'UNKNOWN'} for api in api_config['apis']}
    import threading
    monitor_thread = threading.Thread(target=monitor_apis)
    monitor_thread.start()
    app.run(host='0.0.0.0', port=5000)
