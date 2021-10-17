import pickle
D = {'a': 1, 'b': 2}
F = open('datafile.pkl', 'wb')
pickle.dump(D, F)  # dump data into file
F.close()

F = open('datafile.pkl', 'rb')
E = pickle.load(F)
E  # {'a': 1, 'b': 2}

open('datafile.pkl', 'rb').read()
# b'\x80\x04\x95\x11\x00\x00\x00\x00\x00\x0.... binary reply...
