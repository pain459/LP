# Functions with more than 1 input.

def greet_with(userName, userAge):
    print(f'Hello {userName}!')
    print(f'Your age is {userAge}')

greet_with('RRR', 23)
greet_with(userAge=24, userName='RRR')  # calling with keyword arguments.
greet_with('RRR', userAge=25)
# greet_with(userName='RRR', 26)  # This should give an error. Positional argument follows a keyword argument.

# Some example.
def locations(*args):
    print(f'loc1 {args}')
    print(f'loc2 {args}')
    print(f'loc3 {args}')

locations(1)