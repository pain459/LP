import cv2
import numpy as np
import matplotlib.pyplot as plt

def draw_golden_ratio(image, num_rectangles=5):
    """
    Draw golden ratio rectangles and spirals on an image.
    
    Parameters:
    - image: Input image on which to draw the golden ratio pattern.
    - num_rectangles: Number of iterations for drawing the golden ratio pattern.
    """
    h, w, _ = image.shape
    min_dimension = min(h, w)
    
    # Calculate the scaling factor based on the golden ratio
    phi = (1 + np.sqrt(5)) / 2
    scale_factor = 1 / phi
    
    # Starting dimensions and position
    rect_w, rect_h = min_dimension, min_dimension
    x, y = (w - rect_w) // 2, (h - rect_h) // 2

    for i in range(num_rectangles):
        # Draw the rectangle
        cv2.rectangle(image, (x, y), (x + int(rect_w), y + int(rect_h)), (0, 255, 0), 2)
        
        # Draw the arc for the spiral
        if i % 4 == 0:
            center = (x + int(rect_w), y + int(rect_h))
            start_angle = 180
            end_angle = 270
        elif i % 4 == 1:
            center = (x, y + int(rect_h))
            start_angle = 270
            end_angle = 360
        elif i % 4 == 2:
            center = (x, y)
            start_angle = 0
            end_angle = 90
        else:
            center = (x + int(rect_w), y)
            start_angle = 90
            end_angle = 180

        axes = (int(rect_w), int(rect_h))
        cv2.ellipse(image, (int(center[0]), int(center[1])), (int(axes[0]), int(axes[1])), 0, start_angle, end_angle, (0, 255, 0), 2)
        
        # Update the coordinates and dimensions for the next rectangle
        if i % 4 == 0:
            x += int(rect_w * (1 - scale_factor))
        elif i % 4 == 1:
            y += int(rect_h * (1 - scale_factor))
        elif i % 4 == 2:
            x -= int(rect_w * scale_factor)
        elif i % 4 == 3:
            y -= int(rect_h * scale_factor)

        rect_w, rect_h = rect_w * scale_factor, rect_h * scale_factor

    return image

def process_image(input_image_path, output_image_path, num_rectangles=5):
    """
    Process the input image to overlay a golden ratio pattern.
    
    Parameters:
    - input_image_path: Path to the input image.
    - output_image_path: Path to save the output image.
    - num_rectangles: Number of iterations for drawing the golden ratio pattern.
    """
    # Read the input image
    image = cv2.imread(input_image_path)
    if image is None:
        print("Error: Could not load image")
        return
    
    # Draw the golden ratio pattern on the image
    image_with_golden_ratio = draw_golden_ratio(image, num_rectangles)
    
    # Save the output image
    cv2.imwrite(output_image_path, image_with_golden_ratio)
    
    # Convert the image to RGB (OpenCV uses BGR by default)
    image_rgb = cv2.cvtColor(image_with_golden_ratio, cv2.COLOR_BGR2RGB)
    
    # Display the image
    plt.imshow(image_rgb)
    plt.axis('off')
    plt.title('Golden Ratio Overlay')
    plt.show()

# Example usage
input_image_path = 'sample_hurricane2.jpg'  # Replace with your input image path
output_image_path = 'output_image_with_golden_ratio.jpg'  # Replace with your desired output image path

process_image(input_image_path, output_image_path, num_rectangles=5)
