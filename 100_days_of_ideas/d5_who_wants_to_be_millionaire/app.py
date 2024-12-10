import sqlite3
import csv
import datetime
import secrets

# ------------------------------------------------------------
# Database Setup
# ------------------------------------------------------------
def setup_database(db_name="millionaire_game.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    # Create a table for user sessions if not exists
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


def insert_user(db_name, user_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Generate a unique ID
    # Format: <date+name+random_6_digit_hex>
    date_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    random_hex = secrets.token_hex(3)  # 6 hex digits
    unique_id = f"{date_str}_{user_name}_{random_hex}"

    start_time = datetime.datetime.now().isoformat()
    cursor.execute("INSERT INTO user_game (unique_id, user_name, start_time, final_prize) VALUES (?, ?, ?, ?)",
                   (unique_id, user_name, start_time, 0))
    conn.commit()
    conn.close()
    return unique_id


def update_final_prize(db_name, unique_id, prize):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    end_time = datetime.datetime.now().isoformat()
    cursor.execute("UPDATE user_game SET final_prize = ?, end_time = ? WHERE unique_id = ?",
                   (prize, end_time, unique_id))
    conn.commit()
    conn.close()


# ------------------------------------------------------------
# Questions Handling
# ------------------------------------------------------------
def load_questions(csv_file):
    """Load questions from CSV into a dictionary keyed by difficulty."""
    questions_by_difficulty = {}
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            difficulty = int(row['difficulty'])
            if difficulty not in questions_by_difficulty:
                questions_by_difficulty[difficulty] = []
            questions_by_difficulty[difficulty].append({
                'question': row['question'],
                'options': {
                    'A': row['optionA'],
                    'B': row['optionB'],
                    'C': row['optionC'],
                    'D': row['optionD']
                },
                'correct': row['correct_answer'].strip().upper(),
                'prize': int(row['prize'])
            })
    return questions_by_difficulty


def get_question(questions_by_difficulty, difficulty):
    """Get the next question for a given difficulty. 
    If no question of that difficulty is left, return None."""
    if difficulty not in questions_by_difficulty or not questions_by_difficulty[difficulty]:
        return None
    return questions_by_difficulty[difficulty].pop(0)


# ------------------------------------------------------------
# Game Logic
# ------------------------------------------------------------
def fifty_fifty_lifeline(question_data):
    """Apply 50:50 lifeline to remove two incorrect options."""
    correct = question_data['correct']
    all_options = ['A', 'B', 'C', 'D']
    all_options.remove(correct)  # remove correct answer from the pool
    # randomly pick two incorrect to remove
    to_remove = all_options[:2]  # simplified: just pick the first two incorrect
    # Actually remove them from the question data's options
    for opt in to_remove:
        question_data['options'][opt] = None
    return question_data


def play_game(db_name, csv_file):
    # Setup DB and load questions
    setup_database(db_name)
    questions_by_difficulty = load_questions(csv_file)

    # Get user name
    user_name = input("Enter your name: ")
    unique_id = insert_user(db_name, user_name)
    print(f"Welcome, {user_name}! Your game ID is {unique_id}.")

    # Initialize game state
    current_difficulty = 1
    total_prize = 0
    fifty_fifty_available = True

    print("Game Started! Let's play 'Who Wants to be a Millionaire?'")
    print("You have one 50:50 lifeline available to remove two incorrect options.\n")

    while True:
        question_data = get_question(questions_by_difficulty, current_difficulty)
        if not question_data:
            # No more questions at this difficulty, increase difficulty
            # If still no questions, end the game.
            current_difficulty += 1
            question_data = get_question(questions_by_difficulty, current_difficulty)
            if not question_data:
                # We ran out of questions entirely
                print("Congratulations! You've answered all available questions.")
                print(f"You leave with a total prize of {total_prize}.")
                update_final_prize(db_name, unique_id, total_prize)
                break

        # Display the question
        print(f"Difficulty {current_difficulty} Question:")
        print(question_data['question'])

        # Display options
        for opt, val in question_data['options'].items():
            if val is not None:
                print(f"  {opt}: {val}")

        # Ask if the user wants to use 50:50 if available
        if fifty_fifty_available:
            use_ff = input("Do you want to use 50:50 lifeline? (y/n): ").strip().lower()
            if use_ff == 'y':
                question_data = fifty_fifty_lifeline(question_data)
                fifty_fifty_available = False
                # Display options again after 50:50
                print("\nAfter using 50:50, remaining options:")
                for opt, val in question_data['options'].items():
                    if val is not None:
                        print(f"  {opt}: {val}")

        # Get user answer
        user_answer = input("Your answer (A/B/C/D) or type Q to quit: ").strip().upper()

        if user_answer == 'Q':
            print(f"You chose to quit. You leave with a total prize of {total_prize}.")
            update_final_prize(db_name, unique_id, total_prize)
            break

        # Validate input
        if user_answer not in ['A', 'B', 'C', 'D']:
            print("Invalid choice. Game ends.")
            print(f"You leave with a total prize of {total_prize}.")
            update_final_prize(db_name, unique_id, total_prize)
            break

        # Check answer
        if user_answer == question_data['correct']:
            # Correct answer
            total_prize = question_data['prize']
            print("Correct Answer!")
            print(f"You have won {total_prize} so far.\n")
            # Increase difficulty after a correct answer
            current_difficulty += 1
        else:
            # Wrong answer
            print("Wrong Answer!")
            print(f"Game Over. You leave with {total_prize}.")
            update_final_prize(db_name, unique_id, total_prize)
            break


if __name__ == "__main__":
    # Example usage
    db_name = "millionaire_game.db"
    csv_file = "questions.csv"
    play_game(db_name, csv_file)
