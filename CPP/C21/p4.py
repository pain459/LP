# creating your own thread
from threading import Thread

# Create a class as sub class to Thread class
class MyThread(Thread):
    # override the run method of thread class
    def run(self):
        for i in range(1, 6):
            print(i)

# Create an instance of MyThread class
t1 = MyThread()

# Start running the thread t1
t1.start()

# Wait till thread completes execution.
t1.join()