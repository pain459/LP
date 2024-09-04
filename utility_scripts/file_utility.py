import os
import shutil
from datetime import datetime

class FileUtility:
    def __init__(self, base_dir):
        """Initialize with the base directory"""
        self.base_dir = base_dir

    def list_files(self, ext=None, size=None, modified_after=None):
        """
        List files in the base directory with optional filtering.
        - ext: Filter by file extension (e.g. '.txt')
        - size: Filter by minimum file size (in bytes)
        - modified_after: Filter by modification date (as datetime object)
        """
        file_list = []
        for root, dirs, files in os.walk(self.base_dir):
            for file in files:
                file_path = os.path.join(root, file)
                if ext and not file.endswith(ext):
                    continue
                if size and os.path.getsize(file_path) < size:
                    continue
                if modified_after:
                    modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                    if modified_time < modified_after:
                        continue
                file_list.append(file_path)
        return file_list

    def copy_files(self, file_paths, dest_dir):
        """
        Copy a list of files to the destination directory.
        """
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        for file_path in file_paths:
            shutil.copy(file_path, dest_dir)
        print(f"Copied {len(file_paths)} files to {dest_dir}")

    def move_files(self, file_paths, dest_dir):
        """
        Move a list of files to the destination directory.
        """
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        for file_path in file_paths:
            shutil.move(file_path, dest_dir)
        print(f"Moved {len(file_paths)} files to {dest_dir}")

    def delete_files(self, file_paths):
        """
        Delete a list of files.
        """
        for file_path in file_paths:
            os.remove(file_path)
        print(f"Deleted {len(file_paths)} files")

# Example usage
if __name__ == "__main__":
    base_dir = "LP/utility_scripts/"
    utility = FileUtility(base_dir)
    
    # List all .txt files greater than 1KB and modified after Jan 1, 2023
    files_to_manage = utility.list_files(ext=".txt", size=1, modified_after=datetime(2023, 1, 1))
    
    # Copy these files to another directory
    utility.copy_files(files_to_manage, "/tmp/")

    # Move files to another directory
    # utility.move_files(files_to_manage, "/path/to/destination")
    
    # Delete these files
    # utility.delete_files(files_to_manage)
