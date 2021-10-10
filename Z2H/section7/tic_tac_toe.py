from random import random

def greetings():
    print('Hello all. Welcome to tic tac toe by a noob!')

def player_name_entries():
    print('Please enter the player names as requested.')
    p = dict()
    p['p1'] = input('Enter your name Player 1 : ')
    p['p2'] = input('Enter your name Player 2 : ')
    return p

def display_board(board):
    print(f'-------------')
    print(f'| {board[7]} | {board[8]} | {board[9]} |')
    print(f'-------------')
    print(f'| {board[4]} | {board[5]} | {board[6]} |')
    print(f'-------------')
    print(f'| {board[1]} | {board[2]} | {board[3]} |')
    print(f'-------------')



greetings()
players_info = player_name_entries()

players_info['p1']  # now I can call from outside of the function