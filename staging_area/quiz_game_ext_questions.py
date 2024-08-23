import json
import random

# Open JSON file
with open('DB.json', 'r') as file:
    data = json.load(file)

# # Access data
# print(data[1])
# # Access question
# print(data[1]["question"])
# print(data[1]["answers"])
# print(data[1]["answers"][0:3])
# print(len(data))  # Give number of questions

total_questions = len(data)
score = 0
questions_per_game = 1
selected_question = []

def choose_random_question():
    return random.randint(0, total_questions)

for i in range(questions_per_game):
    extract_question = choose_random_question()
    selected_question.append(extract_question)
    print(data[extract_question])
    print(f'Your question is {extract_question}')
    print(f'{data[extract_question]["question"]}')
    print("Your options: \n")
    for options in data[extract_question]["answers"]:
        print(f"{options['choice']}: {options['text']}")
    answer = input("Your answer? ").strip().upper()
    print(data[extract_question]["question"]["answers"][0]['correct'])

print(selected_question)