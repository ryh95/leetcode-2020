from collections import Counter
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if not nums: return 0
        c = Counter()
        for n in nums:
            c[n] = c[n-1] + 1
        return max(c.values())

nums = [100,4,200,1,3,2]
nums = [1,2,0,1]
# nums = [0,3,7,2,5,8,4,6,0,1]
# nums = [1]
print(Solution().longestConsecutive(nums))