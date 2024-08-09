import cv2
import numpy as np
from PIL import Image
import pytesseract
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def preprocess_image(image_path):
    # Load the image using OpenCV
    logging.info(f"Loading image: {image_path}")
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if image is None:
        logging.error(f"Failed to load image: {image_path}")
        return None, None

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply adaptive thresholding
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 11, 2)
    
    return thresh, image

def extract_boxes(thresh, original_image):
    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    boxes = []
    logging.info(f"Found {len(contours)} contours")

    for contour in contours:
        # Get the bounding box of each contour
        x, y, w, h = cv2.boundingRect(contour)
        
        # Filter out small contours that are unlikely to be a number
        if 40 < w < 100 and 40 < h < 100:  # Adjusted for the size of the boxes
            logging.info(f"Found box with dimensions: x={x}, y={y}, w={w}, h={h}")
            # Extract the region of interest (the box)
            roi = original_image[y:y+h, x:x+w]
            boxes.append(roi)
    
    return boxes

def ocr_on_boxes(boxes):
    results = []
    
    for i, box in enumerate(boxes):
        # Convert the box to a PIL image
        pil_box = Image.fromarray(box)
        
        # Perform OCR on the box, limiting to digits only
        custom_config = r'--oem 3 --psm 8 -c tessedit_char_whitelist=0123456789'
        text = pytesseract.image_to_string(pil_box, config=custom_config)
        logging.info(f"OCR result for box {i}: {text.strip()}")
        
        # Append the result
        results.append(text.strip())
    
    return results

def image_to_text_with_boxes(image_path, output_text_file):
    # Preprocess the image for number detection
    thresh, original_image = preprocess_image(image_path)
    
    if thresh is None or original_image is None:
        logging.error("Preprocessing failed; skipping OCR")
        return

    # Extract boxes from the image
    boxes = extract_boxes(thresh, original_image)
    
    if not boxes:
        logging.error("No valid boxes found; skipping OCR")
        return

    # Perform OCR on each box
    extracted_text = ocr_on_boxes(boxes)
    
    # Save the extracted text to a text file
    if extracted_text:
        with open(output_text_file, 'w', encoding='utf-8') as text_file:
            for text in extracted_text:
                text_file.write(text + '\n')
        logging.info(f"Text extracted and saved to {output_text_file}")
    else:
        logging.error("No text was extracted during OCR")

# Example usage
if __name__ == "__main__":
    image_path = 'sample1.jpg'  # Replace with your image file path
    output_text_file = 'output_numbers_main2.txt'
    image_to_text_with_boxes(image_path, output_text_file)
