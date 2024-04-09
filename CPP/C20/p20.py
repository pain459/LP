# To measure time taken by the program
from time import *

# note the starting time of the program
t1 = perf_counter()
p1 = process_time()

# do some processing
i, sum = 0, 0
while i < 100_000_000:
    sum += i
    i += 1

# make the processor or PVM sleep for 3 seconds.
# this will be also measured by perf_counter
sleep(3)

# note the ending time of the program
t2 = perf_counter()
p2 = process_time()

# Find the time for the program in seconds
print(f'Execution time using perf_counter = {t2 - t1}')
print(f'Execution time using process_counter = {p2 - p1}')