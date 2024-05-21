import time
import subprocess
import requests
import socket
import argparse
import logging

# Setup logging
logging.basicConfig(filename='process_monitor.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Setup argument parser
parser = argparse.ArgumentParser(description='Monitor a process and alert if it is not running.')
parser.add_argument('--process_name', '-pname', type=str, required=True, help='Name of the process to monitor.')
parser.add_argument('--restart_command', '-rcmd', type=str, help='Command to restart the process if not running.')

args = parser.parse_args()

# Use the process name and restart command from the command-line arguments
process_name = args.process_name
restart_command = args.restart_command
# Replace with your Slack Webhook URL
slack_webhook_url = "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"

# Get the hostname of the server
hostname = socket.gethostname()

def check_process(process_name):
    try:
        output = subprocess.check_output(["pgrep", "-x", process_name])
        pids = output.decode().strip().split("\n")
        if pids:
            logging.info(f"Process '{process_name}' found on '{hostname}' with PIDs: {', '.join(pids)}")
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False

def post_slack_message(message):
    payload = {"text": message}
    response = requests.post(slack_webhook_url, json=payload)
    if response.status_code != 200:
        logging.error(f"Failed to send message to Slack: {response.status_code}")

def restart_process():
    retries = 3
    for i in range(retries):
        try:
            subprocess.check_call(restart_command, shell=True)
            time.sleep(10)  # Give some time for the process to start
            if check_process(process_name):
                post_slack_message(f"Attempt {i + 1}: Successfully restarted the process.")
                logging.info(f"Successfully restarted the process using '{restart_command}'.")
                return True
            else:
                raise Exception("Process started but not detected.")
        except Exception as e:
            error_message = f"Attempt {i + 1}: Failed to restart the process: {e}."
            logging.error(error_message)
            post_slack_message(error_message)
            time.sleep(10)  # Delay before retrying
            if i == retries - 1:  # Last retry
                final_message = f"Failed to restart process '{process_name}' after {retries} attempts."
                post_slack_message(final_message)
                logging.error(final_message)
    return False

def post_success_metric(success):
    if success:
        print("Process is running.")
    else:
        alert_message = f"ALERT: Process '{process_name}' is not running on '{hostname}'! Attempting to restart..."
        post_slack_message(alert_message)
        if restart_command:
            if not restart_process():
                failure_message = f"Script attempted to auto-recover '{process_name}' but failed to do so."
                post_slack_message(failure_message)
                logging.error(failure_message)

interval = 5 * 60  # 5 minutes in seconds

print(f"Starting process monitoring for '{process_name}' on {hostname}...")
while True:
    success = check_process(process_name)
    post_success_metric(success)
    time.sleep(interval)
