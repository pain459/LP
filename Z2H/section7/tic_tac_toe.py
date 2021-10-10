def display_board(board):
    print(f'-------------')
    print(f'| {board[7]} | {board[8]} | {board[9]} |')
    print(f'-------------')
    print(f'| {board[4]} | {board[5]} | {board[6]} |')
    print(f'-------------')
    print(f'| {board[1]} | {board[2]} | {board[3]} |')
    print(f'-------------')


test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)

def player_input():
    
    choice = 'wrong'
    while choice not in ['X', 'O']:
        choice = input('Pick your marker for the game (X, O):')
        
        if choice not in ['X', 'O']:
            print('Sorry, invalid choice')
            
    return choice

player_input()

def place_marker(board, marker, position):
    pass