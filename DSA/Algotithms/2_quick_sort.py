# Quick sort implementation in Python

def quick_sort(arr):
    if len(arr) <= 1:
        return arr 
    else:
        # Using the last element as pivot
        pivot = arr.pop()
        less = []
        greater = []

        for x in arr:
            if x <= pivot:
                less.append(x)
            else:
                greater.append(x)
        return quick_sort(less) + [pivot] + quick_sort(greater)

example_array = [99, 78, 55, 23, 43, 67, 88]
sorted_array = quick_sort(arr=example_array)
print(f'Sorted array: {sorted_array}')