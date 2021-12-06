row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# print(type(position))  # str datatype
a, b = int(position[0]), int(position[1])
map[b-1][a-1] = 'X'
print(f"{row1}\n{row2}\n{row3}")
