# This program will take the user input for username and validate the password.
# If possible we will try to create a new user and password dynamically too.

import getpass

def prompt_password():
    return getpass.getpass(prompt='Enter password: ')

_database = {"user1": "pass@123", "user2": "pass@456"}
_username = input("Enter the username: ")

if _username in _database:
    _password = prompt_password()

    while _password != _database[_username]:
        _password = prompt_password()

    print("Verified")
else:
    print("Username not found")

