# abstract class works like an interface
from abc import *


class Myclass(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass


# this is a subclass
class Oracle(Myclass):
    def connect(self):
        print('Connecting to Oracle database...')

    def disconnect(self):
        print('Disconnected from Oracle...')


class Sybase(Myclass):
    def connect(self):
        print('Connecting to Sybase database...')

    def disconnect(self):
        print('Disconnected from Sybase...')


class Database:
    # Accept database name as a string
    str = input('Enter the database name: ')

    # Convert the string into class name
    classname = globals()[str]

    # Create an object to that class
    x = classname()

    # call the connect() and disconnect() methods
    x.connect()
    x.disconnect()
