from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.core.window import Window
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

class Game2048(App):
    def build(self):
        self.board = initialize_game()
        self.layout = GridLayout(cols=4)
        self.labels = [[Label(text=str(self.board[i][j]), font_size='20sp') for j in range(4)] for i in range(4)]
        for i in range(4):
            for j in range(4):
                self.layout.add_widget(self.labels[i][j])

        # Add developer info button
        self.dev_info_button = Button(text="About", size_hint=(1, 0.1))
        self.dev_info_button.bind(on_press=self.show_developer_info)
        self.layout.add_widget(self.dev_info_button, index=0)

        self.update_grid()
        Window.bind(on_key_down=self.on_key_down)
        return self.layout

    def update_grid(self):
        for i in range(4):
            for j in range(4):
                value = self.board[i][j]
                if value == 0:
                    self.labels[i][j].text = ''
                else:
                    self.labels[i][j].text = str(value)

    def on_key_down(self, window, key, scancode, codepoint, modifier):
        if key == 273:  # Up arrow key
            self.board = move_up(self.board)
        elif key == 274:  # Down arrow key
            self.board = move_down(self.board)
        elif key == 276:  # Left arrow key
            self.board = move_left(self.board)
        elif key == 275:  # Right arrow key
            self.board = move_right(self.board)

        if is_game_over(self.board):
            self.show_game_over()
        else:
            add_new_tile(self.board)
            self.update_grid()

    def show_developer_info(self, instance):
        content = Button(text='This 2048 game is developed by Pain.')
        popup = Popup(title='PAIN',
                      content=content,
                      size_hint=(0.6, 0.6))
        content.bind(on_press=popup.dismiss)
        popup.open()

    def show_game_over(self):
        self.layout.clear_widgets()
        self.layout.add_widget(Label(text="Game Over!", font_size='40sp'))

if __name__ == "__main__":
    Game2048().run()
