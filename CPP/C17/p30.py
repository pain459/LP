 # display the contents of the current directory

import os

os.chdir('../C17')

for dirpath, dirnames, filenames in os.walk('.'):
    print(f'Current path {dirpath}')
    print(f'Directories {dirnames}')
    print(f'Files {filenames}')
