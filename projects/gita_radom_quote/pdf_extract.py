import PyPDF2

def extract_text_pypdf2(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = []
        for page_num in range(4, len(reader.pages)):  # Start from page 5 using updated API
            page = reader.pages[page_num]
            text.append(page.extract_text())
    return '\n'.join(text)

def write_text_to_file(text, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)


# Usage example
pdf_path = '/home/ravik/src_git/LP/projects/gita_radom_quote/gita_quotes_filtered.pdf'
extracted_text = extract_text_pypdf2(pdf_path)
print(extracted_text[:2000])  # Print the first 2000 characters to check

# Usage example
extracted_text_path = 'extracted_text.txt'
write_text_to_file(extracted_text, extracted_text_path)
