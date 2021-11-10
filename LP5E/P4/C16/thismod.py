# Other ways to access globals
# Does not work, to be fixed.

var = 99  # Global variable == module attribute

def local():
    var = 0  # Change local var


def glob1():
    global var  # Declaring global (normal)
    var += 1  # Change global var


def glob2():
    var = 0  # Change in local var


def glob3():
    var = 0
    import sys
    glob = sys.modules['thismod']
    glob.var += 1


def test():
    print(var)
    local(); glob1(); glob2(); glob3()
    print(var)