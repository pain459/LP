# Program to display fibonacci series

n = int(input("How many Fibonacci's ? "))
f1 = 0  # this is the first fibonacci
f2 = 1  # this is the second fibonacci
c = 2  # Counts the number fo Fibonacci's
if n == 1 or n == 2:
    print(f1, '\n', f2, sep='')
else:
    print(f1, '\n', f2, sep='')
    while c < n:
        f = f1 + f2
        print(f)
        f1, f2 = f2, f
        c += 1
