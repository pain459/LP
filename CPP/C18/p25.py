# Retrieve data from the file using regular expressions

import re
# Open the files
f1 = open('salaries.txt', 'r')
f2 = open('newfile.txt', 'w')

# repeat for each line for the file f1
for line in f1:
    res1 = re.search(r'\d{1}', line)
    res2 = re.search(r'\$\d{4,}', line)
    f2.write(res1.group()+'\t')  # write id no into f2
    f2.write(res2.group()+'\n')  # write salary into f2

# Close the files
f1.close()
f2.close()