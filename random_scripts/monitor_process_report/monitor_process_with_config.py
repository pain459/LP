import time
import subprocess
import requests
import socket
import argparse
import signal
import sys
import os
import yaml
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    else:
        logging.warning(f"No configuration file found at {file_path}. Using default or environmental settings.")
        return {}

def setup_arg_parser(config):
    parser = argparse.ArgumentParser(description='Monitor a process and alert if it is not running.')
    parser.add_argument('--process_name', '-pname', type=str, required=True,
                        help='Name of the process to monitor.', default=config.get('process_name'))
    parser.add_argument('--slack_webhook_url', type=str,
                        help='Slack webhook URL for notifications.', default=config.get('slack_webhook_url'))
    parser.add_argument('--interval', type=int,
                        help='Time interval between checks in seconds.', default=config.get('interval', 300))
    return parser.parse_args()

def get_hostname():
    return socket.gethostname()

def check_process(process_name):
    try:
        output = subprocess.check_output(["pgrep", "-f", f"{process_name} | grep -v grep"], shell=True)
        pids = output.decode().strip().split("\n")
        logging.info(f"Process '{process_name}' found with PIDs: {', '.join(pids)}")
        return True
    except subprocess.CalledProcessError:
        logging.warning(f"Process '{process_name}' not found.")
        return False

def post_slack_message(webhook_url, message):
    payload = {"text": message}
    response = requests.post(webhook_url, json=payload)
    if response.status_code != 200:
        logging.error(f"Failed to send message to Slack: {response.status_code}")

def post_success_metric(webhook_url, process_name, success):
    if success:
        logging.info("Process is running")
    else:
        message = f"ALERT: Process '{process_name}' is not running on '{get_hostname()}'!"
        post_slack_message(webhook_url, message)

def signal_handler(signum, frame):
    logging.info('Gracefully shutting down')
    sys.exit(0)

def main():
    config_path = 'config.yaml'  # Default path to configuration file
    config = load_config(config_path)
    args = setup_arg_parser(config)
    logging.info(f"Starting process monitoring for '{args.process_name}' on {get_hostname()}...")
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        success = check_process(args.process_name)
        post_success_metric(args.slack_webhook_url, args.process_name, success)
        time.sleep(args.interval)

if __name__ == "__main__":
    main()
