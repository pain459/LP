# Bubble sort implementation in python

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


test_array = [64, 34, 25, 12, 22, 11, 90]
bubble_sorted_array = bubble_sort(test_array)

print(bubble_sorted_array)