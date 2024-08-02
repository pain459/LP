import matplotlib.pyplot as plt

def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

def plot_fibonacci_sequence(n):
    sequence = fibonacci_sequence(n)
    plt.figure(figsize=(10, 6))
    plt.plot(sequence, marker='o', linestyle='-', color='b')
    plt.title(f"Fibonacci Sequence (first {n} terms)")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(True)
    plt.show()

# Test with a number
plot_fibonacci_sequence(20)
