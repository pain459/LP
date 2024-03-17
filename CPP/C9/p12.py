# Functions can return other functions
def display():
    def message():
        return "How are you?"

    return message


fun = display()
print(fun)
print(fun())
