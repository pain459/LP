from fastapi import FastAPI, UploadFile, File
from pyzbar.pyzbar import decode
from PIL import Image
from io import BytesIO

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    decoded_data = decode_qr_code(contents)
    return {"decoded_data": decoded_data}

def decode_qr_code(image_bytes):
    img = Image.open(BytesIO(image_bytes))
    decoded = decode(img)
    if decoded:
        return decoded[0].data.decode('utf-8')
    return "No QR code found"
