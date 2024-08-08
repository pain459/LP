import cv2
import pytesseract

def extract_numbers_from_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    new_numbers = set(filter(lambda x: x.isdigit(), text.split()))
    return new_numbers
