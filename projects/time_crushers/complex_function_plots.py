import numpy as np
import matplotlib.pyplot as plt

def plot_functions(functions, x_range, title="Complex Function Plots", xlabel="X-axis", ylabel="Y-axis", grid=True):
    """
    Plots multiple functions on a single graph.
    
    Parameters:
    functions (list of dict): List of dictionaries where each dictionary defines a function to plot.
                              Each dictionary should have keys: 'func', 'label', and 'color'.
                              'func' is a lambda function, 'label' is the label for the legend, and 'color' is the plot color.
    x_range (tuple): A tuple defining the range of x values (start, end).
    title (str): Title of the plot.
    xlabel (str): Label for the x-axis.
    ylabel (str): Label for the y-axis.
    grid (bool): Whether to show the grid.
    """
    x = np.linspace(x_range[0], x_range[1], 1000)
    
    plt.figure(figsize=(10, 6))
    
    for function in functions:
        y = function['func'](x)
        plt.plot(x, y, label=function['label'], color=function['color'])
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(grid)
    plt.show()

# Define the functions to plot
functions = [
    {'func': lambda x: np.sin(x), 'label': 'sin(x)', 'color': 'blue'},
    {'func': lambda x: np.cos(x), 'label': 'cos(x)', 'color': 'green'},
    {'func': lambda x: np.exp(x), 'label': 'exp(x)', 'color': 'red'},
    {'func': lambda x: np.log(x), 'label': 'log(x)', 'color': 'purple'}
]

# Define the range for x values
x_range = (0.1, 10)

# Call the plot function
plot_functions(functions, x_range, title="Complex Function Plots", xlabel="X values", ylabel="Y values")
