# Using Least Significant Bit technique for encoding the image.

from PIL import Image

def encode_message(img_path, message, output_path):
    img = Image.open(img_path)
    encoded = img.copy()
    width, height = img.size
    index = 0
    message += '####'  # Delimiter to mark end of message

    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))
            for n in range(3):  # Iterate through R, G, B channels
                if index < len(message):
                    char_bin = format(ord(message[index]), '08b')
                    pixel[n] = int(format(pixel[n], '08b')[:-1] + char_bin[n % 8], 2)
                    if n % 8 == 7:
                        index += 1
                else:
                    break
            encoded.putpixel((col, row), tuple(pixel))
            if index >= len(message):
                break
        if index >= len(message):
            break

    encoded.save(output_path)

# Example usage
encode_message('/home/ravik/src_git/LP/projects/steganography/image.png', 'Hello, World!', 'encoded_image.png')
