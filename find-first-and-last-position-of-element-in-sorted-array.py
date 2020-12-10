from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        return [self.bisect_left(nums,target),self.bisect_right(nums,target)-1]

    def bisect_left(self,nums,target):
        # search the lower bound of >=
        l, h = 0, len(nums)
        while l < h:
            mid = l + (h - l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                h = mid
        return l if nums and l < len(nums) and nums[l] == target else -1

    def bisect_right(self,nums,target):
        # search the lower bound of >
        l, h = 0, len(nums)
        while l < h:
            mid = l + (h - l) // 2
            # the following line is different with the previous code
            if nums[mid] <= target:
                l = mid + 1
            else:
                h = mid
        return l if nums and l <= len(nums) and nums[l-1] == target else 0


# nums = [5,7,7,8,8,10]
# target = 8
nums = [2,2]
target = 3
# nums = [5,7,7,8,8,10]
# target = 6
# nums = []
# target = 0
print(Solution().searchRange(nums,target))