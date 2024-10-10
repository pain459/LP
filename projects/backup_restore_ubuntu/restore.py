import os
import subprocess

# Define the path to the backup directory
backup_dir = input("Enter the path to the backup directory: ")

# Restore APT Sources
def restore_apt_sources():
    apt_sources_backup_dir = os.path.join(backup_dir, "apt_sources")
    
    if os.path.exists(apt_sources_backup_dir):
        # Restore /etc/apt/sources.list
        os.system(f"sudo cp {apt_sources_backup_dir}/sources.list /etc/apt/sources.list")
        
        # Restore /etc/apt/sources.list.d directory
        os.system(f"sudo cp -r {apt_sources_backup_dir}/sources.list.d /etc/apt/")
        
        # Update the package list
        subprocess.run(["sudo", "apt", "update"])
        print("APT sources restored and updated successfully.")
    else:
        print("APT sources backup not found.")

# Restore Installed Applications
def restore_installed_applications():
    package_list_file = os.path.join(backup_dir, "installed_packages.txt")
    
    if os.path.exists(package_list_file):
        # Use dpkg to set selections from the package list file
        with open(package_list_file, "r") as f:
            subprocess.run(["sudo", "dpkg", "--set-selections"], stdin=f)
        
        # Install the packages from the selections
        subprocess.run(["sudo", "apt-get", "-y", "dselect-upgrade"])
        print("Installed applications restored successfully.")
    else:
        print("Installed applications backup not found.")

# Restore Gnome Settings
def restore_gnome_settings():
    gnome_settings_file = os.path.join(backup_dir, "gnome_settings_backup.txt")
    
    if os.path.exists(gnome_settings_file):
        # Use dconf to load the Gnome settings
        with open(gnome_settings_file, "r") as f:
            subprocess.run(["dconf", "load", "/"], stdin=f)
        print("Gnome settings restored successfully.")
    else:
        print("Gnome settings backup not found.")

# Execute all restores
if __name__ == "__main__":
    print("Starting restore process...")
    restore_apt_sources()
    restore_installed_applications()
    restore_gnome_settings()
    print("Restore process completed.")
