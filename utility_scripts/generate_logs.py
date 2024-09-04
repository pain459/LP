import random
import time
from datetime import datetime

# Define log levels and sample messages
log_levels = ["INFO", "WARNING", "ERROR", "DEBUG"]
sample_messages = [
    "User logged in successfully",
    "File not found",
    "Unable to connect to database",
    "System running low on memory",
    "User session expired",
    "Network connection reset",
    "Cache cleared successfully",
    "Permission denied for operation",
    "Disk space usage exceeded limit",
    "Configuration file updated"
]

# Function to generate a single log entry
def generate_log_entry():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_level = random.choice(log_levels)
    message = random.choice(sample_messages)
    return f"{timestamp} - {log_level} - {message}"

# Function to generate a log file with 1000 lines
def generate_log_file(filename, num_lines=1000):
    with open(filename, 'w') as file:
        for _ in range(num_lines):
            log_entry = generate_log_entry()
            file.write(log_entry + '\n')

if __name__ == "__main__":
    log_filename = "sample_log_file.log"  # The name of the log file
    generate_log_file(log_filename, 1000)  # Generate 1000 log entries
    print(f"Log file '{log_filename}' generated with 1000 lines.")
