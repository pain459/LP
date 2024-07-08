import tkinter as tk
import random
import numpy as np

# Initialize the game board and add new tiles
def initialize_game():
    board = np.zeros((4, 4), dtype=int)
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = random.choices([2, 4], [0.9, 0.1])[0]

# Move and merge tiles
def move_left(board):
    new_board = np.zeros((4, 4), dtype=int)
    for i in range(4):
        position = 0
        for j in range(4):
            if board[i][j] != 0:
                if new_board[i][position] == 0:
                    new_board[i][position] = board[i][j]
                elif new_board[i][position] == board[i][j]:
                    new_board[i][position] *= 2
                    position += 1
                else:
                    position += 1
                    new_board[i][position] = board[i][j]
    return new_board

def move_right(board):
    return np.fliplr(move_left(np.fliplr(board)))

def move_up(board):
    return np.transpose(move_left(np.transpose(board)))

def move_down(board):
    return np.transpose(move_right(np.transpose(board)))

# Check if the game is over
def is_game_over(board):
    if any(0 in row for row in board):
        return False
    for i in range(4):
        for j in range(4):
            if i > 0 and board[i][j] == board[i-1][j]:
                return False
            if i < 3 and board[i][j] == board[i+1][j]:
                return False
            if j > 0 and board[i][j] == board[i][j-1]:
                return False
            if j < 3 and board[i][j] == board[i][j+1]:
                return False
    return True

# GUI class for the 2048 game
class Game2048:
    def __init__(self, master):
        self.master = master
        self.master.title("2048 Game")
        self.board = initialize_game()
        self.cells = [[None] * 4 for _ in range(4)]
        self.create_grid()
        self.update_grid()
        self.master.bind("<Key>", self.key_pressed)

    def create_grid(self):
        background = tk.Frame(self.master, bg='azure3', bd=3, width=400, height=400)
        background.grid(pady=(100, 0))
        for i in range(4):
            for j in range(4):
                cell = tk.Frame(background, bg='azure4', width=100, height=100)
                cell.grid(row=i, column=j, padx=5, pady=5)
                t = tk.Label(master=cell, text='', bg='azure4', justify=tk.CENTER, font=("arial", 24, "bold"), width=4, height=2)
                t.grid()
                self.cells[i][j] = t

    def update_grid(self):
        for i in range(4):
            for j in range(4):
                value = self.board[i][j]
                if value == 0:
                    self.cells[i][j].configure(text='', bg='azure4')
                else:
                    self.cells[i][j].configure(text=str(value), bg='orange', fg='black')
        self.master.update_idletasks()

    def key_pressed(self, event):
        key = event.keysym
        if key == 'Left':
            self.board = move_left(self.board)
        elif key == 'Right':
            self.board = move_right(self.board)
        elif key == 'Up':
            self.board = move_up(self.board)
        elif key == 'Down':
            self.board = move_down(self.board)
        
        if is_game_over(self.board):
            self.show_game_over()
        else:
            add_new_tile(self.board)
            self.update_grid()

    def show_game_over(self):
        game_over_frame = tk.Frame(self.master, borderwidth=2)
        game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
        tk.Label(game_over_frame, text="Game Over!", fg='red', font=("arial", 24, "bold")).pack()

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = Game2048(root)
    root.mainloop()
