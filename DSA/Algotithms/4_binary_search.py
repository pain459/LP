# Binary search implemetation in Python

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == target:
            return mid  # Return the index of the target
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


# Example usage.
example_array = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target_value = 9
result_index = binary_search(arr=example_array, target=target_value)
print(f'Index of target is: {result_index}')
