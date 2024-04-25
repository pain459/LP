import os
import subprocess
from datetime import datetime

def run_command(command, sudo=False):
    if sudo:
        command = f"sudo {command}"
    return subprocess.run(command, shell=True, capture_output=True, text=True).stdout

def collect_system_info(output_file):
    with open(output_file, 'w') as f:
        f.write(f"System Information Collection: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=========================================\n\n")

        # 1. System uptime
        f.write("1. System Uptime:\n")
        f.write(run_command("uptime") + "\n\n")

        # 2. System load
        f.write("2. System Load:\n")
        f.write(run_command("cat /proc/loadavg") + "\n\n")

        # 3. Disk usage
        f.write("3. Disk Usage:\n")
        f.write(run_command("df -h") + "\n\n")

        # 4. Memory usage
        f.write("4. Memory Usage:\n")
        f.write(run_command("free -m") + "\n\n")

        # 5. CPU information
        f.write("5. CPU Information:\n")
        f.write(run_command("lscpu") + "\n\n")

        # 6. Network information
        f.write("6. Network Information:\n")
        f.write(run_command("ifconfig -a") + "\n\n")

        # 7. Process information
        f.write("7. Process Information:\n")
        f.write(run_command("ps aux") + "\n\n")

        # 8. Logged in users
        f.write("8. Logged In Users:\n")
        f.write(run_command("w") + "\n\n")

        # 9. Kernel messages
        f.write("9. Kernel Messages (dmesg):\n")
        f.write(run_command("dmesg", sudo=True) + "\n\n")

        # 10. System logs
        f.write("10. System Logs (/var/log/syslog):\n")
        f.write(run_command("cat /var/log/syslog") + "\n\n")

        # 11. Additional custom commands or logs you may need
        # Add your custom commands or logs here as needed

        print(f"System information collected and saved to {output_file}")

if __name__ == "__main__":
    output_file = "system_info.txt"
    collect_system_info(output_file)
