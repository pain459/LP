from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.platypus import Table, TableStyle
from sudoku import Sudoku

def generate_sudoku_puzzle():
    puzzle = Sudoku(3).difficulty(0.9)  # Create a Sudoku puzzle with 90% cells empty
    puzzle.solve()  # Solve the puzzle to ensure it's valid
    return puzzle.board

def draw_grid(canvas, text_list):
    width, height = letter
    cell_size = min((width - 100) / 9, (height - 100) / 9)

    # Draw grid lines
    for i in range(10):
        line_width = 1 if i % 3 != 0 else 2  # thicker lines for subgrids
        canvas.setLineWidth(line_width)
        canvas.line(50, height - 50 - i * cell_size, width - 50, height - 50 - i * cell_size)
        if i < 9:  # Corrected loop range
            canvas.line(50 + i * cell_size, height - 50, 50 + i * cell_size, height - 50 - 9 * cell_size)  # Adjusted end point
        if i % 3 == 0 and i != 0:
            canvas.setLineWidth(2)
            canvas.line(50, height - 50 - i * cell_size + 1, width - 50, height - 50 - i * cell_size + 1)
            canvas.line(50 + i * cell_size + 1, height - 50, 50 + i * cell_size + 1, height - 50 - 9 * cell_size + 1)  # Adjusted end point

    # Add text to cells
    style = getSampleStyleSheet()['BodyText']
    style.fontSize = 0.6 * cell_size
    style.fontName = 'Helvetica-Bold'
    for i in range(9):
        for j in range(9):
            num = text_list[i][j]
            if num is not None:
                text = str(num)
                text_width = canvas.stringWidth(text, style.fontName, style.fontSize)
                text_height = style.fontSize
                x = 50 + j * cell_size + (cell_size - text_width) / 2
                y = height - 50 - (i + 1) * cell_size + (cell_size - text_height) / 2
                canvas.setFont(style.fontName, style.fontSize)
                canvas.drawString(x, y, text)

# Create a PDF
c = canvas.Canvas("sudoku.pdf", pagesize=letter)
text_list = generate_sudoku_puzzle()
draw_grid(c, text_list)
c.save()
