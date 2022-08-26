# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
#
# class Solution:
#     def runningSum(self, nums):
#         result = []
#         for i in range(len(nums)):
#             result.append(sum(nums[:i + 1]))
#         return result
#
#
# s = Solution()
# print(s.runningSum([1, 2, 3, 4]))
#
#

class Solution:
    def runningSum(self, nums):
        return [sum(nums[:i + 1]) for i in range(len(nums))]


s = Solution()
print(s.runningSum([1, 2, 3, 4, 5]))
