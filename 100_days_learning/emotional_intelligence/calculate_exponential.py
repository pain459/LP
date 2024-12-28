import math

def calculate_e_to_x(x, epsilon=1e-6):
    result = 0
    term = 1 # First term (1 / 0!)
    n = 0

    while term > epsilon:
        result += term
        n += 1
        term = (x**n) / math.factorial(n)  # compute next term

    return result


# calculate e^2
approx_e2= calculate_e_to_x(2, epsilon=1e-6)
print(f'Approximation of e^2: {approx_e2}')
print(f'Actual value of e^2: {math.exp(2)}')