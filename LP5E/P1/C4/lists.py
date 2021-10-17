L = [123, 'spam', 1.23]
len(L)
L[0]
L[:-1]

L + [4, 5, 6]  # [123, 'spam', 1.23, 4, 5, 6]
L  # [123, 'spam', 1.23]
L * 2  # [123, 'spam', 1.23, 123, 'spam', 1.23]

# Type specific operations

L = [123, 'spam', 1.23]
L.append('NI')
L  # [123, 'spam', 1.23, 'NI']
L.pop(2)  # will pop 1.23

M = ['bb', 'cc', 'aa']
M.sort()
M  # ['aa', 'bb', 'cc']
M.reverse()
M  # ['cc', 'bb', 'aa']

# Nesting
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
M[1]  # [4, 5, 6]
M[1][2]  # 6

# Comprehensions

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
col2 = [row[1] for row in M]  # Collect the items in column 2
col2  # [2, 5, 8]
# More list comprehensions
print([row[1] + 1 for row in M])  # [3, 6, 9]
print([row[1] for row in M if row[1] % 2 == 0])  # [2, 8]
print([e for row in M for e in row if e % 2 == 0])  # [2, 4, 6, 8]
print([M[i][i] for i in [0, 1, 2]])  # [1, 5, 9] diagonal numbers in a matrix
print([i * 2 for i in 'spam'])  # ['ss', 'pp', 'aa', 'mm']

list(range(4))  # [0, 1, 2, 3]
list(range(-6, 7, 2))  # [-6, -4, -2, 0, 2, 4, 6]
print([[x ** 2, x ** 3] for x in range(3)])  # [[0, 0], [1, 1], [4, 8]]
print([[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0])
# [[2, 1.0, 4], [4, 2.0, 8], [6, 3.0, 12]]
print([[i, int(i / 2), i * 2] for i in range(-6, 7, 2) if i > 0])
# [[2, 1, 4], [4, 2, 8], [6, 3, 12]]

# List comprehensions as a generator
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
G = (sum(i) for i in M)
next(G)  # Works 3 times for 3 rows.
# 4th will return StopIteration

# Demonstration of map, it is similar to generator
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

list(map(sum, M))  # we are saying sum of all items in the list. [6, 15, 24]
# Creating a set from comprehension
{sum(i) for i in M}  # {24, 6, 15}
# Creating a dictionary from comprehension
{i: sum(M[i]) for i in range(3)}  # {0: 6, 1: 15, 2: 24}
# few more examples
[ord(i) for i in 'spamm']
{ord(i) for i in 'spamm'}  # Sets remove duplicates
{i: ord(i) for i in 'spamm'}  # dictionary keys should be unique
(ord(i) for i in 'spamm')  # object created in memory.
