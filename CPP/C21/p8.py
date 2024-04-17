# multitasking using 2 threads
from threading import *
from time import *

class Theatre:
    # Constructor that accepts a string
    def __init__ (self, str):
        self.str = str

    # a method that repeats for 5 tickets
    def movieshow(self):
        for i in range(1, 6):
            print(f'{self.str} : {i}')
            sleep(0.3)

# Create 2 instances to Theatre class
obj1 = Theatre('cut tickets')
obj2 = Theatre('show chair')

# Create two threads to run movieshow()
t1 = Thread(target=obj1.movieshow)
t2 = Thread(target=obj2.movieshow)

# run the methods
t1.start()
t2.start()