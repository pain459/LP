import requests
import time
from prettytable import PrettyTable
from datetime import datetime
import os
import socket

# Function to read URLs from a file
def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = file.read().splitlines()
    return urls

def check_status(url):
    try:
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

def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

def monitor_websites(file_path, interval=10):
    urls = read_urls_from_file(file_path)
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
