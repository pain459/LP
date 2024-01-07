from time import time

start = time()

# Python program to create acronyms
word = "Artificial Intelligence"
text = word.split()
a = ""
for i in text:
    a = a + str(i[0]).upper()
print(a)

# one more dummy piece of code to calculate the execution time.
x = 0
for j in range(100000000):
    x += j
print(x)

end = time()

execution_time = end - start
print("Execution time is: ", execution_time)