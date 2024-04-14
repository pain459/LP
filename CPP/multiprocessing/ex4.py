# multiprocessing with custom args
import time
import multiprocessing

start_time =  time.perf_counter()

def do_something(seconds):
    print(f'Sleep for {seconds} second(s)...')
    time.sleep(seconds)
    print(f'Done sleeping for {seconds} second(s)...')


def main():
    # Empty list to store the processes
    processes = []

    # Trigger the process via iteration
    for _ in range(1000):
        # p = multiprocessing.Process(target=do_something, args=[1.5])
        p = multiprocessing.Process(target=do_something, args=(1.5,))
        p.start()
        processes.append(p)

    # wait for process to complete via iteration
    for process in processes:
        p.join()

    end_time = time.perf_counter()
    # Script time calculation
    print(f'Finished in {round(end_time - start_time, 2)} second(s)...')


if __name__ == "__main__":
    main()