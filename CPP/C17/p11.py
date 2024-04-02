import p10, pickle

# Open emp.dat file as a binary file for writing.
f = open('emp.dat', 'wb')
n = int(input('How many employees? '))

for i in range(n):
    id = int(input('Enter ID: '))
    name = input('Enter name: ')
    sal = float(input('Enter salary: '))

    # Create Emp class object
    e = p10.Emp(id, name, sal)

    # Store the object 2 into the file f
    pickle.dump(e, f)

# Close the file.
f.close()