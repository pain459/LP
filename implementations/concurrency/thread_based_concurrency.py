import threading
import time


def print_numbers():
    for i in range(6):
        print(f'Printing number {i}\n')
        time.sleep(1)


def print_letters():
    for i in "string":
        print(f'Printing letter {i}\n')
        time.sleep(1)


thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()


print("Task completed.")



