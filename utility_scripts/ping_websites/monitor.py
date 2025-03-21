import requests
import time
from prettytable import PrettyTable
from datetime import datetime
import os
import socket
import logging
from logging.handlers import RotatingFileHandler
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse
import json

# Usage
# python monitor.py --file websites.txt --interval 10 --slack-webhook-url YOUR_SLACK_WEBHOOK_URL
# python monitor.py --file websites.txt --interval 10



# Function to read URLs from a file
def read_urls_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            urls = file.read().splitlines()
        return urls
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []

# Function to check the status of a URL with retries
def check_status(url, retries=3):
    for _ in range(retries):
        try:
            # Validate URL format
            if not url.startswith("http://") and not url.startswith("https://"):
                raise ValueError("URL must start with 'http://' or 'https://'")
            
            # Check DNS resolution
            socket.gethostbyname(url.replace("https://", "").replace("http://", "").split('/')[0])
            
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return "OK"
            else:
                return f"HTTP_ERR (Status Code: {response.status_code})"
        except requests.exceptions.Timeout:
            last_exception = "TIMEOUT_ERR"
        except (requests.exceptions.RequestException, socket.gaierror) as e:
            if isinstance(e, socket.gaierror):
                last_exception = "DNS_ERR"
            else:
                last_exception = f"HTTP_ERR (Error: {str(e)})"
        except ValueError as ve:
            return f"FORMAT_ERR (Error: {str(ve)})"
    return last_exception

# Function to send a message to Slack
def send_slack_message(webhook_url, message):
    payload = {"text": message}
    try:
        response = requests.post(webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        if response.status_code != 200:
            raise ValueError(f"Request to Slack returned an error {response.status_code}, the response is:\n{response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending message to Slack: {e}")

# Function to clear the screen
def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

# Function to set up logging
def setup_logging():
    logger = logging.getLogger("WebsiteMonitor")
    logger.setLevel(logging.INFO)
    
    handler = RotatingFileHandler("website_monitor.log", maxBytes=5*1024*1024, backupCount=1)
    handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
    
    logger.addHandler(handler)
    return logger

# Function to monitor websites
def monitor_websites(file_path, interval=10, slack_webhook_url=None):
    urls = read_urls_from_file(file_path)
    if not urls:
        return
    
    logger = setup_logging()
    
    while True:
        clear_screen()
        current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
        print(f"Website Status Monitor - {current_time}\n")
        
        table = PrettyTable()
        table.field_names = ["URL", "Status"]
        log_entries = []
        slack_messages = []
        
        with ThreadPoolExecutor(max_workers=10) as executor:
            future_to_url = {executor.submit(check_status, url): url for url in urls}
            for future in as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    status = future.result()
                except Exception as exc:
                    status = f"OTHER_ERR (Error: {str(exc)})"
                table.add_row([url, status])
                log_entries.append(f"{url} - {status}")
                if "OK" not in status:
                    slack_messages.append(f"{url} - {status}")
        
        print(table)
        
        # Log the current statuses
        logger.info("\n" + "\n".join(log_entries))
        
        # Send Slack notifications if configured
        if slack_webhook_url and slack_messages:
            message = "Website Monitoring Alerts:\n" + "\n".join(slack_messages)
            send_slack_message(slack_webhook_url, message)

        for remaining in range(interval, 0, -1):
            print(f"\rNext refresh in {remaining} seconds...", end="")
            time.sleep(1)
        print("\r", end="")  # Clear the countdown line

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Website Monitoring Script")
    parser.add_argument('--file', type=str, required=True, help='Path to the file containing URLs to monitor')
    parser.add_argument('--interval', type=int, default=10, help='Interval between checks in seconds')
    parser.add_argument('--slack-webhook-url', type=str, help='Slack webhook URL for sending alerts')
    
    args = parser.parse_args()
    
    monitor_websites(args.file, args.interval, args.slack_webhook_url)
