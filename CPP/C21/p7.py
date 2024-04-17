# Single tasking using a single thread
from time import *
from threading import *

# Create your own class
class MyThread:

    def task1(self):
        print('Boil milk and tea powder for 5 minutes...', end='')
        sleep(5)
        print('Done')

    def task2(self):
        print('Add sugar and boil for 3 minutes...', end='')
        sleep(3)
        print('Done')

    def task3(self):
        print('Filter it and serve...', end='')
        print('Done')

    def prepareTea(self):
        self.task1()
        self.task2()
        self.task3()


# Create an instance to our class
obj = MyThread()

# Timer start
start_time = perf_counter()

# create a thread and run prepareTea method of obj
t1 = Thread(target=obj.prepareTea)
t1.start()
# t1.join()

end_time = perf_counter()

time_taken = round(end_time-start_time, 2)
print(f'TIme taken is {time_taken} second(s)...')