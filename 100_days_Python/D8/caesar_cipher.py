from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher(direction, text, shift):
    final_text = ""
    if direction == 'encode':
        for letter in text:
            position = alphabet.index(letter)
            new_position = (position + shift) % 26
            new_letter = alphabet[new_position]
            final_text += new_letter
        print(f"The encoded text is {final_text}")
    elif direction == 'decode':
        for letter in text:
            position = alphabet.index(letter)
            new_position = (position - shift) % 26
            new_letter = alphabet[new_position]
            final_text += new_letter
        print(f"The decoded text is {final_text}")

        
should_end = False
while not should_end:   
    print('Welcome to Caeser Cipher!')
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: (Type 'stop to exit code.')\n").lower()
    if direction in ['encode', 'decode']:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        cipher(direction, text, shift)
        userChoice = input('Do you want to try again? (yes/no): ').lower()
        if userChoice == 'no':
            should_end = True
            print('Bye!')
    elif direction == 'stop':
        should_end = True
        print('Program terminated on user request!')
    else:
        print('Invalid entry!')
        restart = input("Do you want to try again? yes/no ")
        if restart == 'no':
            should_end = True
            print('Bye!')