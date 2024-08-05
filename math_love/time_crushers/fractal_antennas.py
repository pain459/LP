import matplotlib.pyplot as plt
import numpy as np

def sierpinski_triangle(order, scale=10):
    def midpoint(p1, p2):
        return (p1 + p2) / 2

    def sierpinski(order, p1, p2, p3):
        if order == 0:
            return [p1, p2, p3, p1]
        else:
            p12 = midpoint(p1, p2)
            p23 = midpoint(p2, p3)
            p31 = midpoint(p3, p1)
            return (sierpinski(order-1, p1, p12, p31) +
                    sierpinski(order-1, p12, p2, p23) +
                    sierpinski(order-1, p31, p23, p3))

    # Initial equilateral triangle
    p1 = np.array([0, 0])
    p2 = np.array([scale, 0])
    p3 = np.array([scale / 2, np.sin(np.pi / 3) * scale])

    # Generate the Sierpinski triangle
    points = sierpinski(order, p1, p2, p3)
    x, y = zip(*points)

    return x, y

def plot_and_save_sierpinski_triangle(order, scale=10, filename=None):
    x, y = sierpinski_triangle(order, scale)

    plt.figure(figsize=(10, 10))
    plt.plot(x, y)
    plt.axis('equal')
    plt.axis('off')
    plt.title(f'Sierpinski Triangle of Order {order}')

    if filename:
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f'Saved high-resolution image as {filename}')
    else:
        plt.show()

# Parameters
order = 10
scale = 20
filename = 'sierpinski_triangle.png'  # Set to None if you don't want to save the image

# Plot and save the Sierpinski Triangle
plot_and_save_sierpinski_triangle(order, scale, filename)
