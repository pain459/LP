import subprocess
import logging
from logging.handlers import RotatingFileHandler


# Configure logging
LOG_FILENAME = 'app.log'
logging.basicConfig(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler = RotatingFileHandler(LOG_FILENAME, maxBytes=5 * 1024 * 1024, backupCount=3)
handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(handler)


logger.info("Program starts.")
job_names = ['ping google.com', 'ls']

for i in job_names:
    print(i)
    output = subprocess.run(i, capture_output=True, text=True)
    print(output.stdout)