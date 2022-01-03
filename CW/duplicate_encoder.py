def duplicate_encode(word):
    encoded_word = ""
    for i in word.lower():
        if word.count(i) > 1:
            encoded_word += ")"
        elif word.count(i) == 1:
            encoded_word += "("
        else:
            pass
    return encoded_word


print(duplicate_encode("lud DfYJdulFZxJVC(LV(hhB@lTf(kSH!(iv"))
