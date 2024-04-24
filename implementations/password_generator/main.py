import random
import string
import argparse


def generate_special_chars():
    special_characters = string.punctuation
    numbers = string.digits
    upper_case_letters = string.ascii_uppercase
    return [
        random.choice(special_characters),
        random.choice(numbers),
        random.choice(upper_case_letters)
    ]


def generate_password_of_length(password_length):
    return [
        random.choice(string.ascii_letters + string.digits + string.ascii_letters)
        for _ in range(password_length - 3)
    ]


def generate_final_password(p_s, s_s):
    password = p_s + s_s
    random.shuffle(password)
    return ''.join(password)


def main():
    parser = argparse.ArgumentParser(description="Generate a password with specific length and complexity")
    parser.add_argument("--length", dest="length", type=int, help="Length of the password")
    args = parser.parse_args()

    password_length = args.length
    if password_length < 4:
        print("Password length should be at least 4 characters.")
        return

    special_chars = generate_special_chars()
    password_chars = generate_password_of_length(password_length)
    final_password = generate_final_password(special_chars, password_chars)

    print(f"Generated password is '{final_password}'")


if __name__ == "__main__":
    main()
