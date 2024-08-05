import numpy as np
import matplotlib.pyplot as plt

# Function to determine whether a point is in the Mandelbrot set
def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

# Generate the fractal
def generate_fractal(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width, height))
    
    for i in range(width):
        for j in range(height):
            n3[i, j] = mandelbrot(r1[i] + 1j*r2[j], max_iter)
    
    return n3

# Define parameters for the fractal
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 800, 800
max_iter = 1000

# Generate the fractal image
fractal = generate_fractal(xmin, xmax, ymin, ymax, width, height, max_iter)

# Display the fractal image
plt.imshow(fractal.T, extent=[xmin, xmax, ymin, ymax], cmap='hot')
plt.colorbar()
plt.title('Mandelbrot Set')
plt.show()
