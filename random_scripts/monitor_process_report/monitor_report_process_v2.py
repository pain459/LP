import time
import subprocess
import requests
import socket
import argparse
import signal
import sys
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_arg_parser():
    parser = argparse.ArgumentParser(description='Monitor a process and alert if it is not running.')
    parser.add_argument('--process_name', '-pname', type=str, required=True, help='Name of the process to monitor.')
    parser.add_argument('--slack_webhook_url', type=str, default=os.getenv("SLACK_WEBHOOK_URL", "https://hooks.slack.com/services/webhook"),
                        help='Slack webhook URL for notifications.')
    parser.add_argument('--interval', type=int, default=int(os.getenv("CHECK_INTERVAL", 300)),
                        help='Time interval between checks in seconds.')
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

def main(args):
    logging.info(f"Starting process monitoring for '{args.process_name}' on {get_hostname()}...")
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        success = check_process(args.process_name)
        post_success_metric(args.slack_webhook_url, args.process_name, success)
        time.sleep(args.interval)

if __name__ == "__main__":
    args = setup_arg_parser()
    main(args)
