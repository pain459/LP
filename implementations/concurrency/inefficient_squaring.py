import time


def square(x):
    return x * x


if __name__ == "__main__":
    time1 = time.time()
    numbers = [122, 2567, 3345, 4998, 54456]
    squared = []
    for i in numbers:
        squared.append(square(i))

    print(squared)
    time2 = time.time()
    elapsed_time = time2 - time1
    print(f'Elapsed time is {elapsed_time} seconds.')
