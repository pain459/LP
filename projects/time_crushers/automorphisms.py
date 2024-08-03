import matplotlib.pyplot as plt
import numpy as np

# Define the quadratic form Q(x, y) = ax^2 + bxy + cy^2
def quadratic_form(a, b, c, x, y):
    return a*x**2 + b*x*y + c*y**2

# Generate coprime (x, y) pairs within a range
def generate_coprime_pairs(n):
    coprimes = []
    for x in range(-n, n+1):
        for y in range(-n, n+1):
            if np.gcd(x, y) == 1 and (x != 0 or y != 0):
                coprimes.append((x, y))
    return coprimes

# Parameters for the quadratic form
a, b, c = 1, 0, 1

# Range for coprime pairs
n = 10

# Generate the data
coprimes = generate_coprime_pairs(n)
values = [quadratic_form(a, b, c, x, y) for x, y in coprimes]

# Plotting
fig, ax = plt.subplots()
scatter = ax.scatter([x for x, y in coprimes], [y for x, y in coprimes], c=values, cmap='viridis')
plt.colorbar(scatter, label='Q(x, y)')

# Function to update the plot on click
def on_click(event):
    if event.inaxes:
        dx = event.xdata
        dy = event.ydata
        ax.set_xlim(ax.get_xlim() + dx)
        ax.set_ylim(ax.get_ylim() + dy)
        plt.draw()

# Connect the click event to the update function
cid = fig.canvas.mpl_connect('button_press_event', on_click)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Automorphisms of Binary Quadratic Forms')
plt.show()
