import multiprocessing


# Define a square of a number
def square(x):
    return x * x


if __name__ == "__main__":
    # Define a list of numbers
    numbers = [1, 2, 3, 4, 5]
    # Create a multiprocessing tool
    with multiprocessing.Pool() as pool:
        # Use the map method to apply square function for each number in parallel.
        squared = pool.map(square, numbers)
    # Print the results
    print(squared)
    # Program completion message.
    print("Program completed.")
