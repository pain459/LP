import os
import time
import random
import string

def generate_random_alphanumeric(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def rename_files_in_directory(directory_path):
    try:
        # Iterate over all files in the directory
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            
            # Check if it's a file (not a directory)
            if os.path.isfile(file_path):
                # Extract the file extension
                _, file_extension = os.path.splitext(filename)
                
                # Generate the new filename
                unix_timestamp = int(time.time())
                random_alphanumeric = generate_random_alphanumeric()
                new_filename = f"{unix_timestamp}_{random_alphanumeric}{file_extension}"
                
                # Define the new file path
                new_file_path = os.path.join(directory_path, new_filename)
                
                # Rename the file
                os.rename(file_path, new_file_path)
                
                print(f"Renamed '{filename}' to '{new_filename}'")
                
    except Exception as e:
        print(f"An error occurred: {e}")

# Directory path to rename files in
directory_path = "your_directory_path_here"

# Call the function
rename_files_in_directory(directory_path)
