import logging
import time

# Configure logging
logging.basicConfig(filename='/var/log/app2.log', level=logging.INFO, format='%(asctime)s %(message)s')

while True:
    logging.info('This is a log message from Python application 2.')
    time.sleep(5)
