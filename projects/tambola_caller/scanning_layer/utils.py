import cv2
import pytesseract
import logging

def extract_numbers_from_image(image_path):
    logging.debug(f"Reading image from {image_path}")
    img = cv2.imread(image_path)
    if img is None:
        logging.error(f"Failed to read image from {image_path}")
        return set()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    logging.debug("Converted image to grayscale")

    # Apply adaptive thresholding to preprocess the image
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    logging.debug("Applied adaptive thresholding")

    # Apply dilation and erosion to close gaps between lines of text
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dilated = cv2.dilate(thresh, kernel, iterations=1)
    eroded = cv2.erode(dilated, kernel, iterations=1)
    logging.debug("Applied dilation and erosion")

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    logging.debug(f"Found {len(contours)} contours")

    all_text = []
    for i, cnt in enumerate(contours):
        # Get the bounding box for each contour
        x, y, w, h = cv2.boundingRect(cnt)
        # Filter out small contours that are unlikely to be numbers
        if w > 15 and h > 15:
            roi = eroded[y:y+h, x:x+w]
            text = pytesseract.image_to_string(roi, config='--psm 8')
            logging.debug(f"Extracted text from ROI {i}: {text.strip()}")
            all_text.append(text.strip())

    logging.debug(f"All extracted text: {all_text}")

    # Filter out and return only unique numeric values
    numbers = set(filter(lambda x: x.isdigit(), all_text))
    logging.debug(f"Filtered numbers: {numbers}")

    return numbers
