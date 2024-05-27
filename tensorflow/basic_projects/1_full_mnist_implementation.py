import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

# Load the trained model
model = load_model('/home/ravik/src_git/LP/tensorflow/basic_projects/mnist_model_advanced.h5')

# Function to preprocess new images
def preprocess_image(image_path):
    img = Image.open(image_path).convert('L')  # Convert to grayscale
    img = img.resize((28, 28))  # Resize to 28x28 pixels
    img = np.array(img) / 255.0  # Normalize pixel values
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

# Path to the new image
image_path = '/home/ravik/src_git/LP/tensorflow/basic_projects/image.png'

# Preprocess the image
new_image = preprocess_image(image_path)

# Predict the digit
prediction = model.predict(new_image)
predicted_digit = np.argmax(prediction, axis=1)
print('Predicted digit:', predicted_digit[0])
