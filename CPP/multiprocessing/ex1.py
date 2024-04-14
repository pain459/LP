import time

start_time =  time.perf_counter()

def do_something():
    print('Sleep for 1 second...')
    time.sleep(1)
    print('Done sleeping for 1 second...')


do_something()

end_time = time.perf_counter()


print(f'Finished in {round(end_time - start_time, 2)} second(s)...')