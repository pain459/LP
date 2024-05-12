import sys
from fpdf import FPDF
from ebooklib import epub
from bs4 import BeautifulSoup

class PDF(FPDF):
    def add_title(self, title):
        self.add_page()
        self.set_font("Arial", size=12)
        self.cell(200, 10, txt=title, ln=True, align='C')

def epub_to_pdf(epub_file, pdf_file):
    try:
        book = epub.read_epub(epub_file)
        pdf = PDF()
        for item in book.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                soup = BeautifulSoup(item.content, 'html.parser')
                for p in soup.find_all('p'):
                    style = p.attrs.get('style', '')
                    font_name, font_size = parse_style(style)
                    pdf.set_font(font_name, size=font_size)
                    pdf.add_page()
                    pdf.multi_cell(0, 10, p.get_text())
        pdf.output(pdf_file)
        print(f"PDF created successfully from {epub_file} at {pdf_file}")
    except Exception as e:
        print(f"Failed to convert EPUB to PDF: {e}")

def parse_style(style):
    styles = dict(item.split(":") for item in style.split(";") if item)
    font_name = 'Arial'  # Default
    font_size = 12  # Default size
    if 'font-family' in styles:
        font_name = styles['font-family']
    if 'font-size' in styles:
        size = styles['font-size'].replace('px', '')
        font_size = int(size)
    return font_name, font_size

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py input_file output_file.pdf")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        epub_to_pdf(input_file, output_file)
