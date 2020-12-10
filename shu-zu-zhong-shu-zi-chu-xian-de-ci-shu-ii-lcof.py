from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        for x in c.items():
            if x[1] == 1: return x[0]