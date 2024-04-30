# Filter phone number from the give text file.

import re

# regex for phone numbers
phone_pattern = r'\b(?:\d{3}[-.]|\(\d{3}\) )?\d{3}[-.]\d{4}\b'

def findPhoneNumbers(text_file):
    phone_numbers = []
    with open(text_file, 'r') as f:
        file_content = f.read()
        matches = re.findall(phone_pattern, file_content)
        phone_numbers.extend(matches)

    return phone_numbers

def main():
    file_name = '/home/ravik/src_git/LP/ABS/c7/numbers.txt'
    matched_numbers = findPhoneNumbers(file_name)
    print(matched_numbers)

if __name__ == "__main__":
    main()