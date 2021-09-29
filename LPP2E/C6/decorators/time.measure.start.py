from time import sleep, time

def f():
    sleep(.3)  # sleep for 0.3 seconds

def g():
    sleep(.5)  # sleep for 0.5 seconds

t = time()
f()
print('f took:', time() - t)

t = time()
g()
print('g took', time() - t)