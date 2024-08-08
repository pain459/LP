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
    text = pytesseract.image_to_string(gray)
    logging.debug(f"Extracted text: {text}")

    new_numbers = set(filter(lambda x: x.isdigit(), text.split()))
    logging.debug(f"Filtered numbers: {new_numbers}")

    return new_numbers
