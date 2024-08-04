import matplotlib.pyplot as plt
import numpy as np

def koch_snowflake(order, scale=10):
    def koch_curve(order, p1, p2):
        if order == 0:
            return [p1, p2]
        
        p1 = np.array(p1)
        p2 = np.array(p2)
        
        # Divide the segment into three parts
        s = (p2 - p1) / 3
        p3 = p1 + s
        p5 = p2 - s
        
        # Calculate the apex of the equilateral triangle
        p4 = p3 + np.array([
            np.cos(np.pi / 3) * s[0] - np.sin(np.pi / 3) * s[1],
            np.sin(np.pi / 3) * s[0] + np.cos(np.pi / 3) * s[1]
        ])
        
        # Recursively apply the Koch curve to the four segments
        return (koch_curve(order - 1, p1, p3) +
                koch_curve(order - 1, p3, p4) +
                koch_curve(order - 1, p4, p5) +
                koch_curve(order - 1, p5, p2)[1:])
    
    # Initial equilateral triangle
    p1 = [0, 0]
    p2 = [scale, 0]
    p3 = [scale / 2, np.sin(np.pi / 3) * scale]
    
    # Generate the Koch Snowflake
    snowflake = (koch_curve(order, p1, p2) +
                 koch_curve(order, p2, p3) +
                 koch_curve(order, p3, p1)[1:])
    
    return snowflake

def plot_and_save_koch_snowflake(order, scale=10, filename=None):
    # Generate and plot the Koch Snowflake
    snowflake = koch_snowflake(order, scale)
    x, y = zip(*snowflake)

    plt.figure(figsize=(10, 10))
    plt.plot(x, y)
    plt.axis('equal')
    plt.title(f'Koch Snowflake of Order {order}')
    
    if filename:
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f'Saved high-resolution image as {filename}')
    else:
        plt.show()

# Parameters
order = 4
scale = 10
filename = 'koch_snowflake.png'  # Set to None if you don't want to save the image

# Plot and save the Koch Snowflake
plot_and_save_koch_snowflake(order, scale, filename)
