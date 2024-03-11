# Generate prime numbers using Fremats Little theorem.
# We will utilize the threadpool for executing these jobs.
# Fermats theorem a ** n-1 % n = 1
# If n is a prime number, then for every a, 1 ≤ a < n,
import concurrent.futures
import random
import time


def is_prime(n, k=5):
    # Test if number is prime using Fermats Little theorem
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    for _ in range(k):
        a = random.randint(2, n - 1)  # The range can be from 1 as well.
        if pow(a, n - 1, n) != 1:
            return False
    return True


def generate_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def main():
    start_time = time.time()
    # n = 133421334
    # result = is_prime(n)
    # if result:
    #     print(f'{n} is a prime number.')
    # else:
    #     print(f'{n} is not a prime number.')

    # generated_primes = generate_primes(2, 331)
    # print(generated_primes)
    # Create a threadpool with 5 workers.
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # submit the tasks to the threadpool.
        future_tasks = {executor.submit(generate_primes, 2, 200000): "Task 1",
                        executor.submit(generate_primes, 200001, 40000000): "Task 2"}

        # wait for the tasks to complete.
        for future in concurrent.futures.as_completed(future_tasks):
            task_name = future_tasks[future]
            try:
                result = future.result()
                print(f"{task_name} completed. Total primes found: {len(result)}")
            except Exception as e:
                print(f"{task_name} generated an exception: {e}")
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time} seconds.")


if __name__ == "__main__":
    main()
