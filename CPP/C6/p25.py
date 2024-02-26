# Use continue to execute next iteration of while loop.

x = 0
while x < 10:
    x += 1
    if x > 5:
        continue # will stop executing the next statements in this loop.
    print('x =', x)
print("out of loop!")