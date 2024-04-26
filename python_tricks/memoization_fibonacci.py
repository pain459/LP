# memoization using a dictionary to store computed fibonacci numbers
fib_cache = {}

def fibonacci(n):
    # base case: return 0 for n = 0 and 1 for n = 1
    if n <= 1:
        return n
    
    # Check if fobonacci number for n is already computed
    if n in fib_cache:
        return fib_cache[n]
    
    # Compute fibonacci number for n recursively and store in the cache
    fib_cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fib_cache[n]

# test the memoized fibonacci number
print(fibonacci(10))