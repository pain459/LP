def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty_location(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return row, col
    return None


def is_valid(board, num, position):
    # Check row
    for i in range(len(board[0])):
        if board[position[0]][i] == num and position[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][position[1]] == num and position[0] != i:
            return False

    # Check square
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != position:
                return False

    return True


def solve_sudoku(board):
    find = find_empty_location(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False


def main():
    print("Please enter the Sudoku puzzle row-wise, using 0 for empty cells.")
    print("Separate numbers by spaces. Press Enter after each row.")

    board = []
    for _ in range(9):
        row = list(map(int, input().split()))
        board.append(row)

    print("\nSudoku Puzzle:")
    print_board(board)

    if solve_sudoku(board):
        print("\nSudoku Puzzle Solved:")
        print_board(board)
    else:
        print("\nNo solution exists for the given Sudoku puzzle.")




if __name__ == "__main__":
    main()
