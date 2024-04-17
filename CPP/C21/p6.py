# Create a thread without making sub class to thread class

from threading import *

# Create our own class
class MyThread:

    # A constructor
    def __init__ (self, str):
        self.str = str

    # a method
    def display(self, x, y):
        print(self.str)
        print(f'The args are {x} and {y}')

# Create an instance to our class and store 'Hello' string
obj = MyThread('Hello')

# Create a thread to run display method to obj
t1 = Thread(target=obj.display, args=(1, 2,))

# Start the command
t1.start()

# Wait for the thread to complete execution
t1.join()