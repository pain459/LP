import PyPDF2 as pdf_reader

pdf = open("chillu.pdf", "rb")
reader = pdf_reader.PdfReader(pdf)

page = reader.pages[0]

print(page.extract_text())

