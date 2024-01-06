from difflib import SequenceMatcher

text1 = "My name is Naruto"
text2 = "Feel pain, know pain, accept pain"
sequenceScore = SequenceMatcher(None, text1, text2).ratio()

print(f'Both are {sequenceScore * 100} % similar')