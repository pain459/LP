from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import datetime
import secrets
import csv
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key

DB_NAME = 'millionaire_game.db'
CSV_FILE = 'questions.csv'

# Global variable to store questions (not in session)
QUESTIONS = []

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

def load_questions(csv_file):
    questions = []
    if not os.path.exists(csv_file):
        print(f"CSV file {csv_file} not found.")
        return questions

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Ensure prize and difficulty are integers
            try:
                difficulty = int(row['difficulty'])
                prize = int(row['prize'])
            except ValueError:
                # Skip rows that have invalid integer fields
                continue

            question = {
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
            questions.append(question)

    print("Total questions loaded:", len(questions))
    return questions

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_name = request.form.get('username')
        if user_name:
            unique_id = insert_user(user_name)
            session['user_name'] = user_name
            session['unique_id'] = unique_id
            session['current_question_index'] = 0
            session['fifty_fifty_used'] = False
            return redirect(url_for('game'))
    return render_template('index.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    if 'user_name' not in session:
        return redirect(url_for('index'))

    current_index = session.get('current_question_index', 0)
    fifty_fifty_used = session.get('fifty_fifty_used', False)
    unique_id = session.get('unique_id', None)

    # If no questions loaded or no more questions
    if current_index >= len(QUESTIONS) or len(QUESTIONS) == 0:
        # No more questions or empty CSV
        total_prize = QUESTIONS[-1]['prize'] if QUESTIONS else 0
        if unique_id:
            update_final_prize(unique_id, total_prize)
        return render_template('game.html', done=True, total_prize=total_prize, game_over=False)

    question = QUESTIONS[current_index]

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
        else:
            # User selected an answer
            chosen = request.form.get('answer')
            if chosen == question['correct']:
                # Correct answer
                session['current_question_index'] = current_index + 1
                # If this was the last question, game ends
                if session['current_question_index'] >= len(QUESTIONS):
                    # All questions answered
                    total_prize = question['prize']
                    if unique_id:
                        update_final_prize(unique_id, total_prize)
                    return render_template('game.html', done=True, total_prize=total_prize, game_over=False)
                return redirect(url_for('game'))
            else:
                # Wrong answer
                last_prize = 0
                if current_index > 0:
                    last_prize = QUESTIONS[current_index - 1]['prize']
                if unique_id:
                    update_final_prize(unique_id, last_prize)
                return render_template('game.html', game_over=True, total_prize=last_prize, done=False)

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
    QUESTIONS = load_questions(CSV_FILE)  # Load questions once globally
    app.run(debug=True)
