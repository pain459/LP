# multiprocessing by iteration
import time
import multiprocessing

start_time =  time.perf_counter()

def do_something():
    print('Sleep for 1 second...')
    time.sleep(1)
    print('Done sleeping for 1 second...')

# Empty list to store the processes
processes = []

# Trigger the process via iteration
for _ in range(10):
    p = multiprocessing.Process(target=do_something)
    p.start()
    processes.append(p)

# wait for process to complete via iteration
for process in processes:
    p.join()

end_time = time.perf_counter()


print(f'Finished in {round(end_time - start_time, 2)} second(s)...')