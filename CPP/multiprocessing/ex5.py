# multiprocessing with ProcessPoolExecutor
import time
import concurrent.futures

start_time =  time.perf_counter()

def do_something(seconds):
    print(f'Sleep for {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done sleeping for {seconds} second(s)...'


def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1 = executor.submit(do_something, 1.5)
        print(f1.result())

    end_time = time.perf_counter()
    # Script time calculation
    print(f'Finished in {round(end_time - start_time, 2)} second(s)...')


if __name__ == "__main__":
    main()