import concurrent.futures
import threading
import time


def task(task_number):
    print(f'Executing the task {task_number} by Thread {threading.current_thread().name}')
    time.sleep(2)


def main():
    # Create a threadpool with 5 workers.
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Submit the tasks to threadpool
        future_tasks = {executor.submit(task, i): i for i in range(20)}

        # Wait for all tasks to complete
        for future in concurrent.futures.as_completed(future_tasks):
            task_number = future_tasks[future]
            try:
                future.result()
            except Exception as e:
                print(f'Task {task_number} generated an exception: {e}')


if __name__ == '__main__':
    main()