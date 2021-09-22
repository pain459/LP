# Creating an modifying PDF files
# File at C:\local
# File name Installing_and_Upgrading_Geneva.pdf

import PyPDF2
import os

file_path = r"C:\local\Installing_and_Upgrading_Geneva.pdf"
input_pdf = PyPDF2.PdfFileReader(file_path)

print(input_pdf.getNumPages())

document_info = input_pdf.getDocumentInfo()
print(document_info)

print(type(document_info))

print(document_info.title)
print(document_info.author)

page19 = input_pdf.getPage(19)
# print(type(page0))
print(page19.extractText())

# Creating pdf files using reportlab.

from reportlab.pdfgen import canvas

c = canvas.Canvas("hello.pdf")
c.drawString(100, 100, "Hello World")
c.save()

# changing the default page size from A4 to letter and print the same.

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

c = canvas.Canvas("hello2.pdf", pagesize=letter)
c.drawString(100, 100, "Hello World!")
c.save()

# using the inches to place the text on the letter.

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

xmargin = 3.2 * inch
ymargin = 6 * inch

c = canvas.Canvas("hello2.pdf", pagesize=letter)
c.drawString(xmargin, ymargin, "Hello World!")
c.save()

# Drawing a table

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import Table

xmargin = 3.2 * inch
ymargin = 6 * inch

c = canvas.Canvas("report1.pdf", pagesize=letter)
# copying data.
# 1
data = [['#1', '#2', '#3', '#4', '#5'],
        ['10', '11', '12', '13', '14'],
        ['20', '21', '22', '23', '24'],
        ['30', '31', '32', '33', '34'],
        ['20', '21', '22', '23', '24'],
        ['20', '21', '22', '23', '24'],
        ['20', '21', '22', '23', '24'],
        ['20', '21', '22', '23', '24']]
# 2
t = Table(data)

# 3
t.setStyle([('TEXTCOLOR', (0,0), (4,0), colors.red)])

# 4
t.wrapOn(c, xmargin, ymargin)
t.drawOn(c, xmargin, ymargin)

c.save()