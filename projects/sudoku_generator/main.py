import argparse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from sudoku import Sudoku

def generate_sudoku_puzzle(difficulty=0.9, count=1):
    puzzles = []
    solutions = []
    for _ in range(count):
        puzzle = Sudoku(3).difficulty(difficulty)  # Create a Sudoku puzzle with specified difficulty
        solution = puzzle.solve()  # Solve the puzzle to get its solution
        puzzles.append(puzzle.board)
        solutions.append(solution.board)
    return puzzles, solutions

def draw_grid(canvas, text_list, title):
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

    # Add title
    style = getSampleStyleSheet()['Title']
    style.fontSize = 20
    title_width = canvas.stringWidth(title, style.fontName, style.fontSize)
    x = (width - title_width) / 2
    y = height - 50
    canvas.setFont(style.fontName, style.fontSize)
    canvas.drawString(x, y, title)

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

def main():
    parser = argparse.ArgumentParser(description='Generate Sudoku PDF')
    parser.add_argument('-d', '--difficulty', type=float, default=0.9, help='Difficulty level of the Sudoku puzzle (default: 0.9)')
    parser.add_argument('-c', '--count', type=int, default=1, help='Number of Sudoku puzzles to generate (default: 1)')
    parser.add_argument('-f', '--filename', type=str, default='sudoku.pdf', help='Name of the output PDF file (default: sudoku.pdf)')
    args = parser.parse_args()

    # Create a PDF
    c = canvas.Canvas(args.filename, pagesize=letter)
    puzzle_count = args.count
    puzzles, solutions = generate_sudoku_puzzle(args.difficulty, puzzle_count)

    # Draw puzzles
    page_num = 1
    for i in range(0, puzzle_count, 4):
        puzzles_to_draw = puzzles[i:i+4]
        c.setLineWidth(1)
        for j, puzzle in enumerate(puzzles_to_draw):
            draw_grid(c, puzzle, f"Sudoku Puzzle {page_num}")
            if j < len(puzzles_to_draw) - 1:
                c.showPage()
                page_num += 1

    # Draw solutions
    c.showPage()
    for i, solution in enumerate(solutions):
        draw_grid(c, solution, f"Sudoku Solution {i+1}")
        if i < len(solutions) - 1:
            c.showPage()

    # Save the PDF
    c.save()

if __name__ == "__main__":
    main()
