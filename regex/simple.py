text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
996-625-5052
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

import re
sentence = 'Start a sentence and then bring it to an end'
#pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')

matches = pattern.finditer(text_to_search)

for match in matches:
	print(match)

# with open('data.txt', 'r', encoding='utf-8') as f:
# 	contents = f.read()
# 	matches = pattern.finditer(contents)
# 	for match in matches:
# 		print(match)

