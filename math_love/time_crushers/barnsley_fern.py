import matplotlib.pyplot as plt
import random

def barnsley_fern(num_points=100000):
    x, y = [0], [0]

    for _ in range(num_points):
        r = random.random()
        if r < 0.01:
            x_new, y_new = 0, 0.16 * y[-1]
        elif r < 0.86:
            x_new, y_new = 0.85 * x[-1] + 0.04 * y[-1], -0.04 * x[-1] + 0.85 * y[-1] + 1.6
        elif r < 0.93:
            x_new, y_new = 0.2 * x[-1] - 0.26 * y[-1], 0.23 * x[-1] + 0.22 * y[-1] + 1.6
        else:
            x_new, y_new = -0.15 * x[-1] + 0.28 * y[-1], 0.26 * x[-1] + 0.24 * y[-1] + 0.44

        x.append(x_new)
        y.append(y_new)

    return x, y

def plot_and_save_barnsley_fern(num_points=100000, filename=None):
    x, y = barnsley_fern(num_points)

    plt.figure(figsize=(10, 10))
    plt.scatter(x, y, s=0.1, color='green')
    plt.title('Barnsley Fern')
    plt.axis('off')

    if filename:
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f'Saved high-resolution image as {filename}')
    else:
        plt.show()

# Parameters
num_points = 100000
filename = 'barnsley_fern.png'  # Set to None if you don't want to save the image

# Plot and save the Barnsley Fern
plot_and_save_barnsley_fern(num_points, filename)
