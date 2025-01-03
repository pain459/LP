import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time.
        result = func(*args, **kwargs)  # Call the original function.
        # time.sleep(1)
        end_time = time.time()  # Record the end time.
        print(f"Execution time of program: {func.__name__}:{end_time - start_time:.4f} seconds")
        return result  # Return the result of the orifinal function
    return wrapper


@time_it
def slow_function(seconds):
    print(f"Sleeping for {seconds} seconds...")
    time.sleep(seconds)
    print("Done sleeping.")


# Call the decorated function
slow_function(1)