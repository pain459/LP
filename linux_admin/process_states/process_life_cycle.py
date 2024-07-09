import os
import time

def orphan_process():
    pid = os.fork()

    if pid > 0:
        # Parent process
        print(f"Parent process (PID: {os.getpid()}) is exiting to create an orphan process.")
        os._exit(0)
    else:
        # Child process
        time.sleep(2)  # Ensure the parent process terminates first
        print(f"Orphan process (PID: {os.getpid()}) has been adopted by init, new parent PID: {os.getppid()}")

def zombie_process():
    pid = os.fork()

    if pid > 0:
        # Parent process
        print(f"Parent process (PID: {os.getpid()}) creating a zombie process.")
        time.sleep(10)  # Parent sleeps while child becomes a zombie
        pid, status = os.wait()  # Collect the child process exit status
        print(f"Zombie process (PID: {pid}) has been reaped, exit status: {status}")
    else:
        # Child process
        print(f"Child process (PID: {os.getpid()}) is exiting to become a zombie.")
        os._exit(0)

def main():
    print("Simulating orphan process:")
    orphan_process()
    time.sleep(3)  # Wait to ensure orphan process output is displayed

    print("\nSimulating zombie process:")
    zombie_process()
    time.sleep(12)  # Wait to ensure zombie process output is displayed

if __name__ == "__main__":
    main()
