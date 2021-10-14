# Conditional.py

late = True
if late:
    print("I need to call my manager!")

# Conditional2.py
late = False
if late:
    print("I need to call my manager")
else:
    print("No need to call my manager...")

# A specialized else = elif
income = 150000000
if income < 10000:
    tax_coefficient = 0.0
elif income < 30000:
    tax_coefficient = 0.2
elif income < 100000:
    tax_coefficient = 0.35
else:
    tax_coefficient = 0.45

print('I will pay:', income * tax_coefficient, ' in taxes.')

# ternary operator
order_total = 274
discount = 25 if order_total > 100 else 0
print(order_total, discount)

# Looping
for i in [0, 1, 2, 3, 4]:
    print(i)

# Iterating over a range
list(range(10))
list(range(3, 8))
list(range(-10, 10, 4))

# Iterating over a sequence
surnames = ["Rivest", "Shamir", "Adleman"]
for i in range(len(surnames)):
    print(i, surnames[i])

# In Pythonic way
surnames = ["Rivest", "Shamir", "Adleman"]
for i in surnames:
    print(i)

# Using enum to get the position.
surnames = ["Rivest", "Shamir", "Adleman"]
for i, j in enumerate(surnames):
    print(i + 1, j)  # added one only to increment the counter.

# Iterating over multiple sequences.
# Traditional way
people = ['Conrad', 'Deepak', 'Heinrich', 'Tom']
ages = [29, 30, 34, 36]
for i in range(len(people)):
    person = people[i]
    age = ages[i]
    print(person, age)
# Pythonic way of doing the same.
people = ['Conrad', 'Deepak', 'Heinrich', 'Tom']
ages = [29, 30, 34, 36]
for i, j in enumerate(people):
    age = ages[i]
    print(j, age)
# Still not Pythonic as we are using positional argument on ages list.
# To make it even simpler, we will user zip function.
people = ['Conrad', 'Deepak', 'Heinrich', 'Tom']
ages = [29, 30, 34, 36]
for i, j in zip(people, ages):
    print(i, j)
# Expanding the previous assignment in explicit and implicit assignments.
# Explicit assignment based iteration.
people = ['Conrad', 'Deepak', 'Heinrich', 'Tom']
ages = [29, 30, 34, 36]
nationalities = ['Poland', 'India', 'South Africa', 'England']
for i, j, k in zip(people, ages, nationalities):  # this will return a tuple.
    print(i, j, k)
# Implicit assignment based on iteration.
people = ['Conrad', 'Deepak', 'Heinrich', 'Tom']
ages = [29, 30, 34, 36]
nationalities = ['Poland', 'India', 'South Africa', 'England']
for i in zip(people, ages, nationalities):
    j, k, l = i  # exploding the tuple to the body of the for loop.
    print(j, k, l)

# The while loop.
# Looping through until the condition is satisfied.
# 6 / 2 = 3 (remainder: 0)
# 3 / 2 = 1 (remainder: 1)
# 1 / 2 = 0 (remainder: 1)
# List of remainders: 0, 1, 1.
# Inverse is 1, 1, 0, which is also the binary representation of 6: 110
# Calculate the binary representation of number 39.  100111
n = 39
remainders = []
while n > 0:
    remainder = n % 2  # Remainder of division by 2
    remainders.insert(0, remainder)  # keeping track of reminders.
    # We are inserting every result at 0 index. Which is reverse by itself.
    n //= 2
print(remainders)

n = 1258600125521112252145012214
remainders.clear()
remainders = []
while n > 0:
    remainder = n % 2
    remainders.insert(0, remainder)
    n //= 2
print(remainders)  # returns the list of integers
# [1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0]
# Converting the list to int for o/p purposes.
strings = [str(i) for i in remainders]
print(strings)  # returns ['1', '1', '0', '0', '0', '1', '0', '0', '1', '0', '1', '0', '1', '0']
# technically a list of strings.
a_string = "".join(strings)  # Joining the strings into a single string.
an_integer = int(a_string)  # converting the string to int
print(an_integer)  # printing the int.

#  Writing this in more Pythonic way.
n = 39
remainders.clear()  # clearing any junk values
remainders = []
while n > 0:
    n, remainder = divmod(n, 2)
    # which is
    # called with a number and a divisor, and returns a tuple with the result of the integer
    # division and its remainder. For example, divmod(13, 5) would return (2, 3), and
    # indeed 5 * 2 + 3 = 13:
    remainders.insert(0, remainder)
# print(remainders)
strings = [str(i) for i in remainders]
# print(strings)
a_string = "".join(strings)  # Joining the strings into a single string.
an_integer = int(a_string)  # converting the string to int
print(an_integer)

# binary representation of the number using bin function
bin(124558545214521)

