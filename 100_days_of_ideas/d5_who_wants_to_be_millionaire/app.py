from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import datetime
import secrets
import csv
import os
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key

DB_NAME = 'millionaire_game.db'
CSV_FILE = 'questions.csv'

# We will have 15 questions in the game (1 per difficulty level from 1 to 15)
TOTAL_QUESTIONS = 15

# Global dictionary to store questions by difficulty
# Format: {difficulty_number: [ {question_data}, ... ] }
QUESTIONS_BY_DIFF = {}

def setup_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_game (
            unique_id TEXT PRIMARY KEY,
            user_name TEXT,
            start_time TEXT,
            end_time TEXT,
            final_prize INTEGER
        )
    """)
    conn.commit()
    conn.close()

def insert_user(user_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    date_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    random_hex = secrets.token_hex(3)  # 6 hex digits
    unique_id = f"{date_str}_{user_name}_{random_hex}"

    start_time = datetime.datetime.now().isoformat()
    cursor.execute("INSERT INTO user_game (unique_id, user_name, start_time, final_prize) VALUES (?, ?, ?, ?)",
                   (unique_id, user_name, start_time, 0))
    conn.commit()
    conn.close()
    return unique_id

def update_final_prize(unique_id, prize):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    end_time = datetime.datetime.now().isoformat()
    cursor.execute("UPDATE user_game SET final_prize = ?, end_time = ? WHERE unique_id = ?",
                   (prize, end_time, unique_id))
    conn.commit()
    conn.close()

def load_questions_by_difficulty(csv_file):
    questions_by_diff = {}
    if not os.path.exists(csv_file):
        print(f"CSV file {csv_file} not found.")
        return questions_by_diff

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                difficulty = int(row['difficulty'])
                prize = int(row['prize'])
            except ValueError:
                # skip malformed rows
                continue

            q_data = {
                'difficulty': difficulty,
                'question': row['question'],
                'options': {
                    'A': row['optionA'],
                    'B': row['optionB'],
                    'C': row['optionC'],
                    'D': row['optionD']
                },
                'correct': row['correct_answer'].strip().upper(),
                'prize': prize
            }

            if difficulty not in questions_by_diff:
                questions_by_diff[difficulty] = []
            questions_by_diff[difficulty].append(q_data)

    # Print number of questions per difficulty for debugging
    for d, q_list in questions_by_diff.items():
        print(f"Difficulty {d}: {len(q_list)} questions loaded.")

    return questions_by_diff

def get_current_difficulty():
    # difficulty = current_question_index + 1
    current_question_index = session.get('current_question_index', 0)
    return current_question_index + 1

def pick_question_for_current_difficulty():
    difficulty = get_current_difficulty()
    # Ensure we have questions for this difficulty
    if difficulty not in QUESTIONS_BY_DIFF or not QUESTIONS_BY_DIFF[difficulty]:
        return None
    # Randomly choose one question from this difficulty
    question = random.choice(QUESTIONS_BY_DIFF[difficulty])
    # Remove it from the pool so it's not repeated
    QUESTIONS_BY_DIFF[difficulty].remove(question)
    return question

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_name = request.form.get('username')
        if user_name:
            unique_id = insert_user(user_name)
            session.clear()
            session['user_name'] = user_name
            session['unique_id'] = unique_id
            session['current_question_index'] = 0
            session['fifty_fifty_used'] = False
            session['milestone_prize'] = 0
            # Pick the first question now
            question = pick_question_for_current_difficulty()
            if question is None:
                # No questions available for difficulty 1 - end game immediately
                return render_template('game.html', game_over=True, total_prize=0, done=False)
            session['current_question'] = question
            return redirect(url_for('game'))
    return render_template('index.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    if 'user_name' not in session:
        return redirect(url_for('index'))

    current_index = session.get('current_question_index', 0)
    fifty_fifty_used = session.get('fifty_fifty_used', False)
    unique_id = session.get('unique_id', None)
    milestone_prize = session.get('milestone_prize', 0)
    question = session.get('current_question', None)

    # Check if we reached end of game (answered all 15 questions)
    if current_index >= TOTAL_QUESTIONS:
        # All questions answered correctly
        # The last milestone (Q15) prize is guaranteed.
        # Q15 = index 14
        final_prize = session['milestone_prize']
        if unique_id:
            update_final_prize(unique_id, final_prize)
        return render_template('game.html', done=True, total_prize=final_prize, game_over=False)

    # If we have no question loaded in session, try to pick one
    if question is None:
        # Pick a question for current difficulty
        question = pick_question_for_current_difficulty()
        if question is None:
            # No questions available - end game (though this shouldn't happen if CSV is large enough)
            final_prize = milestone_prize
            if unique_id:
                update_final_prize(unique_id, final_prize)
            return render_template('game.html', game_over=True, total_prize=final_prize, done=False)
        session['current_question'] = question

    if request.method == 'POST':
        if 'fifty_fifty' in request.form and not fifty_fifty_used:
            # Use 50:50 lifeline
            correct = question['correct']
            all_opts = ['A','B','C','D']
            all_opts.remove(correct)
            to_remove = all_opts[:2]
            for opt in to_remove:
                question['options'][opt] = None
            session['fifty_fifty_used'] = True
            session['current_question'] = question
        else:
            # User selected an answer
            chosen = request.form.get('answer')
            if chosen == question['correct']:
                # Correct answer
                # Check if we hit a milestone: Q5, Q10, Q15
                # Q5 = index 4, Q10 = index 9, Q15 = index 14
                if current_index == 4:   # just answered Q5
                    milestone_prize = question['prize']
                elif current_index == 9: # just answered Q10
                    milestone_prize = question['prize']
                elif current_index == 14: # just answered Q15
                    milestone_prize = question['prize']

                session['milestone_prize'] = milestone_prize

                session['current_question_index'] = current_index + 1
                session['fifty_fifty_used'] = False
                session.pop('current_question', None)  # Clear current question to pick next one

                # If all questions answered:
                if session['current_question_index'] >= TOTAL_QUESTIONS:
                    # Completed all 15 questions correctly
                    final_prize = milestone_prize  # Q15 prize
                    if unique_id:
                        update_final_prize(unique_id, final_prize)
                    return render_template('game.html', done=True, total_prize=final_prize, game_over=False)

                # Pick next question
                next_question = pick_question_for_current_difficulty()
                if next_question is None:
                    # No questions available for next difficulty - end game but award milestone
                    if unique_id:
                        update_final_prize(unique_id, milestone_prize)
                    return render_template('game.html', done=True, total_prize=milestone_prize, game_over=False)
                session['current_question'] = next_question
                return redirect(url_for('game'))
            else:
                # Wrong answer
                # User gets the last milestone_prize
                if unique_id:
                    update_final_prize(unique_id, milestone_prize)
                return render_template('game.html', game_over=True, total_prize=milestone_prize, done=False)

    # Filter out None options if 50:50 used
    filtered_options = {k: v for k,v in question['options'].items() if v is not None}

    return render_template('game.html',
                           question=question,
                           options=filtered_options,
                           fifty_fifty_used=fifty_fifty_used,
                           done=False,
                           game_over=False)

if __name__ == '__main__':
    setup_database()
    QUESTIONS_BY_DIFF = load_questions_by_difficulty(CSV_FILE)
    app.run(debug=True)
