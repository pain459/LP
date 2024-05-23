# Using Least Significant Bit technique for decoding the image.


from PIL import Image

def decode_message(img_path):
    img = Image.open(img_path)
    width, height = img.size
    message = ''
    char_bin = ''

    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            for n in range(3):  # Iterate through R, G, B channels
                char_bin += format(pixel[n], '08b')[-1]
                if len(char_bin) == 8:
                    char = chr(int(char_bin, 2))
                    if char == '#':
                        return message
                    message += char
                    char_bin = ''

    return message

# Example usage
decoded_message = decode_message('/home/ravik/src_git/LP/projects/steganography/encoded_image.png')
print('Decoded message:', decoded_message)
