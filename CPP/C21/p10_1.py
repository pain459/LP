# Thread synchronization using Semaphore

from threading import *
from time import *

class Railway:
    # Constructor that accepts number of available berths
    def __init__ (self, available):
        self.available = available
        # Create a lock object
        self.l = Semaphore()  # Using semaphore

    # A method that reservs berths
    def reserve(self, wanted):
        # Lock the current object
        self.l.acquire()
        # display number of available berths
        print(f'Available no. if berths = {self.available}')

        # if available >= wanted, allot the berth
        if self.available >= wanted:
            # Find the thread name
            name = current_thread().getName()
            # display berth is allocated to that person
            print(f'{wanted} berts allocated to {name}')
            # make time delay so the ticket is printed
            sleep(1.5)
            # Decrease the no. of available berths
            self.available -= wanted
        else:
            # if available < wanted, then say sorry
            print(f'Sorry, no berths to allot')
        # Task is completed, release the lock
        self.l.release()


# Create instance to Railway class
# Speficy only one berth available
obj = Railway(1)

# Create two threads and specify 1 berth is needed
t1 = Thread(target=obj.reserve, args=(1,))
t2 = Thread(target=obj.reserve, args=(1,))

# give names to the threads
t1.setName('First Person')
t2.setName('Second Person')

# Run the threads
t1.start()
t2.start()