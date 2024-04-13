import time
import concurrent.futures


def do_something(seconds):
    print(f'Sleeping for {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done sleeping for {seconds} second(s)...'


def main():
    t1 = time.perf_counter()
    secs = [5, 4, 3, 2, 1]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # new_list = [expression for variable in iterable]
        threads = executor.map(do_something, secs)
        # Observer the pattern differences here in the output.
        for thread in threads:
            print(thread)

    t2 = time.perf_counter()
    print(f'Finished in {round(t2 - t1, 2)} second(s)')
    

if __name__ == "__main__":
    main()