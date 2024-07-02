import os
import requests
import time
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, jsonify
from flask_cors import CORS
import yaml
from collections import OrderedDict
import json

# Configuration for logging
log_handler = RotatingFileHandler('monitor.log', maxBytes=104857600, backupCount=5)
log_handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
logger = logging.getLogger('MonitorLogger')
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

# Determine the file path for endpoints.yaml
try:
    base_dir = os.path.dirname(__file__)
except NameError:
    base_dir = os.getcwd()

file_path = os.path.join(base_dir, 'endpoints.yaml')
output_file_path = os.path.join(base_dir, 'api_configs.json')

def load_yaml_file(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def transform_api_data(data):
    transformed_data = []
    for api in data.get('apis', []):
        transformed_data.append({
            'name': api.get('name', api['genesis']['host']),
            'genesis': api.get('genesis', {}),
            'dependents': api.get('dependents', []),
            'potentials': api.get('potentials', [])
        })
    return transformed_data

def save_to_json_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

try:
    # Load the YAML data from the specified file
    yaml_data = load_yaml_file(file_path)
    
    # Check if the 'apis' key is present in the loaded YAML data
    if 'apis' in yaml_data:
        # Transform the loaded data
        api_configs = transform_api_data(yaml_data)
        
        # Save the transformed data to a JSON file
        save_to_json_file(api_configs, output_file_path)
        
        # Print the transformed data
        print(api_configs)
    else:
        print(f"The file {file_path} does not contain the 'apis' key")

except yaml.YAMLError as e:
    print(f"Error parsing YAML file {file_path}: {e}")
except Exception as e:
    print(f"Unexpected error with file {file_path}: {e}")

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
    while True:
        for api_config in api_configs:
            name = api_config.get('name', api_config['genesis']['host'])  # Fallback to genesis host if name is missing
            genesis_up = check_api(api_config['genesis'])
            dependents_status = {f"{dep['host']}:{dep['port']}": check_api(dep) for dep in api_config.get('dependents', [])}
            potentials_status = {f"{pot['host']}:{pot['port']}": check_api(pot) for pot in api_config.get('potentials', [])}

            impacted_dependents = [dep for dep, status in dependents_status.items() if not status]
            impacted_potentials = [pot for pot, status in potentials_status.items() if not status]

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
                    ('impacted_dependents', impacted_dependents),
                    ('impacted_potentials', impacted_potentials),
                    ('registered_services', registered_services)
                ])
            elif impacted_dependents:
                service_status[name] = OrderedDict([
                    ('genesis', 'UP'),
                    ('dependents', 'DOWN'),
                    ('potentials', 'DEGRADED'),
                    ('impacted_dependents', impacted_dependents),
                    ('impacted_potentials', impacted_potentials),
                    ('registered_services', registered_services)
                ])
            elif impacted_potentials:
                service_status[name] = OrderedDict([
                    ('genesis', 'UP'),
                    ('dependents', 'UP'),
                    ('potentials', 'DEGRADED'),
                    ('impacted_dependents', impacted_dependents),
                    ('impacted_potentials', impacted_potentials),
                    ('registered_services', registered_services)
                ])
            else:
                service_status[name] = OrderedDict([
                    ('genesis', 'UP'),
                    ('dependents', 'UP'),
                    ('potentials', 'UP'),
                    ('impacted_dependents', impacted_dependents),
                    ('impacted_potentials', impacted_potentials),
                    ('registered_services', registered_services)
                ])
        time.sleep(30)

if __name__ == "__main__":
    service_status = OrderedDict()
    for api in api_configs:
        name = api.get('name', api['genesis']['host'])  # Fallback to genesis host if name is missing
        registered_services = OrderedDict([
            ('genesis', f"{api['genesis']['host']}:{api['genesis']['port']}"),
            ('dependents', [f"{dep['host']}:{dep['port']}" for dep in api.get('dependents', [])]),
            ('potentials', [f"{pot['host']}:{pot['port']}" for pot in api.get('potentials', [])])
        ])
        service_status[name] = OrderedDict([
            ('genesis', 'UNKNOWN'),
            ('dependents', 'UNKNOWN'),
            ('potentials', 'UNKNOWN'),
            ('impacted_dependents', []),
            ('impacted_potentials', []),
            ('registered_services', registered_services)
        ])

    import threading
    monitor_thread = threading.Thread(target=monitor_apis)
    monitor_thread.start()
    app.run(host='0.0.0.0', port=5000)
