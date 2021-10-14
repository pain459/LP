# https://docs.python.org/3/library/operator.html?highlight=operators#mapping-operators-to-functions
import operator
a = 12
b = 3
s1 = "Hello"
s2 = "World"
seq1 = "Hello World! And welcome to python."
# Addition
print(a + b)  # 15
operator.add(a, b)  # 15
# concatenation
print(s1 + s2)  # HelloWorld
operator.concat(s1, s2)  # 'HelloWorld'
# Containment test
print(s1 in seq1)  # returns True
operator.contains(seq1, s1)  # return True
# Division
print(a / b)  # 4.0
operator.truediv(a, b)  # 4.0
# FloorDivision
print(a // b)  # 4
operator.floordiv(a, b)  # 4

# https://www.geeksforgeeks.org/python-bitwise-operators/
# Bitwise And
print(a & b)  # 0
operator.and_(a, b)  # 0
operator.and_(1, 1)  # 1
# Bitwise Exclusive Or
print(a ^ b)
print(10 ^ 4) #
operator.xor(1, 1)  # 0
# Bitwise Inversion
print(~ a)  # -13
print(~ 1)  # -2
print(~ 3)  # -4
operator.invert(3)  # -4
# Bitwise Or
print(a | b)  # 15
# Exponentiation
print(a ** b)  # 1728
# Identity
print(a is b)  # False
12 is 12  # True
operator.is_(12, 12)  # True
operator.is_not(12, 12)  # False
# Indexed assignment
l = [1, 2, 3]
l[0] = 2
print(l)  # [2, 2, 3]
operator.setitem(l, 2, 100)
print(l)  # [2, 2, 100]
# Indexed deletion
l = [1, 2, 3]
del l[0]
print(l)  # [2, 3]
# Indexing
l = [1, 2, 3]
l[0]  # 1
# left shift
a = 5
b = 1
print(a << b)
print(10 << 1)  # 20
# Right shift
print(10 >> 1)  # 5
print(10 >> 10)  # 0
# Modulo
a = 10
b = 5
print(a % b)  # 0
# Multiplication
a = 10
b = 5
print(a * b)  # 50
# Matrix multiplication
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
print(a @ b)
