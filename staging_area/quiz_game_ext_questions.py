import json
import random

# Open JSON file
with open('DB.json', 'r') as file:
    data = json.load(file)

total_questions = len(data)

def choose_random_question():
    return random.randint(0, total_questions)

def main():
    score = 0
    questions_per_game = 3
    selected_question = []
    for i in range(questions_per_game):
        extract_question = choose_random_question()
        selected_question.append(extract_question)
        print(f'Your question is {extract_question}')
        print(f'{data[extract_question]["question"]}')
        print("Your options: \n")
        for options in data[extract_question]["answers"]:
            print(f"{options['choice']}: {options['text']}")
        answer = input("Your answer? ").strip().upper()
        for i in data[extract_question]["answers"]:
            if (i['choice'] == answer) & (i['correct']):
                print('Correct!')
                score += 1
            else:
                pass

    print(f"You scored {score} out of {questions_per_game}")

if __name__ == "__main__":
    main()