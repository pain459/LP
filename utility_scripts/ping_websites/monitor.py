import requests
import time
from prettytable import PrettyTable

# List of URLs to monitor
urls = [
    "https://www.google.com",
    "https://www.github.com",
    # "https://www.website.com"  # Add more URLs as needed
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

def monitor_websites(urls, interval=10):
    while True:
        table = PrettyTable()
        table.field_names = ["URL", "Status"]
        for url in urls:
            status = check_status(url)
            table.add_row([url, status])
        
        print(table)
        time.sleep(interval)

if __name__ == "__main__":
    monitor_websites(urls)
