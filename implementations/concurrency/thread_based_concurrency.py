import threading
import time


# Function to simulate one task
def print_numbers():
    for i in range(6):
        print(f'Printing number {i}\n')
        time.sleep(1)


# Function to simulate another task
def print_letters():
    for i in "string":
        print(f'Printing letter {i}\n')
        time.sleep(1)


# Creating a thread object, one for each function.
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Starting the threads
thread1.start()
thread2.start()

# The main thread waits for both threads to finish.
thread1.join()
thread2.join()

print("Task completed.")
