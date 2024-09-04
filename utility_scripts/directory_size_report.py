import os
from hurry.filesize import size as human_readable_size  # Optional: For human-readable file size

# Function to get the size of a directory
def get_directory_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
    return total_size

# Function to print and sort the size of each subdirectory in the given directory
def report_directory_sizes(base_directory):
    size_dict = {}

    # Gather sizes for each item in the base directory
    for item in os.listdir(base_directory):
        item_path = os.path.join(base_directory, item)
        if os.path.isdir(item_path):
            dir_size = get_directory_size(item_path)
            size_dict[item] = dir_size
        elif os.path.isfile(item_path):
            file_size = os.path.getsize(item_path)
            size_dict[item] = file_size

    # Sort by size in descending order
    sorted_items = sorted(size_dict.items(), key=lambda x: x[1], reverse=True)

    # Print the sorted directory and file sizes
    print(f"Directory size report for: {base_directory}")
    print("-" * 50)
    for item, size in sorted_items:
        print(f"{item}: {human_readable_size(size)}")
    print("-" * 50)

if __name__ == "__main__":
    base_dir = "/home/ravik/src_git/"  # Change to your target directory
    report_directory_sizes(base_dir)
