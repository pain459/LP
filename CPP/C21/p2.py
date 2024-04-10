# Creating a thread without using a class
from threading import *


# Create a function
def display():
    print('Hello, I\'m running')


# Create a thread and run the function for 5 times
for i in range(5):
    # Create the thread and specify the function as its target
    t = Thread(target=display)
    # run the thread
    t.start()