'''
1. Reverse an Array
   Given an array, reverse its elements in-place without using extra space.
   - Concepts: Arrays, Two-Pointer Technique
'''

def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


# Example usage
arr = [1, 2, 3, 4, 5]
print(reverse_array(arr=arr))
