import os
import time
from datetime import datetime, timedelta

# Function to get human-readable file sizes
def human_readable_size(size, decimal_places=2):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.{decimal_places}f} {unit}"
        size /= 1024.0

# Function to find files larger than a specified size
def find_large_files(directory, min_size):
    large_files = []
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path)
                if file_size >= min_size:
                    large_files.append((file_path, file_size))
    return large_files

# Function to find files older than a specified number of days
def find_old_files(directory, days_old):
    old_files = []
    cutoff_time = time.time() - (days_old * 86400)  # Convert days to seconds
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if os.path.isfile(file_path):
                file_mod_time = os.path.getmtime(file_path)
                if file_mod_time < cutoff_time:
                    old_files.append(file_path)
    return old_files

# Function to delete files and free up disk space
def delete_files(file_paths):
    for file_path in file_paths:
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

# Function to display large files and optionally delete them
def clean_large_files(directory, min_size, delete=False):
    large_files = find_large_files(directory, min_size)
    if large_files:
        print(f"Found {len(large_files)} large files (larger than {human_readable_size(min_size)}):")
        for file, size in large_files:
            print(f"{file} - {human_readable_size(size)}")
        if delete:
            confirm = input("Do you want to delete these files? (y/n): ").lower()
            if confirm == 'y':
                delete_files([file for file, size in large_files])
    else:
        print(f"No files larger than {human_readable_size(min_size)} found.")

# Function to display old files and optionally delete them
def clean_old_files(directory, days_old, delete=False):
    old_files = find_old_files(directory, days_old)
    if old_files:
        print(f"Found {len(old_files)} files older than {days_old} days:")
        for file in old_files:
            mod_time = datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y-%m-%d %H:%M:%S')
            print(f"{file} - Last modified: {mod_time}")
        if delete:
            confirm = input("Do you want to delete these files? (y/n): ").lower()
            if confirm == 'y':
                delete_files(old_files)
    else:
        print(f"No files older than {days_old} days found.")

if __name__ == "__main__":
    # Directory to clean
    base_dir = "/home/ravik/src_git/LP/"  # Replace with your target directory
    
    # Option 1: Clean large files
    min_file_size = 100 * 1024 * 1024  # Example: 100 MB
    clean_large_files(base_dir, min_file_size, delete=False)  # Set delete=True to actually delete
    
    # Option 2: Clean old files
    days_threshold = 30  # Example: files older than 30 days
    clean_old_files(base_dir, days_threshold, delete=False)  # Set delete=True to actually delete
