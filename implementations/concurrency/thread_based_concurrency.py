import threading
import time
from loguru import logger

# logger.add("file_{time}.log", rotation="1 MB", enqueue=True)
logger.add("file_temp.log", rotation="1 MB", enqueue=True)


# Function to simulate one task
@logger.catch
def print_numbers():
    for i in range(10):
        print(f'Printing number {i}\n')
        time.sleep(1)


# Function to simulate another task
@logger.catch
def print_letters():
    for i in "string":
        print(f'Printing letter {i}\n')
        time.sleep(1)


# Creating a thread object, one for each function.
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)
logger.debug("Threads created!")

# Starting the threads
thread1.start()
thread2.start()
logger.debug("Threads started!")

# The main thread waits for both threads to finish.
thread1.join()
logger.debug("Thread1 completed.")
thread2.join()
logger.debug("Thread2 completed.")

print("Task completed.")
