import matplotlib.pyplot as plt
import numpy as np
from mpmath import mp

def generate_pi_digits(n):
    """Generate the first n digits of pi."""
    mp.dps = n + 1  # Set decimal places (n + 1 to include the leading 3)
    pi_str = str(mp.pi)[2:]  # Get pi digits as a string (excluding "3.")
    return pi_str

def plot_pi_spiral(pi_digits, n):
    """Plot the first n digits of pi in a spiral pattern."""
    fig, ax = plt.subplots(figsize=(10, 10), facecolor='black')
    ax.set_facecolor('black')
    
    # Parameters for the spiral
    a = 0.0001  # Initial radius
    b = 0.004  # Distance between turns
    theta = np.linspace(0, 4 * np.pi * n / 100, n)  # Angle in radians
    
    # Generate spiral coordinates
    r = a + b * theta
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    # Plot each digit
    for i, digit in enumerate(pi_digits):
        ax.text(x[i], y[i], digit, color='white', fontsize=8, ha='center', va='center')
    
    ax.axis('off')  # Turn off the axis
    plt.title(f'First {n} Decimal Places of π', color='white', fontsize=15)
    plt.show()

# Parameters
n = 1000  # Number of decimal places of pi to plot

# Generate pi digits
pi_digits = generate_pi_digits(n)

# Plot the pi spiral
plot_pi_spiral(pi_digits, n)
