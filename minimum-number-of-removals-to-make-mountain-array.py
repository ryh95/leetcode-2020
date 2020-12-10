from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:

        # todo: finish and submit the code

        f = [0 for _ in range(len(nums))]
        i = 1
        while i<len(nums)-1:
            tmp = [f[j] for j in range(i) if nums[i] > nums[j]]
            if not tmp:
                f[i] = 1
            else:
                f[i] = max(tmp) + 1
            i += 1
        nums = nums[::-1]
        f.append(0)
        q = [0 for _ in range(len(nums))]
        i = 1
        while i < len(nums)-1:
            tmp = [q[j] for j in range(i) if nums[i] > nums[j]]
            if not tmp:
                q[i] = 1
            else:
                q[i] = max(tmp) + 1
            i += 1
        q.append(0)
        max_res = float('-inf')
        for i in range(len(nums)):
            max_res = max(max_res,f[i] + q[len(nums)-1-i])
        return len(nums) - max_res

nums = [2,1,1,5,6,2,3,1]
# nums = [1,3,1]
nums = [4,3,2,1,1,2,3,1]
# nums = [1,2,3,4,4,3,2,1]
print(Solution().minimumMountainRemovals(nums))