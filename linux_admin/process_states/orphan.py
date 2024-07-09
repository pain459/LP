import os
import time

def main():
    pid = os.fork()

    if pid > 0:
        # Parent process
        print(f"Parent process (PID: {os.getpid()}) is exiting")
        os._exit(0)
    else:
        # Child process
        time.sleep(2)  # Ensure the parent terminates first
        print(f"Child process (PID: {os.getpid()}) has been orphaned, new parent PID: {os.getppid()}")

if __name__ == "__main__":
    main()
