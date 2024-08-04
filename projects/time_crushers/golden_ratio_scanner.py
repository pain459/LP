import cv2
import numpy as np
import matplotlib.pyplot as plt

def draw_fibonacci_spiral(image, center, max_radius, num_turns):
    """
    Draw a Fibonacci spiral on an image.
    
    Parameters:
    - image: Input image on which to draw the spiral.
    - center: Tuple (x, y) for the center of the spiral.
    - max_radius: The maximum radius of the spiral.
    - num_turns: The number of turns in the spiral.
    """
    golden_ratio = (1 + np.sqrt(5)) / 2
    theta = np.linspace(0, 2 * np.pi * num_turns, 1000)
    radius = max_radius * np.exp(theta * np.log(golden_ratio) / (2 * np.pi * num_turns))
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    
    for i in range(len(x) - 1):
        cv2.line(image, (int(x[i]), int(y[i])), (int(x[i+1]), int(y[i+1])), (0, 255, 0), 2)

def process_image(input_image_path, output_image_path, num_turns=5):
    """
    Process the input image to overlay a Fibonacci spiral.
    
    Parameters:
    - input_image_path: Path to the input image.
    - output_image_path: Path to save the output image.
    - num_turns: Number of turns in the Fibonacci spiral.
    """
    # Read the input image
    image = cv2.imread(input_image_path)
    if image is None:
        print("Error: Could not load image")
        return
    
    # Convert the image to RGB (OpenCV uses BGR by default)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Define the center and maximum radius for the Fibonacci spiral
    center = (image.shape[1] // 2, image.shape[0] // 2)
    max_radius = min(center) // 2
    
    # Draw the Fibonacci spiral on the image
    draw_fibonacci_spiral(image_rgb, center, max_radius, num_turns)
    
    # Save the output image
    output_image_rgb = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)
    cv2.imwrite(output_image_path, output_image_rgb)
    
    # Display the image
    plt.imshow(image_rgb)
    plt.axis('off')
    plt.title('Fibonacci Spiral Overlay')
    plt.show()

# Example usage
input_image_path = 'input_image.jpg'  # Replace with your input image path
output_image_path = 'output_image_with_fibonacci_spiral.jpg'  # Replace with your desired output image path

process_image(input_image_path, output_image_path, num_turns=5)
