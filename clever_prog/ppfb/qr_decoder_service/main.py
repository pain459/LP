from fastapi import FastAPI, UploadFile, File, HTTPException
from pyzbar.pyzbar import decode
from PIL import Image
from io import BytesIO

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    decoded_data = decode_qr_code(contents)
    if not decoded_data:
        raise HTTPException(status_code=404, detail="No QR code found")
    print("Decoded Data:", decoded_data[0].data.decode('utf-8'))
    return {"decoded_data": decoded_data[0].data.decode('utf-8')}

def decode_qr_code(image_bytes):
    img = Image.open(BytesIO(image_bytes))
    return decode(img)
