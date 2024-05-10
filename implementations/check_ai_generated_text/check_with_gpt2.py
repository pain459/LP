from transformers import pipeline
import torch

# Initialize the AI text detector model
def load_model():
    if torch.cuda.is_available():
        device = 0  # Use GPU if available
    else:
        device = -1  # Use CPU otherwise
    detector = pipeline("text-classification", model="mrm8488/GPT-2-output-dataset-detector", device=device)
    return detector

# Function to read text from a file
def read_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

# Function to check if the text is AI-generated
def check_if_ai_generated(text, model):
    result = model(text)
    return result

# Main function to load model, read file and check text
def main(file_path):
    detector_model = load_model()
    text = read_text(file_path)
    prediction = check_if_ai_generated(text, detector_model)
    return prediction

# Example usage
if __name__ == "__main__":
    file_path = 'path_to_your_text_file.txt'  # Replace with your text file path
    result = main(file_path)
    print("Prediction:", result)

