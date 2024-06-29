import requests
import time
import logging
from logging.handlers import RotatingFileHandler

log_handler = RotatingFileHandler('monitor.log', maxBytes=104857600, backupCount=5)
log_handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
logger = logging.getLogger('MonitorLogger')
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

api_endpoints = [
    {"name": "service1", "port": 80},
    {"name": "service2", "port": 80},
    {"name": "service3", "port": 80},
    {"name": "service4", "port": 80},
]

def monitor_apis():
    while True:
        for api in api_endpoints:
            url = f'http://{api["name"]}:{api["port"]}'
            try:
                response = requests.get(url)
                logger.info(f'{api["name"]}_{api["port"]}: {response.status_code}')
            except Exception as e:
                logger.error(f'{api["name"]}_{api["port"]}: {str(e)}')
        time.sleep(30)

if __name__ == "__main__":
    time.sleep(10)  # Give services some time to start up
    monitor_apis()
