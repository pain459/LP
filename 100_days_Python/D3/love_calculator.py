from os import name


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1, name2 = name1.lower(), name2.lower()

# find matches for TRUE in name1
# find matches for LOVE in name2
n1_count = 0
n2_count = 0
n1_count = name1.count('t') + name1.count('r') + \
    name1.count('u') + name1.count('e') + name2.count('t') + name2.count('r') + \
    name2.count('u') + name2.count('e')
n2_count = name2.count('l') + name2.count('o') + \
    name2.count('v') + name2.count('e') + name1.count('l') + name1.count('o') + \
    name1.count('v') + name1.count('e')

love_score = str(n1_count) + str(n2_count)
love_score = int(love_score)

if love_score < 10 or love_score > 90:
    print(f'Your score is {love_score}, you go together like coke and mentos.')
elif 50 > love_score > 40:
    print(f'Your score is {love_score}, you are alright together.')
else:
    print(f'Your score is {love_score}.')

# Pierre Curie
# Marie Curie
