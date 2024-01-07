from spellchecker import SpellChecker


corrector = SpellChecker()

user_word = input("Enter a spelling to check: ")
if user_word in corrector:
    print("Correct!")
else:
    corrected_word = corrector.correction(user_word)
    print("Correct word is: " + corrected_word)
