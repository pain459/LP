# generate random numbers between 100 and 200 every 3.5 secs
import time, random

# set seed
random.seed(10)
# Generate 10 numbers
for i in range(10):
    num = random.randrange(start=100, stop=200, step=12)
    print(num)
    time.sleep(1)