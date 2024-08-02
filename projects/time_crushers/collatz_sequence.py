import matplotlib.pyplot as plt

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def plot_collatz_sequence(n):
    sequence = collatz_sequence(n)
    plt.figure(figsize=(10, 6))
    plt.plot(sequence, marker='o')
    plt.title(f"Collatz Sequence for {n}")
    plt.xlabel("Step")
    plt.ylabel("Value")
    plt.grid(True)
    plt.show()

# Test with a number
plot_collatz_sequence(201)
