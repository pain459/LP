# find vowels in the given string.

def getCount(inputStr):
    return sum(1 for i in inputStr if i in 'aeiouAEIOU')

user_input = str(input('Enter a string to calculate vowels in it: '))
result = getCount(user_input)
print(result)