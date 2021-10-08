# We will write a program to guess the ball postition here.

from random import shuffle

def shuffle_balls(x_balls):
	shuffle(x_balls)
	return x_balls

def user_input():
	x = ''
	# As the user to input the number 0, 1, or 2 to determine the guess
	while x not in ['0', '1', '2']:
		x = input("Enter the number 0, 1, or 2:")

	return int(x)

def check_guess(x_balls, x):
	if x_balls[x] == 'O':
		print("Correct")
		print(x_balls)
	else:
		print('Wrong guess')
		print(x_balls)

# initial list
balls_list = [' ', 'O', ' ']
# shuffle list
mixedup_list = shuffle_balls(balls_list)
# user guess
x = user_input()
# check guess
check_guess(mixedup_list, x)