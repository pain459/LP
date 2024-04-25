from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Load pre-trained MobileNet model
model = tf.keras.applications.MobileNetV2(weights='imagenet', include_top=True)

# Preprocess input image
def preprocess_image(image):
    img = image.resize((224, 224))  # Resize image to match MobileNet input size
    img = np.array(img) / 255.0  # Normalize pixel values
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    img = Image.open(file)
    img = preprocess_image(img)

    # Predict class probabilities
    predictions = model.predict(img)

    # Decode predictions
    decoded_predictions = tf.keras.applications.imagenet_utils.decode_predictions(predictions)

    # Format predictions as JSON
    results = []
    for _, label, prob in decoded_predictions[0]:
        results.append({'label': label, 'probability': float(prob)})
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