# example to increment. Multiple sequences while loop.
people = ['Conrad', 'Deepak', 'Heinrich', 'Tom']
ages = [29, 30, 34, 36]
position = 0
while position < len(people):
    person = people[position]
    age = ages[position]
    print(person, age)
    position += 1

# Break and continue statements.
# Applying discount based on expiry date.
from datetime import date, timedelta

today = date.today()
# print(today)  # returns 2021-09-07. Format yyyy-mm-dd
tomorrow = today + timedelta(days=1)  # today + 1 day is tomorrow.
# print(tomorrow)  # returns 2021-09-08. Format yyyy-mm-dd
products = [
    {'sku': '1', 'expiration_date': today, 'price': 100.0},
    {'sku': '2', 'expiration_date': tomorrow, 'price': 50},
    {'sku': '3', 'expiration_date': today, 'price': 20},
]
for product in products:
    if product['expiration_date'] != today:
        continue
    product['price'] *= 0.8  # equivalent to applying 20% discount
    print(
        'Price for sku', product['sku'],
        'is now', product['price'])

# Evaluating the break statement.
items = [0, None, 0.0, True, 0, 7]  # True and 7 evaluate to True.

found = False  # this is called flag
for item in items:
    print("Scanning item", item)
    if item:
        found = True  # we update the flag
        break
if found:  # we inspect the flag.
    print("At least one item evaluate to True")
else:
    print("All items evaluate to False")


# The special else clause.
# for.no.else
class DriverException(Exception):
    pass


people = [('James', 17), ('Kirk', 9), ('Lars', 13), ('Robert', 8)]
driver = None  # flag
for person, age in people:
    if age >= 18:
        driver = (person, age)
        break
if driver is None:
    raise DriverException("Driver not found")


# same condition and data as above. but using for.else
class DriverException(Exception):
    pass


people = [('James', 17), ('Kirk', 9), ('Lars', 13), ('Robert', 8)]
for person, age in people:
    if age >= 18:
        driver = (person, age)
        print(driver)
        break
else:
    raise DriverException('Driver not found')

# A prime generator
# inefficient way of writing, but just for concept.
primes = []  # This will contain the list of primes at the end.
upto = 100  # the limit to check
for n in range(2, upto + 1):  # upto + 1 as the range will calculate 1 less than the given range.
    is_prime = True  # flag, for each iteration for outer for.
    for divisor in range(2, n):
        if n % divisor == 0:
            is_prime == False
            break
    if is_prime:  # check on flag if it is True.
        primes.append(n)
print(primes)

# Beautifying the code with if else.
primes = []
upto = 100
for i in range(2, upto + 1):
    for j in range(2, i):
        if j % i == 0:
            break
    else:
        primes.append(i)
print(primes)

# declaring data as a dict and querying the same.
customers = [
    dict(id=2, total=200, coupon_code='F20'),
    dict(id=2, total=150, coupon_code='F50')
]
customers[0]['id']

discounts = {
    'F20': (0.0, 20.0),  # each value is (percent, fixed)
    'P30': (0.3, 0.0),
    'P50': (0.5, 0.0),
    'F15': (0.0, 15.0),
}
discounts.get('F20', (0.0, 0.0))

# using the above data to create a program
# This program will calculate the discount applied per input token.

customers = [
    dict(id=1, total=200, coupon_code='F20'),  # F20: fixed, £20
    dict(id=2, total=150, coupon_code='P30'),  # P30: percent, 30%
    dict(id=3, total=100, coupon_code='P50'),  # P50: percent, 50%
    dict(id=4, total=110, coupon_code='F15'),  # F15: fixed, £15
]
discounts = {
    'F20': (0.0, 20.0),  # each value is (percent, fixed)
    'P30': (0.3, 0.0),
    'P50': (0.5, 0.0),
    'F15': (0.0, 15.0),
}
for customer in customers:
    code = customer['coupon_code']
    percent, fixed = discounts.get(code, (0.0, 0.0))
    customer['discount'] = percent * customer['total'] + fixed  # adding new value into dictionary

for customer in customers:
    print(customer['id'], customer['total'], customer['discount'])

print(customers)


# itertools sneak peak
from itertools import count
for i in count(5, 3):
    if i > 100:
        break
    print(i, end=', ')

# Iterators terminating on the shortest input sequence.
from itertools import compress
data = range(10)
even_selector = [1, 0] * 10
odd_selector = [0, 1] * 10

even_numbers = list(compress(data, even_selector))
odd_numbers = list(compress(data, odd_selector))

print(odd_selector)
print(list(data))
print(odd_numbers)
print(even_numbers)


# Combinatoric generators
# Permutations
from itertools import permutations
print(list(permutations('ABC')))