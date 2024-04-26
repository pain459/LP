# List of dictionaries representing students
students = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 20},
    {'name': 'Charlie', 'age': 22}
]

# Using sorted to sort by age
sorted_students = sorted(students, key=lambda x: x['age'])

print(sorted_students)