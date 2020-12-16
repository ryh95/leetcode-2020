from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # todo: do this problem again later
        nums.sort(reverse=True)
        l = len(nums) // 2
        nums[::2],nums[1::2] = nums[l:],nums[:l]

nums = [1, 5, 1, 1, 6, 4]
# nums = [1,2,4,4,4,6]
nums = [1,2,3]
Solution().wiggleSort(nums)
print(nums)