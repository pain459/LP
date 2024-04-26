# using memoization technique to find the longest increasing sub-sequence in the given list.
def length_of_lis(nums):
    memo = {}
    
    def lis_helper(prev_index, current_index):
        if current_index == len(nums):
            return 0
        
        if (prev_index, current_index) in memo:
            return memo[(prev_index, current_index)]
        
        without_current = lis_helper(prev_index, current_index + 1)
        
        if prev_index == -1 or nums[current_index] > nums[prev_index]:
            with_current = 1 + lis_helper(current_index, current_index + 1)
        else:
            with_current = 0
            
        memo[(prev_index, current_index)] = max(without_current, with_current)
        return memo[(prev_index, current_index)]
    
    return lis_helper(-1, 0)

# Example usage
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(length_of_lis(nums))  # Output: 4 (the LIS is [2, 3, 7, 101])

