import easyocr
import logging

# Initialize EasyOCR Reader
reader = easyocr.Reader(['en'])

def extract_numbers_from_image(image_path):
    logging.debug(f"Reading image from {image_path}")

    # Use EasyOCR to read text from the image
    result = reader.readtext(image_path)
    logging.debug(f"Raw OCR result: {result}")

    # Extract text from the result
    extracted_text = [text for _, text, _ in result]
    logging.debug(f"Extracted text: {extracted_text}")

    # Filter out and return only unique numeric values
    numbers = set(filter(lambda x: x.isdigit(), extracted_text))
    logging.debug(f"Filtered numbers: {numbers}")

    return numbers
