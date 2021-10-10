def player_name_entries():
    print('Please enter the player names as requested.')
    p = dict()
    p['p1'] = input('Enter your name Player 1 : ')
    p['p2'] = input('Enter your name Player 2 : ')
    return p

#player_name_entries()
players_info = player_name_entries()

print(players_info)
#print(players)
def symbol_selection():
    for i in players_info.values():
        print(i)


symbol_selection()



t = ('a', 'b')
for i in t:
    choice = 'Wrong'
    while choice not in ['X', 'O']:
        choice = input(f'{i} enter your preferred symbol (X or O): ')

        if choice not in ['X', 'O']:
            print('Invalid entry')
        else:
            pass
    print(choice)



sample_dict = {'p1': 'RRR', 'p2': 'SSS'}
sample_dict['p1'].append('X')
print(sample_dict)
