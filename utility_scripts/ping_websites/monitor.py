import requests
import time
from prettytable import PrettyTable
from datetime import datetime
import os
import socket
import logging
from logging.handlers import RotatingFileHandler

# Function to read URLs from a file
def read_urls_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            urls = file.read().splitlines()
        return urls
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []

# Function to check the status of a URL
def check_status(url):
    try:
        # Validate URL format
        if not url.startswith("http://") and not url.startswith("https://"):
            raise ValueError("URL must start with 'http://' or 'https://'")
        
        # Check DNS resolution
        socket.gethostbyname(url.replace("https://", "").replace("http://", "").split('/')[0])
        
        response = requests.get(url)
        if response.status_code == 200:
            return "OK"
        else:
            return f"Down (Status Code: {response.status_code})"
    except requests.exceptions.RequestException as e:
        return f"Down (Error: {str(e)})"
    except socket.gaierror:
        return "DNS resolution error"
    except ValueError as ve:
        return f"Error: {str(ve)}"

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
def monitor_websites(file_path, interval=10):
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
        for url in urls:
            status = check_status(url)
            table.add_row([url, status])
            log_entries.append(f"{url} - {status}")
        
        print(table)
        
        # Log the current statuses
        logger.info("\n" + "\n".join(log_entries))

        for remaining in range(interval, 0, -1):
            print(f"\rNext refresh in {remaining} seconds...", end="")
            time.sleep(1)
        print("\r", end="")  # Clear the countdown line

if __name__ == "__main__":
    file_path = 'websites.txt'
    monitor_websites(file_path)
