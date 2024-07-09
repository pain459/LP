import psutil

def print_process_tree(pid, indent=0):
    try:
        process = psutil.Process(pid)
        print(' ' * indent + f"PID: {process.pid}, PPID: {process.ppid()}, Name: {process.name()}")
        for child in process.children(recursive=False):
            print_process_tree(child.pid, indent + 4)
    except psutil.NoSuchProcess:
        print(' ' * indent + f"PID: {pid} does not exist")

if __name__ == "__main__":
    # Start from init (PID 1)
    print_process_tree(1)
