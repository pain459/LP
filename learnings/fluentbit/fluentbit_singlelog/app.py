import logging
import time

# Configure logging
logging.basicConfig(filename='/var/log/app.log', level=logging.INFO, format='%(asctime)s %(message)s')

while True:
    logging.info('This is a log message from the Python application.')
    time.sleep(5)
