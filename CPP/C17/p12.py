# unpickle the object for deserialization
import p10, pickle

# open the file to read objects
f = open('emp.dat', 'rb')
print('Employees details: ')
while True:
    try:
        # Read objects from file f
        obj = pickle.load(f)
        # Display the contents of employee obj
        obj.display()
    except EOFError:
        print('End of file reached.')
        break
# Close the file
f.close()