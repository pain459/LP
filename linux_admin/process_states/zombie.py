import os
import time

def main():
    pid = os.fork()

    if pid > 0:
        # Parent process
        print(f"Parent process (PID: {os.getpid()}) sleeping")
        time.sleep(10)  # Child will be a zombie during this time
        print(f"Parent process (PID: {os.getpid()}) waking up")
        os.wait()  # Collect child process exit status
        print("Zombie child process has been reaped")
    else:
        # Child process
        print(f"Child process (PID: {os.getpid()}) is exiting")
        os._exit(0)

if __name__ == "__main__":
    main()
