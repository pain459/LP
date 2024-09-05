import os
import zipfile
import datetime

# Function to create a ZIP archive of a given directory or file
def create_backup(source, destination):
    # Create a timestamp for the backup file
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    
    # Ensure the destination directory exists
    if not os.path.exists(destination):
        os.makedirs(destination)
    
    # Define the full path of the backup file
    backup_filename = os.path.join(destination, f"backup_{timestamp}.zip")
    
    # Create a ZIP file
    with zipfile.ZipFile(backup_filename, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
        # If source is a directory, add all files and subdirectories to the ZIP archive
        if os.path.isdir(source):
            for foldername, subfolders, filenames in os.walk(source):
                for filename in filenames:
                    file_path = os.path.join(foldername, filename)
                    backup_zip.write(file_path, os.path.relpath(file_path, source))
        # If source is a file, add it directly to the ZIP archive
        elif os.path.isfile(source):
            backup_zip.write(source, os.path.basename(source))
    
    print(f"Backup created: {backup_filename}")

# Function to perform a backup of multiple directories or files
def backup_multiple_sources(sources, destination):
    for source in sources:
        create_backup(source, destination)

if __name__ == "__main__":
    # List of directories or files to backup
    backup_sources = [
        "/path/to/your/directory1",
        "/path/to/your/directory2",
        "/path/to/your/file.txt"
    ]
    
    # Directory where the backups will be saved
    backup_destination = "/path/to/your/backup/destination"
    
    # Perform backup
    backup_multiple_sources(backup_sources, backup_destination)
