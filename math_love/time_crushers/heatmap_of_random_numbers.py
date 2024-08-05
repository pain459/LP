import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def create_heatmap(size=(10, 10), title="Heatmap of Random Numbers", cmap="viridis"):
    """
    Creates and displays a heatmap of random numbers.
    
    Parameters:
    size (tuple): Size of the heatmap (number of rows, number of columns).
    title (str): Title of the heatmap.
    cmap (str): Colormap to use for the heatmap.
    """
    # Generate random numbers
    data = np.random.rand(*size)
    
    # Create the heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(data, annot=True, fmt=".2f", cmap=cmap)
    
    # Add title and labels
    plt.title(title)
    plt.xlabel("Columns")
    plt.ylabel("Rows")
    
    # Show the heatmap
    plt.show()

# Create a heatmap of size 10x10
create_heatmap(size=(10, 10), title="Heatmap of Random Numbers", cmap="viridis")
