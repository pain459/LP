import time


def do_something():
    print('Sleeping for 1 second...')
    time.sleep(1)
    print('Done sleeping...')


def main():
    t1 = time.perf_counter()
    do_something()
    do_something()
    do_something()
    t2 = time.perf_counter()
    print(f'Finished in {round(t2 - t1, 2)} second(s)')
    

if __name__ == "__main__":
    main()