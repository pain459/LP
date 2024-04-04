# to view the contents of the zipped files
from zipfile import *

# open a zip file
z = ZipFile('test.zip', 'r')

# Extract all the file names which are in a zip file
z.extractall()