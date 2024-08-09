from PIL import Image
import pytesseract
import os

def preprocess_image(image):
    """
    Preprocess the image by converting it to grayscale and applying thresholding.
    """
    # Convert image to grayscale
    gray_image = image.convert('L')
    
    # Apply thresholding to binarize the image
    threshold_image = gray_image.point(lambda x: 0 if x < 128 else 255)
    
    return threshold_image

def image_to_text(image_path, output_text_file, lang='eng'):
    """
    Perform OCR on the image and save the extracted text to a text file.
    """
    # Load the image from the given path
    image = Image.open(image_path)
    
    # Preprocess the image
    processed_image = preprocess_image(image)
    
    # Perform OCR on the processed image
    extracted_text = pytesseract.image_to_string(processed_image, lang=lang)
    
    # Save the extracted text to a text file
    with open(output_text_file, 'w', encoding='utf-8') as text_file:
        text_file.write(extracted_text)
    
    print(f"Text extracted and saved to {output_text_file}")

def batch_process_images(input_folder, output_folder, lang='eng'):
    """
    Process all images in the input folder and save the extracted text to the output folder.
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Process each image in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            image_path = os.path.join(input_folder, filename)
            output_text_file = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")
            image_to_text(image_path, output_text_file, lang=lang)
            print(f"Processed {filename}")

# Example usage
if __name__ == "__main__":
    # Single image processing
    image_path = 'sample_ocr_1.jpg'  # Replace with your image file path
    output_text_file = 'output_text.txt'
    image_to_text(image_path, output_text_file, lang='eng')

    # # Batch processing
    # input_folder = 'input_images'  # Replace with your input folder path
    # output_folder = 'output_texts'  # Replace with your output folder path
    # batch_process_images(input_folder, output_folder, lang='eng+fra')  # Example for English and French
