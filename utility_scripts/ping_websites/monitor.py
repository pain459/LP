import requests
import time
from prettytable import PrettyTable
from datetime import datetime
import os
import socket

def read_urls_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            urls = file.read().splitlines()
        return urls
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []

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

def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

def monitor_websites(file_path, interval=10):
    urls = read_urls_from_file(file_path)
    if not urls:
        return
    
    while True:
        clear_screen()
        current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
        print(f"Website Status Monitor - {current_time}\n")
        
        table = PrettyTable()
        table.field_names = ["URL", "Status"]
        for url in urls:
            status = check_status(url)
            table.add_row([url, status])
        
        print(table)
        time.sleep(interval)

if __name__ == "__main__":
    file_path = 'websites.txt'
    monitor_websites(file_path)
