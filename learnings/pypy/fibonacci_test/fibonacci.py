import time

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def measure_time(n):
    start_time = time.time()
    result = fibonacci(n)
    end_time = time.time()
    print(f'Fibonacci of {n} is {result}')
    print(f'Time taken is {end_time - start_time} seconds.')


def main():
    n = 50
    measure_time(n)


if __name__ == "__main__":
    main()