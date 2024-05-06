import time
import subprocess
import requests
import socket

# Replace this with the process name you want to monitor
process_name = "your_process_name"
# Replace with your Slack Webhook URL
slack_webhook_url = "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"

# Get the hostname of the server
hostname = socket.gethostname()

def check_process(process_name):
    try:
        output = subprocess.check_output(["pgrep", "-f", process_name])
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

interval = 5 * 60  # 5 minutes in seconds

print(f"Starting process monitoring on {hostname}...")
while True:
    success = check_process(process_name)
    post_success_metric(success)
    time.sleep(interval)
