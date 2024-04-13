import time
import threading


def do_something(seconds):
    print(f'Sleeping for {seconds} second(s)...')
    time.sleep(seconds)
    print(f'Done sleeping for {seconds} second(s)...')


def main():
    t1 = time.perf_counter()
    threads = []
    for _ in range(10):
        # t = threading.Thread(target=do_something, args=(1.5,))
        t = threading.Thread(target=do_something, args=[1.5])
        t.start()
        threads.append(t)
    
    for thread in threads:
        thread.join()

    t2 = time.perf_counter()
    print(f'Finished in {round(t2 - t1, 2)} second(s)')
    

if __name__ == "__main__":
    main()