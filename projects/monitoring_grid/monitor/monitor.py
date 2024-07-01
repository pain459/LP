import os
import requests
import time
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, jsonify
from flask_cors import CORS
import yaml
from collections import OrderedDict

# Configuration for logging
log_handler = RotatingFileHandler('monitor.log', maxBytes=104857600, backupCount=5)
log_handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
logger = logging.getLogger('MonitorLogger')
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

# Read API endpoints from the services directory    
services_dir = 'services'
api_configs = []
for filename in os.listdir(services_dir):
    if filename.endswith('.yaml'):
        with open(os.path.join(services_dir, filename), 'r') as f:
            api_configs.append(yaml.safe_load(f))

# Flask app setup
app = Flask(__name__)
CORS(app, resources={r"/status": {"origins": "*"}})  # Allow all origins for the /status endpoint

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
        for api_config in api_configs:
            name = api_config['genesis']['host']
            genesis_up = check_api(api_config['genesis'])
            dependents_status = [check_api(dep) for dep in api_config.get('dependents', [])]
            potentials_status = [check_api(pot) for pot in api_config.get('potentials', [])]

            registered_services = OrderedDict([
                ('genesis', f"{api_config['genesis']['host']}:{api_config['genesis']['port']}"),
                ('dependents', [f"{dep['host']}:{dep['port']}" for dep in api_config.get('dependents', [])]),
                ('potentials', [f"{pot['host']}:{pot['port']}" for pot in api_config.get('potentials', [])])
            ])

            if not genesis_up:
                service_status[name] = OrderedDict([
                    ('genesis', 'DOWN'),
                    ('dependents', 'DEGRADED'),
                    ('potentials', 'DEGRADED'),
                    ('registered_services', registered_services)
                ])
            elif any(not dep for dep in dependents_status):
                service_status[name] = OrderedDict([
                    ('genesis', 'UP'),
                    ('dependents', 'DOWN'),
                    ('potentials', 'DEGRADED'),
                    ('registered_services', registered_services)
                ])
            elif any(not pot for pot in potentials_status):
                service_status[name] = OrderedDict([
                    ('genesis', 'UP'),
                    ('dependents', 'UP'),
                    ('potentials', 'DEGRADED'),
                    ('registered_services', registered_services)
                ])
            else:
                service_status[name] = OrderedDict([
                    ('genesis', 'UP'),
                    ('dependents', 'UP'),
                    ('potentials', 'UP'),
                    ('registered_services', registered_services)
                ])
        time.sleep(30)

if __name__ == "__main__":
    service_status = OrderedDict()
    for api in api_configs:
        registered_services = OrderedDict([
            ('genesis', f"{api['genesis']['host']}:{api['genesis']['port']}"),
            ('dependents', [f"{dep['host']}:{dep['port']}" for dep in api.get('dependents', [])]),
            ('potentials', [f"{pot['host']}:{pot['port']}" for pot in api.get('potentials', [])])
        ])
        service_status[api['genesis']['host']] = OrderedDict([
            ('genesis', 'UNKNOWN'),
            ('dependents', 'UNKNOWN'),
            ('potentials', 'UNKNOWN'),
            ('registered_services', registered_services)
        ])

    import threading
    monitor_thread = threading.Thread(target=monitor_apis)
    monitor_thread.start()
    app.run(host='0.0.0.0', port=5000)
