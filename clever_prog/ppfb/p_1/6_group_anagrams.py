# This program will group the words that are anagrams. We are using default dict library to solve this problem.

from collections import defaultdict


def _group_anagrams(a):
    dfdict = defaultdict(list)
    for i in a:
        sorted_i = "".join(sorted(i))
        dfdict[sorted_i].append(i)
    return dfdict


if __name__ == "__main__":
    words = ["tea", "eat", "bat", "ate", "arc", "car"]
    print(_group_anagrams(words))
