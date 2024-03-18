# A function to find the total and average
def calculate(lst):
    """To find the total and average"""
    n = len(lst)
    total = 0
    for i in range(n):
        total += i
    average = total / n
    return total, average


print("Enter numbers separated by space: ")
x = [int(i) for i in input().split()]

total, average = calculate(x)
print(f'Entered values in list: {x}')
print(f'Total of the inputs = {total}')
print(f'Average of the inputs = {average}')