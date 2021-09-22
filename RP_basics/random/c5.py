# Numbers and Math
num1 = 1
print(type(num1))  # Will return <class 'int'>
num2 = int("25")
print(type(num2))  # Will return int as the conversion happened.
num3 = 1_000_000_000
print(num3)  # Just like JAVA. This will print without any _ characters.
# Floating-point numbers
f1 = 1.0
print(type(f1))  # Will return <class 'float'>
# exponential notations
f2 = 100000000000000000000000000000000.0
print(f2)  # Will return as 1e+32
f2 = 1e-4
print(f2)  # Will return 0.0001. This is technically 1/1000
# Float have maximum sizes. Depends on the system capabilities.
f3 = 2e400
print(f3)  # Will reply inf.
print(type(f3))  # Should return float. As default convention is float.
# Basic math.
x = 5.0
y = 2.0
print(x + y)
print(x - y)
print(x * y)
print(x % y)  # Modulus
print(x // y)  # Integer division. Weird with negative numbers.

# Math functions and number methods
c1 = round(2.3)
print(c1)  # A tie is any number whose last digit is 5. 2.5 and 3.1415 are ties, but 1.37 is not.
c1 = round(2.7)
print(c1)  # A tie is any number whose last digit is 5. 2.5 and 3.1415 are ties, but 1.37 is not.
c1 = round(3.1415, 2)
print(c1)  # Rounded by 2 decimal places.
c1 = round(2.715, 2)
print(c1)  # Error in floating point representation. Not a bug in round()

# Absolute function
x = -1.0
print(abs(x))  # Will return 1.0
x = 1.0
print(abs(x))  # Will return 1.0
x = -1
print(abs(x))  # will return 1 as the base value is in int.

# pow functon.
x = pow(2, 100)
print(x)  # equivalent to 2 ** 100
x = pow(2, -100)
print(x)  # equivalent to 2 ** (1/100)
# one more power of pow function.
x = pow(2, 3, 5)
print(x)  # equivalent to (2 ** 3) % 5

# check if the float is integral
num = 2.5
print(num.is_integer())  # return boolean response.

# printing numbers in style.
n = 7.125  # controlling the rounding with {number:.placef}
print(f"The value of n is {n}")
print(f"The value of n rounded 2 places is {n:.2f}")
print(f"The value of n rounded 1 place is {n:.1f}")
# experimenting with integers
n = 1
print(f"The value in n is {n}")  # prints 1
print(f"The value in n with 2 decimal places is {n:.2f}")  # printing 2 decimal places
print(type(f'{n:.2f}'))  # obviously this will be string.

# Inserting commas. Not a critical task, but good to know.
n = 1234567890
print(f'The value of n is {n:,}')

# inserting commas and working with decimals.
n = 123456.4524
print(f"The value of n is {n:,.2f}")  # This will print 123,456.45

# making currently values readable.
balance = 2000.0
spent = 256.35
balance = balance - spent
print(f"After spending ${spent:.2f}, I was left with ${balance:.2f}")

# making the most of % option in {}
ratio = 0.5
print(f"Thanos killed {ratio:.1%} population on earth.")  # % in {} will multiply
# the value by 100 and give specified decimal places.
# In short, display percentage with 2 decimal places.

# exercises
calc = 3 ** 0.125
print(f"Result is {calc:,.3f}")

money = 150000
print(f"I have ${money:,.2f} in my savings account")

p = 2 / 10
print(f"{p:.1%}")

# Complex numbers
n = 1 + 2j
print(n)  # python wraps the number as (1+2j)
print(n.real)  # should print 1.0
print(n.imag)  # should print 2.0
print(n.conjugate())  # should return the complex conjugate (1-2j). () is required at the end as this is a function.

# Playing with complex numbers.
a = 1 + 2j
b = 3 - 4j
j = 10  # This is not honoured as it is not part of the equation.
print(a + b)  # prints (4-2j)
print(a - b)  # prints (-2+6j)
print(a * b)  # prints (11+2j)
print(a / b)
print(a ** b)
# Modulus and floor division on complex numbers is not supported.

# Checking real and imaginary parts on integers.
x = 50
print(x.real)
print(x.imag)
print(x.conjugate())

