# Find the maximum size of sub array of size k in the given array

import array as arr


def max_sum_subarray(arr, k):
    max_sum = 0
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(1, len(arr) - k + 1):
        window_sum += arr[i + k - 1] - arr[i - 1] # Slide the window, include one new element, remove one old element
        max_sum = max(max_sum, window_sum) # update the maximum sum
    
    return max_sum



def main():
    # We have to find a sub array of size 3 which is of maximum size.
    array1 = arr.array('i', [3, 4, 7, 8, 4, 3, 5, 1, 0, 9, 5])
    k = 3
    print(max_sum_subarray(arr=array1, k=k))


if __name__ == "__main__":
    main()

