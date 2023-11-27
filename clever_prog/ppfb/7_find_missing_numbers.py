# Find the missing number in the given set using python.
# Easy - Find in the sequence.
# Next - Find in the given array with scrabbled numbers.

def find_missing_numbers(range1):
    range1.sort()
    numbers = set(range1)
    length = len(range1)
    output = []
    for i in range(1, range1[-1]):
        if i not in range1:
            output.append(i)
    return output


if __name__ == "__main__":
    test_range1 = [1, 3, 4, 5, 7, 8, 10, 11, 13, 14, 15, 18, 20]
    test_range2 = [3, 5, 6, 7, 8, 9, 2]
    print(find_missing_numbers(test_range1))
    print(find_missing_numbers(test_range2))