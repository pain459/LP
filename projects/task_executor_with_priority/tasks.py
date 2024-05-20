import random
import time
import subprocess

def calculate():
    """Perform a basic arithmetic calculation with a random sleep to simulate processing time."""
    time.sleep(random.randint(1, 10))  # Random sleep between 1 and 10 seconds
    a, b = random.randint(1, 100), random.randint(1, 100)
    operation = random.choice(['+', '-', '*', '//'])
    result = eval(f"{a} {operation} {b}")
    print(f"Calculate: {a} {operation} {b} = {result}")
    return result

def ping():
    """Ping 'google.com' with a random sleep to simulate processing time."""
    time.sleep(random.randint(1, 10))  # Random sleep between 1 and 10 seconds
    host = "google.com"
    result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, text=True)
    print(f"Ping: {result.stdout}")
    return result.returncode == 0

def reverse_string():
    """Reverse a random string with a random sleep to simulate processing time."""
    time.sleep(random.randint(1, 10))  # Random sleep between 1 and 10 seconds
    s = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))
    reversed_s = s[::-1]
    print(f"Reverse String: {s} -> {reversed_s}")
    return reversed_s

def sum_numbers():
    """Calculate the sum of a random list of numbers with a random sleep to simulate processing time."""
    time.sleep(random.randint(1, 10))  # Random sleep between 1 and 10 seconds
    numbers = random.sample(range(1, 100), 10)
    total = sum(numbers)
    print(f"Sum Numbers: {numbers} -> Total = {total}")
    return total
