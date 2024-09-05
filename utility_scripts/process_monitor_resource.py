import psutil
from datetime import datetime

# Function to get a list of running processes
def list_processes(sort_by="memory", limit=10):
    processes = []
    
    # Iterate over all running processes
    for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_info', 'create_time']):
        try:
            # Get process information
            proc_info = proc.info
            proc_info['memory_percent'] = proc.memory_percent()
            proc_info['create_time'] = datetime.fromtimestamp(proc_info['create_time']).strftime('%Y-%m-%d %H:%M:%S')
            processes.append(proc_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    # Sort processes based on the provided criteria
    if sort_by == "cpu":
        processes = sorted(processes, key=lambda p: p['cpu_percent'], reverse=True)
    elif sort_by == "memory":
        processes = sorted(processes, key=lambda p: p['memory_percent'], reverse=True)
    
    # Limit the number of processes to display
    return processes[:limit]

# Function to print the process list in a readable format
def print_processes(processes):
    print(f"{'PID':<8} {'Name':<25} {'User':<15} {'CPU%':<10} {'Memory%':<10} {'Start Time':<20}")
    print("=" * 90)
    for proc in processes:
        print(f"{proc['pid']:<8} {proc['name']:<25} {proc['username']:<15} {proc['cpu_percent']:<10} {proc['memory_percent']:<10.2f} {proc['create_time']:<20}")
    print("=" * 90)

# Function to monitor and display processes
def monitor_processes(sort_by="memory", limit=10):
    processes = list_processes(sort_by, limit)
    print_processes(processes)

if __name__ == "__main__":
    # Sort by either "cpu" or "memory" and limit the number of processes displayed
    monitor_processes(sort_by="cpu", limit=10)  # Change sort_by to "memory" if needed
