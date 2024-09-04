import os
import hashlib

# Function to compute the MD5 hash of a file
def compute_md5(file_path, chunk_size=4096):
    md5 = hashlib.md5()
    try:
        with open(file_path, 'rb') as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:  # If the chunk is empty, break the loop
                    break
                md5.update(chunk)
        return md5.hexdigest()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

# Function to find duplicate files in a directory
def find_duplicates(base_directory):
    files_seen = {}  # Dictionary to store files by hash
    duplicates = []  # List to store duplicate files

    for dirpath, _, filenames in os.walk(base_directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if os.path.isfile(file_path):
                file_hash = compute_md5(file_path)  # Compute hash of the file
                if file_hash:
                    if file_hash in files_seen:
                        duplicates.append((file_path, files_seen[file_hash]))  # Add to duplicates
                    else:
                        files_seen[file_hash] = file_path  # Store the first occurrence

    return duplicates

# Function to report and display duplicates
def report_duplicates(duplicates):
    if duplicates:
        print("Duplicate files found:")
        print("-" * 50)
        for duplicate, original in duplicates:
            print(f"Duplicate: {duplicate}")
            print(f"Original: {original}")
            print("-" * 50)
    else:
        print("No duplicate files found.")

if __name__ == "__main__":
    base_dir = "/home/ravik/src_git/"  # Replace with the directory to search
    duplicates = find_duplicates(base_dir)
    report_duplicates(duplicates)
