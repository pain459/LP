import os
import cv2
import numpy as np
from tensorflow.keras.models import model_from_json  # Use TensorFlow's Keras here
from tensorflow.keras.preprocessing import image

# Define paths for model and cascade files
model_json_path = os.path.join("models", "fer.json")
model_weights_path = os.path.join("models", "fer.h5")
cascade_path = os.path.join("models", "haarcascade_frontalface_default.xml")

# Load the model architecture and weights
try:
    with open(model_json_path, "r") as json_file:
        model = model_from_json(json_file.read())
    model.load_weights(model_weights_path)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    exit()

# Load the Haar cascade for face detection
face_haar_cascade = cv2.CascadeClassifier(cascade_path)

# Initialize the camera
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, test_img = cap.read()
    if not ret:
        continue

    # Convert frame to grayscale
    gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)

    for (x, y, w, h) in faces_detected:
        # Draw rectangle around each face
        cv2.rectangle(test_img, (x, y), (x + w, y + h), (255, 0, 0), thickness=7)

        # Crop and preprocess the region of interest (face area)
        roi_gray = gray_img[y:y + w, x:x + h]
        roi_gray = cv2.resize(roi_gray, (48, 48))
        img_pixels = image.img_to_array(roi_gray)
        img_pixels = np.expand_dims(img_pixels, axis=0)
        img_pixels /= 255.0

        # Predict emotion
        predictions = model.predict(img_pixels)
        max_index = np.argmax(predictions[0])

        # Define emotion labels
        emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
        predicted_emotion = emotions[max_index]

        # Add the emotion label to the frame
        cv2.putText(test_img, predicted_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Resize and display the frame
    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow('Facial Emotion Analysis', resized_img)

    # Exit loop on 'q' key press
    if cv2.waitKey(10) == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
