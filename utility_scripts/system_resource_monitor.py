import psutil
import time
from datetime import datetime

# Function to get CPU usage
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

# Function to get memory usage
def get_memory_usage():
    memory_info = psutil.virtual_memory()
    return {
        'total': memory_info.total,
        'available': memory_info.available,
        'percent': memory_info.percent,
        'used': memory_info.used,
        'free': memory_info.free
    }

# Function to get disk usage
def get_disk_usage():
    disk_info = psutil.disk_usage('/')
    return {
        'total': disk_info.total,
        'used': disk_info.used,
        'free': disk_info.free,
        'percent': disk_info.percent
    }

# Function to get network statistics
def get_network_stats():
    net_io = psutil.net_io_counters()
    return {
        'bytes_sent': net_io.bytes_sent,
        'bytes_recv': net_io.bytes_recv
    }

# Function to print a resource usage report
def print_resource_usage():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"Resource usage report at {timestamp}:")
    
    cpu_usage = get_cpu_usage()
    print(f"CPU Usage: {cpu_usage}%")
    
    memory_usage = get_memory_usage()
    print(f"Memory Usage: {memory_usage['percent']}%")
    print(f"Total Memory: {memory_usage['total'] / (1024 ** 3):.2f} GB")
    print(f"Used Memory: {memory_usage['used'] / (1024 ** 3):.2f} GB")
    print(f"Free Memory: {memory_usage['free'] / (1024 ** 3):.2f} GB")
    
    disk_usage = get_disk_usage()
    print(f"Disk Usage: {disk_usage['percent']}%")
    print(f"Total Disk Space: {disk_usage['total'] / (1024 ** 3):.2f} GB")
    print(f"Used Disk Space: {disk_usage['used'] / (1024 ** 3):.2f} GB")
    print(f"Free Disk Space: {disk_usage['free'] / (1024 ** 3):.2f} GB")
    
    network_stats = get_network_stats()
    print(f"Bytes Sent: {network_stats['bytes_sent'] / (1024 ** 2):.2f} MB")
    print(f"Bytes Received: {network_stats['bytes_recv'] / (1024 ** 2):.2f} MB")
    print("-" * 50)

# Function to monitor resources every few seconds
def monitor_resources(interval=5):
    try:
        while True:
            print_resource_usage()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Monitoring stopped.")

if __name__ == "__main__":
    monitor_resources(10)  # Adjust the interval (in seconds) as needed
