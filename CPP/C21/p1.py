# Every python program is run by main thread

import threading
print('Let us find the current thread.')

# Find the name of the present thread
print(f'Currently running thread {threading.current_thread().name}')

# Check if it is main thread or not
if threading.current_thread() == threading.main_thread():
    print('The current thread is the main thread.')
else:
    print('The current thread is not the main thread.')