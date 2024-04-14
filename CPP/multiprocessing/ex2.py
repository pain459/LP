# multiprocessing introduced.
import time
import multiprocessing

start_time =  time.perf_counter()

def do_something():
    print('Sleep for 1 second...')
    time.sleep(1)
    print('Done sleeping for 1 second...')

# Create processes
p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

# Start the processes
p1.start()
p2.start()

# wait for compeltion.
p1.join()
p2.join()

end_time = time.perf_counter()


print(f'Finished in {round(end_time - start_time, 2)} second(s)...')