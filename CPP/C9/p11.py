# function can be passed as a parameter to other functions
def display(fun):
    return "Hai " + fun


def message():
    return "How are you?"


print(display(message()))  # Return of message() is feeding as input for display()
