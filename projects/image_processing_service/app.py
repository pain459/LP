from flask import Flask, render_template, request, send_file
import cv2
import numpy as np
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    
    img_bytes = file.read()
    npimg = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_GRAYSCALE)  # Read as grayscale image

    # Check if the grayscale image has two dimensions
    if len(img.shape) != 2:
        return "Invalid image format"

    # Convert grayscale image to color using colormap
    color_img = cv2.applyColorMap(img, cv2.COLORMAP_JET)

    # Convert numpy array back to bytes
    _, img_encoded = cv2.imencode('.jpg', color_img)
    img_bytes = img_encoded.tobytes()

    return send_file(io.BytesIO(img_bytes), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
