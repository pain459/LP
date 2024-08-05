import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            n3[i, j] = mandelbrot(r1[i] + 1j*r2[j], max_iter)
    return (r1, r2, n3)

# Animation function
def update(frame):
    global zoom
    zoom *= 0.9
    xmin, xmax = -2.0 / zoom, 1.0 / zoom
    ymin, ymax = -1.5 / zoom, 1.5 / zoom
    r1, r2, n3 = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    ax.clear()
    ax.imshow(n3.T, extent=[xmin, xmax, ymin, ymax], cmap='hot')
    ax.set_title('Mandelbrot Set Zoom')

zoom = 1.0
width, height = 800, 800
max_iter = 256

fig, ax = plt.subplots(figsize=(10, 10))
ani = FuncAnimation(fig, update, frames=100, interval=100)
ani.save('/tmp/mandelbrot_zoom.mp4', writer='ffmpeg', fps=10)

plt.close(fig)
