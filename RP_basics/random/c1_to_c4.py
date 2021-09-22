string1 = "Hello World!"
print(type(string1))  # This prints the type of string.
print(len("abc"))  # Finding the length of the string.
string1 = "cupcakes"
print(len(string1))  # Finding length of the string from an assigned variable.
paragraph1 = "Twinkle Twinkle little star \
             how I wonder what you are \
             up above the world so high \
             like a diamond in the sky"
print(paragraph1)

# String indexing.
flavor = "apple pie"
print(flavor[1])  # This will print P
print(flavor[-1])  # This will print last letter e
# other way to get last character.
last_char = len(flavor) - 1
print(flavor[last_char])

# String slicing - long method & clumsy
flavor = "apple pie"
first_three_letters = flavor[0] + flavor[1] + flavor[2]
print(first_three_letters)

# String slicing by using substring
flavor = "apple pie"
print(flavor[0:3])  # Should print app
# Lets play with some more.
print(flavor[:5])  # Should print apple
print(flavor[3:])  # le pie
print(flavor[-1:])  # e
print(flavor[:-1])  # apple pi
print(flavor[:])  # full string
# copying one string to other variable.
copied_flavor = flavor[:]
print(copied_flavor)

# Strings are immutable. You can assign and twist the string, but cannot change it.
word = "goal"
word = "f" + word[1:]
print(word)

# BAZINGA
word = "ZING"
word = "BA" + word[:] + "A"
print(word)

#  String manipulation
string1 = "pablo escobar cocaine"
print(string1.upper())
print(string1.title())

# Removing white spaces
name = "    Pablo Escobar Cocaine   "
print(name.lstrip())  # Remove the left empty space.
print(name.rstrip())  # Remove the right empty space.
print(name.strip())  # Remove the empty space from both sides.

# Determines if string starts or ends with a particular string.
name = "Pablo Escobar Cocaine"
print(name.startswith("Pa"))  # True
print(name.endswith("new"))  # false

#  Interact with user input.
prompt = "Hey, what's up? "
user_input = input(prompt)
print("You said:", user_input)

response = "What should I shout?"
user_input = input(response)
print("Well if you insist...", user_input.upper())

# Working with strings and numbers
num = "2"  # Python understands this as string object.
print(num + num)  # Should return "22"
print(type(num + num))  # <class 'str'>
print(num * 3)  # should print 222. Type is still str.

# converting strings to numbers
num = input("Enter a number to be doubled: ")
doubled_num = int(num) * 2
print(doubled_num)
print(type(doubled_num))

# Converting numbers to strings
user_input = eval(input("Enter the balance pan cakes: "))
pancakes_in_stock = 20
pancakes_in_stock -= user_input
print("We have " + str(pancakes_in_stock) + " pancakes remaining with us.")

# Streamlining print statements. All 3 types we know.
name = "Zaphod"
heads = 2
arms = 3
# Technical name = string interpolation.
print(name, "has", str(heads), "heads and", str(arms), "arms")
print(name + " has " + str(heads) + " heads and " + str(arms) + " arms")
print(f"{name} has {heads} heads and {arms} arms")
# Using string interpolation for some basic math.
x = 10
y = 20
print(f"{x} times {y} is {x*y}")  # f strings are advanced. Stick to this.
# Using format which is before 3.6
print("{} times {} is {}".format(x, y, x * y))

# Finding string in a string
phrase = "the surprise is in here somewhere"
print(phrase.find('is'))  # Only replies the first occurrence.
print(phrase.find('x'))  # If the string is not available, it will reply -1.
my_number = 9966255052
print(my_number.find(5))  # Cannot find the location of number.
my_number = "9966255052"
print(my_number.find("5"))  # Works as the search type is string.
# Now we will play with replace.
my_story = "I'm telling you the truth; nothing but the truth!"
print(my_story.replace("the truth", "lies"))
print(my_story)  # Yeah, we will get the base string due to immutability
# Use multiple replace statements to replace text multiple times.
text = "some of the stuff"
new_text = text.replace("some of", "all")
new_text = new_text.replace("stuff", "things")
print(new_text)

# Code challenge 4.9
user_input = input("Enter the string to be converted to leetspeak: ")
c_string = user_input.replace("a", "4")
c_string = c_string.replace("b", "8")
c_string = c_string.replace("e", "3")
c_string = c_string.replace("l", "1")
c_string = c_string.replace("o", "0")
c_string = c_string.replace("s", "5")
c_string = c_string.replace("t", "7")
print(c_string)

