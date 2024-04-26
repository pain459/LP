# Using deque to append items to the queue on either sides.
from collections import deque

# Create a deque
my_deque = deque([1, 2, 3])

my_deque.append(4)
my_deque.append(5)

my_deque.appendleft(0)
my_deque.appendleft(-1)

print(my_deque)
print(list(my_deque))