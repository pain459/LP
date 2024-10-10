import os
import time
import random
import string

def generate_random_alphanumeric(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def rename_files_in_directory(directory_path, exclude_extensions_csv):
    # Convert CSV string of extensions into a list and strip any whitespace
    exclude_extensions = [ext.strip() for ext in exclude_extensions_csv.split(',')]
    
    try:
        # Iterate over all files in the directory
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            
            # Check if it's a file (not a directory)
            if os.path.isfile(file_path):
                # Extract the file extension
                _, file_extension = os.path.splitext(filename)
                
                # Proceed only if the file extension is not in the exclude list
                if file_extension not in exclude_extensions:
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

# Directory path and CSV list of extensions to exclude (edit these as needed)
directory_path = "your_directory_path_here"
exclude_extensions_csv = ".txt, .py, .pdf"  # Exclude .txt, .py, and .pdf files

# Call the function
rename_files_in_directory(directory_path, exclude_extensions_csv)
