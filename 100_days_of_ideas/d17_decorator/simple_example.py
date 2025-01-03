# Define a simple decorator
def greet_decorator(func):
    def wrapper():
        print("Hello!")  # Add a new functionality
        func()  # Call the original function
    return wrapper


# use the decorator
@greet_decorator
def say_name():
    print("My name is Python!")

# call the decorated function.
say_name()