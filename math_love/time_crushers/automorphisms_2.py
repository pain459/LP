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

# Plot bubbles
for (x, y), value in zip(coprimes, values):
    circle = plt.Circle((x, y), radius=0.2, color=plt.cm.viridis(value / max(values)), alpha=0.6)
    ax.add_patch(circle)
    
# Connect the bubbles
for (x1, y1) in coprimes:
    for (x2, y2) in coprimes:
        if (x1, y1) != (x2, y2):
            ax.plot([x1, x2], [y1, y2], 'k-', lw=0.5, alpha=0.3)

ax.set_aspect('equal')
plt.xlim(-n-1, n+1)
plt.ylim(-n-1, n+1)

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
plt.title('Automorphisms of Binary Quadratic Forms with Connected Bubbles')
plt.show()
