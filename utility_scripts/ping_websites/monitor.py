import requests
import time
from prettytable import PrettyTable
from datetime import datetime
import os

# List of URLs to monitor
urls = [
    "https://www.google.com",
    "https://www.github.com",
    # "https://www.nonexistentwebsite.com"  # Add more URLs as needed
]

def check_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "OK"
        else:
            return f"Down (Status Code: {response.status_code})"
    except requests.exceptions.RequestException as e:
        return f"Down (Error: {str(e)})"

def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

def monitor_websites(urls, interval=10):
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
    monitor_websites(urls)
