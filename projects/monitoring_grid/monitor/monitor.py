import requests
import time
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, jsonify

# Configuration for logging
log_handler = RotatingFileHandler('monitor.log', maxBytes=104857600, backupCount=5)
log_handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
logger = logging.getLogger('MonitorLogger')
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

# Read API endpoints from the file
api_endpoints = []
with open('endpoints.txt', 'r') as f:
    for line in f:
        name, port = line.strip().split(':')
        api_endpoints.append({"name": name, "port": int(port)})

# Dictionary to hold the status of services
service_status = {api["name"]: "DOWN" for api in api_endpoints}

# Flask app setup
app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    return jsonify({'services': service_status})

def monitor_apis():
    while True:
        for api in api_endpoints:
            url = f'http://{api["name"]}:{api["port"]}'
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    service_status[api["name"]] = "UP"
                else:
                    service_status[api["name"]] = "DOWN"
                logger.info(f'{api["name"]}_{api["port"]}: {response.status_code}')
            except Exception as e:
                service_status[api["name"]] = "DOWN"
                logger.error(f'{api["name"]}_{api["port"]}: {str(e)}')
        time.sleep(30)

if __name__ == "__main__":
    import threading
    monitor_thread = threading.Thread(target=monitor_apis)
    monitor_thread.start()
    app.run(host='0.0.0.0', port=5000)
