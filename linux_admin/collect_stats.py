import os
import subprocess
from datetime import datetime

def run_command(command, sudo=False):
    if sudo:
        command = f"sudo {command}"
    return subprocess.run(command, shell=True, capture_output=True, text=True).stdout

def collect_system_info(output_file):
    tasks = [
        ("System Uptime", "uptime", False),
        ("System Load", "cat /proc/loadavg", False),
        ("Disk Usage", "df -h", False),
        ("Memory Usage", "free -m", False),
        ("CPU Information", "lscpu", False),
        ("Network Information", "ifconfig -a", False),
        ("Process Information", "ps aux", False),
        ("Logged In Users", "w", False),
        ("Kernel Messages (dmesg)", "dmesg", True),
        ("System Logs (/var/log/syslog)", "cat /var/log/syslog", False),
        ("System Configuration (/etc/hosts)", "cat /etc/hosts", False),
        ("System Configuration (/etc/resolv.conf)", "cat /etc/resolv.conf", False),
        ("System Configuration (/etc/fstab)", "cat /etc/fstab", False),
        ("System Configuration (/etc/passwd)", "cat /etc/passwd", False),
        ("System Configuration (/etc/group)", "cat /etc/group", False),
        ("Network Configuration (Routing Table)", "route -n", True),
        ("Network Configuration (ARP Table)", "arp -a", True),
        ("Network Configuration (Firewall Rules)", "iptables -L", True),
        ("User Information", "cat /etc/passwd", False),
        ("Group Information", "cat /etc/group", False),
        ("System Processes (Process Tree)", "pstree", False),
        ("System Services (Status)", "systemctl status", True),
        ("System Services (Enabled/Disabled)", "systemctl list-unit-files", True),
        ("Hardware Information", "lshw", True),
        ("Connected Hardware Devices (USB)", "lsusb", True),
        ("Connected Hardware Devices (PCI)", "lspci", True),
        ("Kernel Version", "uname -a", False),
        ("Kernel Modules", "lsmod", False),
        ("File System Type and Usage", "mount", True),
        ("File System Check Status", "fsck -n", True),
        ("Last Login Information", "last", True),
        ("Security Logs", "cat /var/log/auth.log", True),
        ("Installed Packages", "dpkg -l", True),
        ("Environment Variables", "env", False)
    ]

    with open(output_file, 'w') as f:
        f.write(f"System Information Collection: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=========================================\n\n")

        for task_name, command, sudo in tasks:
            print(f"Running task: {task_name}")
            f.write(f"{task_name}:\n")
            f.write(run_command(command, sudo) + "\n\n")

        print(f"System information collected and saved to {output_file}")

if __name__ == "__main__":
    output_file = "system_info.txt"
    collect_system_info(output_file)
