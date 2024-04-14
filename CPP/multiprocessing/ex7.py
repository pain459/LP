# multiprocessing with ProcessPoolExecutor and as_completed to yield results
# Custom seconds passed via list.
import time
import concurrent.futures

start_time =  time.perf_counter()

def do_something(seconds):
    print(f'Sleep for {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done sleeping for {seconds} second(s)...'


def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        processes = [executor.submit(do_something, sec) for sec in secs]

        for f in concurrent.futures.as_completed(processes):
            print(f.result())

    end_time = time.perf_counter()
    # Script time calculation
    print(f'Finished in {round(end_time - start_time, 2)} second(s)...')


if __name__ == "__main__":
    main()