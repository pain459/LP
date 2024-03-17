# define a function inside a function
def display(str):
    def message():
        return "How are you? "
    return message() + str


print(display('Pain'))