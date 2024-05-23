import cv2
import numpy as np

def encode_dct(img_path, message, output_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    rows, cols = img.shape
    message += '####'  # Delimiter to mark end of message
    message_index = 0

    # Split image into 8x8 blocks
    for i in range(0, rows, 8):
        for j in range(0, cols, 8):
            if message_index >= len(message):
                break
            block = img[i:i+8, j:j+8]
            dct_block = cv2.dct(np.float32(block))
            char_bin = format(ord(message[message_index]), '08b')

            # Embed message bits into the DCT coefficients
            for k in range(8):
                dct_block[7, k] = int(format(int(dct_block[7, k]), '08b')[:-1] + char_bin[k], 2)
            
            img[i:i+8, j:j+8] = cv2.idct(dct_block)
            message_index += 1

    cv2.imwrite(output_path, img)

# Example usage
encode_dct('input_image.jpg', 'Hello, World!', 'encoded_image.jpg')


def decode_dct(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    rows, cols = img.shape
    message = ''
    char_bin = ''

    # Split image into 8x8 blocks
    for i in range(0, rows, 8):
        for j in range(0, cols, 8):
            if len(message) > 0 and message[-1] == '#':
                break
            block = img[i:i+8, j:j+8]
            dct_block = cv2.dct(np.float32(block))

            # Extract message bits from the DCT coefficients
            for k in range(8):
                char_bin += format(int(dct_block[7, k]), '08b')[-1]
                if len(char_bin) == 8:
                    char = chr(int(char_bin, 2))
                    if char == '#':
                        return message[:-1]
                    message += char
                    char_bin = ''

    return message

# Example usage
decoded_message = decode_dct('encoded_image.jpg')
print('Decoded message:', decoded_message)
