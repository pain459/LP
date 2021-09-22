# Challenge
# Define a function, enrollment_stats(), that takes, as an input, a list of
# lists where each individual list contains three elements: (a) the name
# of a university, (b) the total number of enrolled students, and (c) the
# annual tuition fees.
# enrollment_stats() should return two lists: the first containing all of
# the student enrollment values and the second containing all of the
# tuition fees.
# Next, define a mean() and a median() function. Both functions should
# take a single list as an argument and return the mean and median of
# the values in each list.
# Using universities, enrollment_stats(), mean(), and median(), calculate
# the total number of students, the total tuition, the mean and median
# of the number of students, and the mean and median tuition values.
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(list_of_universities):
    total_students = []
    total_tuition = []
    for i in list_of_universities:
        total_students.append(i[1])
        total_tuition.append(i[2])
    return total_students, total_tuition



def mean(values):
    return sum(values) / len(values)

def median(values):
    values.sort()
    if len(values) % 2 == 1:
        center_index = int(len(values) / 2)
        return values[center_index]
    else:
        left_center_index = (len(values) - 1) // 2
        right_center_index = (len(values) + 1) // 2
        return mean([values[left_center_index], values[right_center_index]])

totals = enrollment_stats(universities)

print("\n")
print("*****" * 6)
print(f"Total students:   {sum(totals[0]):,}")
print(f"Total tuition:  $ {sum(totals[1]):,}")
print(f"\nStudent mean:     {mean(totals[0]):,.2f}")
print(f"Student median:   {median(totals[0]):,}")
print(f"\nTuition mean:   $ {mean(totals[1]):,.2f}")
print(f"Tuition median: $ {median(totals[1]):,}")
print("*****" * 6)
print("\n")