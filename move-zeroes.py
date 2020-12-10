from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j = 0,0
        while j < len(nums):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            j += 1
        while i < len(nums):
            nums[i] = 0
            i += 1

test = [0,1,0,3,12]
test = [1]
Solution().moveZeroes(test)
print(test)