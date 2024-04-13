import time
import threading


def do_something():
    print('Sleeping for 1 second...')
    time.sleep(1)
    print('Done sleeping...')


def main():
    t1 = time.perf_counter()
    threads = []
    for _ in range(10000):
        t = threading.Thread(target=do_something)
        t.start()
        threads.append(t)
    
    for thread in threads:
        thread.join()

    t2 = time.perf_counter()
    print(f'Finished in {round(t2 - t1, 2)} second(s)')
    

if __name__ == "__main__":
    main()