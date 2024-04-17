# A thread that accesses instance variables
from threading import *

# Create a class as subclass to thread class
class MyThread(Thread):

    # Constructor that calls thread class constructor
    def __init__ (self, str):
        Thread.__init__(self)
        self.str = str

    # Override the run() method of thread class
    def run(self):
        print(self.str)

# Create an instance of MyThread class and pass the string
t1 = MyThread('Hello')

# start running the thread
t1.start()

# wait till the thread completes execution
t1.join()