student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

ranks_dict = {}

# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

for i,j in student_scores.items():
    if 91 <= j <= 100:
        ranks_dict[i] = 'Outstanding'
    elif 81 <= j <= 90:
        ranks_dict[i] = 'Exceeds Expectations'
    elif 71 <= j <= 80:
        ranks_dict[i] = 'Acceptable'
    elif j <= 70:
        ranks_dict[i] = 'Fail' 
    elif j > 100 or j < 0:
        print('Invalid entry observed.')
    elif type(j) != int:
        print('Not an integer datatype.')
    else:
        pass

print(ranks_dict)
