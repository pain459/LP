from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.platypus import Table, TableStyle

def draw_grid(canvas, text_list):
    width, height = letter
    cell_width = (width - 100) / 9
    cell_height = (height - 100) / 9

    # Draw grid lines
    for i in range(10):
        line_width = 1 if i % 3 != 0 else 2  # thicker lines for subgrids
        canvas.setLineWidth(line_width)
        canvas.line(50, height - 50 - i * cell_height, width - 50, height - 50 - i * cell_height)
        canvas.line(50 + i * cell_width, height - 50, 50 + i * cell_width, 50)
        if i % 3 == 0 and i != 0:
            canvas.setLineWidth(2)
            canvas.line(50, height - 50 - i * cell_height + 1, width - 50, height - 50 - i * cell_height + 1)
            canvas.line(50 + i * cell_width + 1, height - 50, 50 + i * cell_width + 1, 50)

    # Add text to cells
    style = getSampleStyleSheet()['BodyText']
    style.fontSize = 18
    style.fontName = 'Helvetica-Bold'
    for i in range(9):
        for j in range(9):
            num = text_list[i][j]
            if num is not None:
                text = str(num)
                text_width = canvas.stringWidth(text, style.fontName, style.fontSize)
                text_height = style.fontSize
                x = 50 + j * cell_width + (cell_width - text_width) / 2
                y = height - 50 - i * cell_height - (cell_height - text_height) / 2
                canvas.setFont(style.fontName, style.fontSize)
                canvas.drawString(x, y, text)

# Create a PDF
c = canvas.Canvas("sudoku.pdf", pagesize=letter)
text_list = [
    [8, None, None, None, None, None, None, 6, None],
    [None, None, None, None, None, None, 9, None, None],
    [None, None, None, None, None, 8, None, None, None],
    [None, None, None, 9, None, None, None, 7, None],
    [None, None, None, 7, None, None, None, 9, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, 6, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None]
]
draw_grid(c, text_list)
c.save()
