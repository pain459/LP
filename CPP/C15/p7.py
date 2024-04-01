# An interface to send text to any printer.
from abc import *


# Create an interface
class Printer(ABC):
    @abstractmethod
    def printit(self, text):
        pass

    @abstractmethod
    def disconnect(self):
        pass

# this is a subclass for IBM printer
class IBM(Printer):
    def printit(self, text):
        print(text)

    def disconnect(self):
        print('Printing complete on IBM printer.')

# this is a subclass for EPSON printer
class Epson(Printer):
    def printit(self, text):
        print(text)

    def disconnect(self):
        print('Printing complete on Epson printer.')


class UsePrinter:
    # accept printer name as a string from configuration file
    with open('file.txt', 'r') as f:
        str = f.readline()
    # Convert the string to classname
    classname = globals()[str]
    # Create an object to that clas
    x = classname()
    # Call the printit and disconnect methods
    x.printit('Hello this is sent to printer')
    x.disconnect()