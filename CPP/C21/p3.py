# Creating a thread without using a class - v2.0

from threading import *


# create a function
def display(str):
    print(str)


# Create a thread and run the function for 5 times
for i in range(5):
    t = Thread(target=display, args=('Hello', ))
    t.start()