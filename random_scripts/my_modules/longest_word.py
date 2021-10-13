def long_word(s):
    longest = max(s.split(), key=len)
    return longest


if __name__ == "__main__":
    s = "be confident and be yourself"
    long_word(s)
