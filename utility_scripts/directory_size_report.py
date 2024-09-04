import os
from hurry.filesize import size as human_readable_size  # Optional: For a human-readable file size

# Function to get the size of a directory
def get_directory_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
    return total_size

# Function to print the size of each subdirectory in the given directory
def report_directory_sizes(base_directory):
    print(f"Directory size report for: {base_directory}")
    print("-" * 50)
    for item in os.listdir(base_directory):
        item_path = os.path.join(base_directory, item)
        if os.path.isdir(item_path):
            dir_size = get_directory_size(item_path)
            print(f"{item}: {human_readable_size(dir_size)}")
        elif os.path.isfile(item_path):
            file_size = os.path.getsize(item_path)
            print(f"{item}: {human_readable_size(file_size)}")
    print("-" * 50)

if __name__ == "__main__":
    base_dir = "/home/ravik/src_git/"  # Change to your target directory
    report_directory_sizes(base_dir)
