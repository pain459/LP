import time
import subprocess
import requests
import socket
import argparse

# Argument parser
parser = argparse.ArgumentParser(description='Monitor a process and alert if it is not running.')
parser.add_argument('--process_name', '-pname', type=str, required=True, help='Name of the process to monitor.')

args = parser.parse_args()

# Use the process name from the command-line arguments
process_name = args.process_name

# Constants
slack_webhook_url = "https://hooks.slack.com/services/webhook"
hostname = socket.gethostname()
interval = 5 * 60  # 5 minutes in seconds

def check_process(process_name):
    try:
        output = subprocess.check_output(["pgrep", "-f", process_name, 'grep', '-v', 'grep'])
        pids = output.decode().strip().split("\n")
        print(f"Process '{process_name}' found on '{hostname}' with PIDs: {', '.join(pids)}")
        return True
    except subprocess.CalledProcessError:
        print(f"Process '{process_name}' not found on '{hostname}'.")
        return False

def post_slack_message(message):
    payload = {"text": message}
    response = requests.post(slack_webhook_url, json=payload)
    if response.status_code != 200:
        print(f"Failed to send message to Slack: {response.status_code}")

def post_success_metric(success):
    if success:
        print("Posting success metric: Process is running")
    else:
        message = f"ALERT: Process '{process_name}' is not running on '{hostname}'!"
        post_slack_message(message)

def main():
    print(f"Starting process monitoring for '{process_name}' on {hostname}...")
    while True:
        success = check_process(process_name)
        post_success_metric(success)
        time.sleep(interval)


if __name__ == "__main__":
    main()