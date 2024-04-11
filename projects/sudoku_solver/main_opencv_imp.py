import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load pre-trained digit recognition model
model = load_model('digit_recognition_model.h5')


def capture_sudoku_from_webcam():
    # Initialize webcam
    cap = cv2.VideoCapture(0)

    # Set dimensions for Sudoku grid (9x9)
    grid_size = (9, 9)

    while True:
        ret, frame = cap.read()

        # Preprocess the frame
        processed_frame = preprocess_frame(frame)

        # Detect Sudoku grid
        sudoku_grid = detect_sudoku_grid(processed_frame)

        if sudoku_grid is not None:
            # Extract digits from Sudoku grid
            digits = extract_digits(sudoku_grid, grid_size)

            # Solve Sudoku puzzle
            solution = solve_sudoku(digits)

            if solution is not None:
                # Overlay solution on original frame
                output_frame = overlay_solution(frame, solution)

                # Display the output frame
                cv2.imshow('Sudoku Solver', output_frame)
            else:
                cv2.putText(frame, "No solution found!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow('Captured Sudoku', frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def preprocess_frame(frame):
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply adaptive thresholding to get binary image
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    return thresh


def detect_sudoku_grid(processed_frame):
    # Find contours in the processed frame
    contours, _ = cv2.findContours(processed_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop over the contours
    for contour in contours:
        # Approximate the contour
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

        # If the contour has four vertices, it might be the Sudoku grid
        if len(approx) == 4:
            return approx

    return None


def extract_digits(sudoku_grid, grid_size, processed_frame=None):
    # Extract the Sudoku grid region
    sudoku_region = cv2.boundingRect(sudoku_grid)
    x, y, w, h = sudoku_region

    # Crop the Sudoku grid region
    cropped_sudoku = processed_frame[y:y + h, x:x + w]

    # Divide the Sudoku grid into cells
    cell_width = w // grid_size[1]
    cell_height = h // grid_size[0]

    digits = []

    # Loop over the rows and columns
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            # Extract cell
            cell = cropped_sudoku[i * cell_height:(i + 1) * cell_height, j * cell_width:(j + 1) * cell_width]

            # Preprocess cell for digit recognition
            digit = preprocess_digit(cell)

            digits.append(digit)

    return digits


def preprocess_digit(digit):
    # Resize the digit to 28x28 (required input size for the model)
    resized_digit = cv2.resize(digit, (28, 28))

    # Convert the digit to grayscale
    gray_digit = cv2.cvtColor(resized_digit, cv2.COLOR_BGR2GRAY)

    # Convert the digit to binary image
    _, binary_digit = cv2.threshold(gray_digit, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Expand dimensions to match the input shape of the model
    preprocessed_digit = np.expand_dims(binary_digit, axis=0)
    preprocessed_digit = np.expand_dims(preprocessed_digit, axis=-1)

    return preprocessed_digit


def solve_sudoku(digits):
    def solve_sudoku_algorithm(grid):
        # Find empty cell
        empty_cell = find_empty_location(grid)

        if not empty_cell:
            # If no empty cell found, puzzle is solved
            return grid

        row, col = empty_cell

        # Try numbers 1 through 9
        for num in range(1, 10):
            if is_valid(grid, num, (row, col)):
                # If the number is valid, try placing it in the cell
                grid[row][col] = num

                # Recursively solve the rest of the puzzle
                if solve_sudoku_algorithm(grid):
                    return grid

                # If the number doesn't lead to a solution, backtrack
                grid[row][col] = 0

        # If no number leads to a solution, backtrack
        return None

    # Flatten digits list into a single array
    flattened_digits = np.array(digits).reshape((81, 28, 28, 1))

    # Predict digits using the model
    predictions = model.predict(flattened_digits)

    # Convert predictions to integers
    predicted_digits = np.argmax(predictions, axis=1)

    # Reshape predicted digits into a 9x9 grid
    grid = predicted_digits.reshape((9, 9))

    # Call the existing Sudoku solving algorithm
    solution = solve_sudoku_algorithm(grid)

    return solution


def find_empty_location(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None


def is_valid(board, num, position):
    # Check row
    for i in range(9):
        if board[position[0]][i] == num and position[1] != i:
            return False

    # Check column
    for i in range(9):
        if board[i][position[1]] == num and position[0] != i:
            return False

    # Check square
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != position:
                return False

    return True


def overlay_solution(frame, solution):
    # Determine cell dimensions
    height, width, _ = frame.shape
    cell_width = width // 9
    cell_height = height // 9

    # Loop through the solution grid
    for i in range(9):
        for j in range(9):
            # Calculate cell coordinates
            x = j * cell_width
            y = i * cell_height

            # Skip if cell is already filled
            if solution[i][j] != 0:
                continue

            # Overlay the solution digit onto the frame
            cv2.putText(frame, str(solution[i][j]), (x + 10, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    return frame


def main():
    print("Would you like to capture Sudoku puzzle from webcam? (Y/N)")
    choice = input().strip().lower()

    if choice == 'y':
        capture_sudoku_from_webcam()
    else:
        print("Please enter the Sudoku puzzle row by row, with empty cells represented by '-'.")
        print("Enter each row without spaces, e.g., '260701680070090190004500......'")
        puzzle = []
        for _ in range(9):
            row = input().strip()
            puzzle.append(row)

        # Convert the puzzle to a 9x9 grid
        grid = []
        for row in puzzle:
            grid_row = []
            for char in row:
                if char == '-':
                    grid_row.append(0)
                else:
                    grid_row.append(int(char))
            grid.append(grid_row)

        # Solve the Sudoku puzzle
        solution = solve_sudoku_algorithm(grid)

        if solution is not None:
            print("Sudoku Puzzle Solved:")
            print_solution(solution)
        else:
            print("No solution found!")

def print_solution(grid):
    for row in grid:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()

