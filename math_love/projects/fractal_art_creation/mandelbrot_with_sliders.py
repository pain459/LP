import ipywidgets as widgets
from IPython.display import display
from basic_implementation import generate_fractal
import matplotlib as plt
import numpy as np

# Define parameters for the fractal
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 800, 800
max_iter = 1000

def plot_fractal(xmin, xmax, ymin, ymax):
    fractal = generate_fractal(xmin, xmax, ymin, ymax, width, height, max_iter)
    plt.imshow(fractal.T, extent=[xmin, xmax, ymin, ymax], cmap='hot')
    plt.colorbar()
    plt.title('Mandelbrot Set')
    plt.show()

xmin_slider = widgets.FloatSlider(value=-2.0, min=-2.5, max=1.5, step=0.01, description='xmin')
xmax_slider = widgets.FloatSlider(value=1.0, min=-2.0, max=2.0, step=0.01, description='xmax')
ymin_slider = widgets.FloatSlider(value=-1.5, min=-2.0, max=2.0, step=0.01, description='ymin')
ymax_slider = widgets.FloatSlider(value=1.5, min=-2.0, max=2.0, step=0.01, description='ymax')

ui = widgets.HBox([xmin_slider, xmax_slider, ymin_slider, ymax_slider])
out = widgets.interactive_output(plot_fractal, {'xmin': xmin_slider, 'xmax': xmax_slider, 'ymin': ymin_slider, 'ymax': ymax_slider})

display(ui, out)
