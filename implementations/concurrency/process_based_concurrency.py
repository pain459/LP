import multiprocessing
import time


# Define a square of a number
def square(x):
    return x * x


if __name__ == "__main__":
    time1 = time.time()
    # Define a list of numbers
    numbers = [122, 2567, 3345, 4998, 54456]
    # Create a multiprocessing tool
    with multiprocessing.Pool() as pool:
        # Use the map method to apply square function for each number in parallel.
        squared = pool.map(square, numbers)
    # Print the results
    print(squared)
    # Program completion message.
    print("Program completed.")
    time2 = time.time()
    elapsed_time = time2 - time1
    print(f'Elapsed time is {elapsed_time} seconds.')
