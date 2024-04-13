import time
import concurrent.futures


def do_something(seconds):
    print(f'Sleeping for {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done sleeping for {seconds} second(s)...'


def main():
    t1 = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        f1 = executor.submit(do_something, 1.5)
        f2 = executor.submit(do_something, 1.5)

        print(f1.result())
        print(f2.result())

    t2 = time.perf_counter()
    print(f'Finished in {round(t2 - t1, 2)} second(s)')
    

if __name__ == "__main__":
    main()