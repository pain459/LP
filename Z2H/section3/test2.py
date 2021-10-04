# we are testing something with lists

string1 = "Geneva is active and ready"
status_of_geneva = string1.split()[2::2]
verification = ['active', 'ready']
if verification == status_of_geneva:
    print("Geneva is up and running")
else:
    print("Geneva is not running. Please check")
