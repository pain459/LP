# using dictionary comprehension to transform or filter dictionaries

marks = {
    'a':46,
    'b':78,
    'c':90,
    'd':87,
    'e':88,
    'f':69
}

# filter the dictionary
passed_students = {student: score for student, score in marks.items() if score > 75}
print(passed_students)