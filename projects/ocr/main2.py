import cv2
import numpy as np
from PIL import Image
import pytesseract
import os

def preprocess_image_for_numbers(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to remove noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Apply binary thresholding
    _, thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY_INV)
    
    return thresh, image

def extract_boxes(thresh, original_image):
    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    boxes = []
    
    for contour in contours:
        # Get the bounding box of each contour
        x, y, w, h = cv2.boundingRect(contour)
        
        # Filter out small contours that are unlikely to be a number
        if w > 15 and h > 15:
            # Extract the region of interest (the box)
            roi = original_image[y:y+h, x:x+w]
            
            # Store the bounding box
            boxes.append(roi)
    
    return boxes

def ocr_on_boxes(boxes):
    results = []
    
    for i, box in enumerate(boxes):
        # Convert the box to a PIL image
        pil_box = Image.fromarray(box)
        
        # Perform OCR on the box
        text = pytesseract.image_to_string(pil_box, config='--psm 8 digits')
        
        # Append the result
        results.append(text.strip())
    
    return results

def image_to_text_with_boxes(image_path, output_text_file):
    # Preprocess the image for number detection
    thresh, original_image = preprocess_image_for_numbers(image_path)
    
    # Extract boxes from the image
    boxes = extract_boxes(thresh, original_image)
    
    # Perform OCR on each box
    extracted_text = ocr_on_boxes(boxes)
    
    # Save the extracted text to a text file
    with open(output_text_file, 'w', encoding='utf-8') as text_file:
        for text in extracted_text:
            text_file.write(text + '\n')
    
    print(f"Text extracted and saved to {output_text_file}")

# Example usage
if __name__ == "__main__":
    image_path = 'sample1.jpg'  # Replace with your image file path
    output_text_file = 'output_numbers_main2.txt'
    image_to_text_with_boxes(image_path, output_text_file)
