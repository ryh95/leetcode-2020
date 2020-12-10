import heapq
from collections import deque
from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        # p_end = len(nums) - k
        # i, res = 0, deque()
        # num_id = 0
        # while i < k:
        #     num_id = min(range(num_id, p_end + i + 1), key=lambda x: nums[x])
        #     res.append(nums[num_id])
        #     num_id += 1
        #     i += 1
        # return list(res)
        stack = []
        i,j = 0,len(nums) - k
        while i < len(nums):
            while j > 0 and stack and stack[-1] > nums[i]:
                stack.pop()
                j -= 1
            stack.append(nums[i])
            i += 1
        return stack[:k]





# nums = [3,5,2,6]
# k = 2
# nums = [2,4,3,3,5,4,9,6]
# k = 4
# nums = [71,18,52,29,55,73,24,42,66,8,80,2]
# k = 3
nums = [84,10,71,23,66,61,62,64,34,41,80,25,91,43,4,75,65,13,37,41,46,90,55,8,85,61,95,71]
k = 24
print(Solution().mostCompetitive(nums,k))


