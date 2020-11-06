from math import inf
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j,max_area = 0,len(height) - 1,0
        while i != j:
            area = min(height[i],height[j]) * (j - i)
            if area > max_area: max_area = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area

test = [1,2]
max_area = Solution().maxArea(test)
print(max_area)