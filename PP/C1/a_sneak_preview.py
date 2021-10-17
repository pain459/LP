bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 40000, 'hardware']

print(bob[0], sue[2])  # fetch name, pay
bob[0].split()[-1]

sue[2] *= 1.25  # give sue 25% raise
sue

people = [bob, sue]
for person in people:
    print(person)

people[1][0]

for person in people:
    print(person[0].split()[-1])
    person[2] *= 1.20

for person in people: print(person[2])

# using list comprehension
pays = [person[2] for person in people]
print(pays)

# Using lambda
