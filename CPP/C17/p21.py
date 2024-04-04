# zipping the contents of file
from zipfile import *

# Create zip file
f = ZipFile('test.zip', 'w', ZIP_DEFLATED)

# add some file. These are zipped
f.write('cities.bin')
f.write('copy.png')

# close the zip file
print('test.zip file created..')
f.close()