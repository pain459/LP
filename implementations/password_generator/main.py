# Script to generate passwords of required lengths.

import random
import string
import argparse


# function to generate 3 random characters from upper case, special symbol and number
def generate_special_chars():
    special_characters = string.punctuation
    numbers = string.digits
    upper_case_letters = string.ascii_uppercase
    spl_sequence = [random.choice(special_characters), random.choice(numbers), random.choice(upper_case_letters)]
    return spl_sequence


# generate a password with length -3 .
def generate_password_of_length(password_length):
    remaining_length = password_length - 3
    primary_sequence = []
    for _ in range(remaining_length):
        primary_sequence.append(random.choice(string.ascii_letters + string.digits + string.ascii_letters))
    return primary_sequence


# combine the password with random letters from func1 and shuffle
def generate_final_password(p_s, s_s):
    random.shuffle(p_s)
    random.shuffle(s_s)
    final = p_s + s_s
    final_password = ""
    final_password = final_password.join(final)
    return final_password



def main():
    # argpass for length input
    parser = argparse.ArgumentParser(description="Generate a password with specific length and complexity")
    parser.add_argument("--length", dest="length", type=int, help="Length of the password")
    args = parser.parse_args()

    password_length = args.length
    s1 = generate_special_chars()
    s2 = generate_password_of_length(password_length=password_length)
    s3 = generate_final_password(p_s=s1, s_s=s2)
    print(f'Generated password is {s3}')


if __name__ == "__main__":
    main()