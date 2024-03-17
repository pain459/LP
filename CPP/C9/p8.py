# Function that returns multiple results
def sum_sub_mul_div(x, y):
    """This function returns the results of addition,
    subtraction, multiplication, division"""
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return a, b, c, d


result = sum_sub_mul_div(10, 20)  # Store results in a tuple
print(result)
for i in result:  # Unpack the tuple
    print(i)