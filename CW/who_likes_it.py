"""
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Note: For 4 or more names, the number in "and 2 others" simply increases.
"""

def likes(names):
    disp_msg = []
    if len(names) >= 1:
        disp_msg.append(names)
        if len(names) == 1:
            return f'{names[0]} likes this'
        elif len(names) == 2:
            return f'{names[0]} and {names[1]} like this'
        elif len(names) == 3:
            return f'{names[0]}, {names[1]} and {names[2]} like this'
        else:
            return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'
    if len(names) == 0:
        return f'no one likes this'
    # return names


print(likes(["Alex", "Jacob", "Mark", "Max"]))