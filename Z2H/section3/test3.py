# Checking if maximum members are attending the class

actual_students = "abcdfghijklnopqrstuvwxyz"
actual_students = list(actual_students)
print('----')
print('Actual list of students below')
print(actual_students)
attended_students = "abcgilmopqtvwyz"
attended_students = list(attended_students)
print('Actual attended students')
print(attended_students)

if len(attended_students) / len(actual_students) >= len(actual_students) / 2:
    print('Atleast half of the students attended the class')
else:
    print('Thin audience')
