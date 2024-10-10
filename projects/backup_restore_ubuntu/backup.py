import os
import subprocess
from datetime import datetime

# Define backup directory
backup_dir = os.path.expanduser("~/ubuntu_backup")
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_dir = os.path.join(backup_dir, timestamp)

# Create backup directory if it doesn't exist
os.makedirs(backup_dir, exist_ok=True)

# Backup APT Sources
def backup_apt_sources():
    apt_sources_dir = os.path.join(backup_dir, "apt_sources")
    os.makedirs(apt_sources_dir, exist_ok=True)
    
    # Copy /etc/apt/sources.list
    os.system(f"cp /etc/apt/sources.list {apt_sources_dir}")
    
    # Copy /etc/apt/sources.list.d/ directory
    os.system(f"cp -r /etc/apt/sources.list.d {apt_sources_dir}")
    print("APT sources backed up successfully.")

# Backup Installed Applications
def backup_installed_applications():
    package_list_file = os.path.join(backup_dir, "installed_packages.txt")
    
    # Use dpkg to get the list of installed packages
    with open(package_list_file, "w") as f:
        subprocess.run(["dpkg", "--get-selections"], stdout=f)
    print("Installed applications backed up successfully.")

# Backup Gnome Settings
def backup_gnome_settings():
    gnome_settings_file = os.path.join(backup_dir, "gnome_settings_backup.txt")
    
    # Use dconf to dump Gnome settings
    with open(gnome_settings_file, "w") as f:
        subprocess.run(["dconf", "dump", "/"], stdout=f)
    print("Gnome settings backed up successfully.")

# Execute all backups
if __name__ == "__main__":
    print("Starting backup process...")
    backup_apt_sources()
    backup_installed_applications()
    backup_gnome_settings()
    print(f"Backup completed. All files are stored in {backup_dir}")
