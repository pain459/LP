import argparse
import paramiko
import os

def execute_remote_script(host, username, password, script_path):
    # Create SSH client
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to remote host
        ssh_client.connect(hostname=host, username=username, password=password)

        # Transfer the system information collection script to the remote host
        sftp_client = ssh_client.open_sftp()
        sftp_client.put(script_path, '/tmp/collect_stats.py')
        sftp_client.close()

        # Execute the system information collection script on the remote host
        stdin, stdout, stderr = ssh_client.exec_command('python3 /tmp/collect_stats.py')
        for line in stdout:
            print(line.strip())
        for line in stderr:
            print(line.strip())

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close SSH connection
        ssh_client.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Wrapper script to execute system information collection script on a remote machine.")
    parser.add_argument("--host", help="Remote host IP address or hostname", required=True)
    parser.add_argument("--username", help="Username for SSH login", required=True)
    parser.add_argument("--password", help="Password for SSH login")
    args = parser.parse_args()

    # Assuming the system information collection script is in the same directory as the wrapper script
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "collect_stats.py")

    # Execute the system information collection script on the remote host
    execute_remote_script(args.host, args.username, args.password, script_path)
