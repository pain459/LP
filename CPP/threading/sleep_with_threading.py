import time
import threading


def do_something():
    print('Sleeping for 1 sec...')
    time.sleep(1)
    print('Done sleeping...')


def main():
    start_time = time.perf_counter()
    # Create the threads
    t1 = threading.Thread(target=do_something)
    t2 = threading.Thread(target=do_something)
    t3 = threading.Thread(target=do_something)
    # Start the threads
    t1.start()
    t2.start()
    t3.start()
    # Wait to finish the threads
    t1.join()
    t2.join()
    t3.join()
    end_time = time.perf_counter()
    print(f'Script took {round(end_time - start_time, 2)} second(s)')


if __name__ == "__main__":
    main()