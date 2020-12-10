from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums = [float('-inf')] + nums + [float('inf')]
        n = len(nums)
        i,j = 0,n-1
        while i < n - 1 and nums[i + 1] >= nums[i]:
            i += 1
        while j > 0 and nums[j - 1] <= nums[j]:
            j -= 1
        if i >= j: return 0
        min_ij,max_ij = min(nums[i:j]),max(nums[i:j])
        while i > 0 and min_ij < nums[i-1]:
            min_ij = min(min_ij, nums[i-1])
            i -= 1
        while j < n-1 and max_ij > nums[j]:
            max_ij = max(max_ij, nums[j])
            j += 1
        return j - i

test = [2, 6, 4, 8, 10, 9, 15]
test = [1,2,1]
# test = [2,6,5,9]
test = [2,3,3,2,4]
print(Solution().findUnsortedSubarray(test))