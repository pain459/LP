import cv2
import dlib
import numpy as np
import requests
from io import BytesIO
from scipy.spatial import distance as dist
import bz2
import os

# URL to the pre-trained model file (choose .dat or .bz2 URL)
MODEL_URL = "https://github.com/davisking/dlib-models/raw/master/shape_predictor_68_face_landmarks.dat.bz2"
TEMP_MODEL_PATH = "temp_shape_predictor.dat"

# Download the model file into memory
print("Downloading shape_predictor_68_face_landmarks.dat...")
response = requests.get(MODEL_URL, stream=True)
if response.status_code != 200:
    raise Exception("Error downloading the model file.")

# Check if the file is compressed or uncompressed
if MODEL_URL.endswith(".bz2"):
    print("Detected compressed model file (.bz2). Decompressing...")
    # Decompress the .bz2 content and write to temporary file
    compressed_data = BytesIO(response.content)
    with open(TEMP_MODEL_PATH, "wb") as f:
        f.write(bz2.decompress(compressed_data.getvalue()))
else:
    print("Detected uncompressed model file (.dat). Writing to temp file...")
    # Write uncompressed content directly to temporary file
    with open(TEMP_MODEL_PATH, "wb") as f:
        f.write(response.content)

# Load the shape predictor model from the temporary file
predictor = dlib.shape_predictor(TEMP_MODEL_PATH)

# Delete the temporary model file after loading
os.remove(TEMP_MODEL_PATH)

# Function to calculate Eye Aspect Ratio (EAR) for blink detection
def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Load dlib's face detector
detector = dlib.get_frontal_face_detector()

# Define constants for EAR calculation
(left_eye_start, left_eye_end) = (42, 48)
(right_eye_start, right_eye_end) = (36, 42)
eye_aspect_ratio_threshold = 0.25

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        landmarks = predictor(gray, face)

        left_eye = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(left_eye_start, left_eye_end)]
        right_eye = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(right_eye_start, right_eye_end)]

        left_ear = eye_aspect_ratio(left_eye)
        right_ear = eye_aspect_ratio(right_eye)
        ear = (left_ear + right_ear) / 2.0

        if ear < eye_aspect_ratio_threshold:
            cv2.putText(frame, "Blinking", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Eye Blink Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
