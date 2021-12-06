# Restricting the use of straight forward functions.

student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
heights_int = []
for i in student_heights:
    heights_int.append(int(i))

total = 0
total_entries = 0
for i in heights_int:
    total += i
    total_entries += 1

print(
    f'Average height is {round(total/total_entries)} for {total_entries} entries.')
