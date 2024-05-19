def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2 # Finding midway of the array
        L = arr[:mid]  # Dividing the elements into 2 halves
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr



example_array = [38, 27, 43, 3, 9, 82, 10]
sorted_array = merge_sort(example_array.copy())  # Using copy to avoid in-place sorting
print("Sorted array:", sorted_array)