from game_data import data
from art import logo, vs
import random

x = random.choice(data)
y = random.choice(data)


def generate_unique_questions(x, y):
    unique_questions_generated = False
    while not unique_questions_generated:
        if x == y:
            y = random.choice(data)
        elif x != y:
            unique_questions_generated = True
            return x, y
        else:
            unique_questions_generated = False


def give_correct_answer(a, b):
    if a['follower_count'] > b['follower_count']:
        return 'A'
    else:
        return 'B'


def game_template(logo, vs, q1, q2):
    print(logo)
    print(
        f"Compare A: {q1['name']}, a {q1['description']}, from {q1['country']}.")
    print(vs)
    print(
        f"Compare A: {q2['name']}, a {q2['description']}, from {q2['country']}.")
    user_input = str(input("Who has more followers? Type 'A' or 'B': "))
    return user_input


def compare_user_answer(correct_answer, user_answer):
    if correct_answer == user_answer:
        return 0
    else:
        return 1


game_over = False
score = 0
while not game_over:
    question1, question2 = generate_unique_questions(x=x, y=y)
    user_answer = game_template(logo=logo, vs=vs, q1=question1, q2=question2)
    answer = give_correct_answer(a=question1, b=question2)
    result = compare_user_answer(
        correct_answer=answer, user_answer=user_answer)
    if result == 0:
        score += 1
        print('Next question!')
        game_over = False
    else:
        print('Game Over!')
        print(f"Total score is {score}")
        game_over = True
