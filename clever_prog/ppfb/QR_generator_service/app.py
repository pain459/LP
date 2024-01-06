from flask import Flask, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    url = request.form.get('url')
    if not url:
        return "Please provide a URL.", 400

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
