from collections import Counter
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a,k = Counter(nums),0
        for i in [0,1,2]:
            while a[i] != 0:
                nums[k] = i
                k += 1
                a[i] -= 1

nums = []
Solution().sortColors(nums)
print(nums)