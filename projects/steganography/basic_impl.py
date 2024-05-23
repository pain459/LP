from PIL import Image

def text_to_bits(text):
    bits = []
    for char in text:
        binval = bin(ord(char))[2:].rjust(8, '0')
        bits.extend([int(bit) for bit in binval])
    return bits

def bits_to_text(bits):
    chars = []
    for b in range(len(bits) // 8):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

def encode_image(image_path, message, output_path):
    image = Image.open(image_path)
    image = image.convert('RGB')
    pixels = list(image.getdata())
    
    bits = text_to_bits(message)
    bits.extend(text_to_bits('\x00'))  # Add a null character to mark the end of the message

    encoded_pixels = []
    bit_index = 0
    for pixel in pixels:
        if bit_index < len(bits):
            r, g, b = pixel
            r = (r & 0xFE) | bits[bit_index]
            bit_index += 1
            if bit_index < len(bits):
                g = (g & 0xFE) | bits[bit_index]
                bit_index += 1
            if bit_index < len(bits):
                b = (b & 0xFE) | bits[bit_index]
                bit_index += 1
            encoded_pixels.append((r, g, b))
        else:
            encoded_pixels.append(pixel)
    
    encoded_image = Image.new(image.mode, image.size)
    encoded_image.putdata(encoded_pixels)
    encoded_image.save(output_path)

def decode_image(image_path):
    image = Image.open(image_path)
    image = image.convert('RGB')
    pixels = list(image.getdata())
    
    bits = []
    for pixel in pixels:
        r, g, b = pixel
        bits.append(r & 1)
        bits.append(g & 1)
        bits.append(b & 1)
    
    message = bits_to_text(bits)
    return message.split('\x00')[0]

# Usage example
input_image_path = '/home/ravik/src_git/LP/projects/steganography/image.png'
output_image_path = 'encoded_image.png'
secret_message = 'Hello, Steganography!'

encode_image(input_image_path, secret_message, output_image_path)
decoded_message = decode_image(output_image_path)

print('Decoded message:', decoded_message)
