even_sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        even_sum += i
    else:
        pass
print(even_sum)

# method 2
even_sum_2 = 0
for i in range(2, 101, 2):
    even_sum_2 += i
print(even_sum_2)
