from collections import OrderedDict
from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        i = 0
        nums.append(float('inf'))
        res = True
        while i < len(nums) - 1:
            sub_nums = []
            while True:
                sub_nums.append(nums[i])
                if nums[i+1] - nums[i] > 1:
                    break
                i += 1
            i += 1
            res = res and self.__isPossible(sub_nums)
            if not res: return False
        return res


    def __isPossible(self,nums):
        C = OrderedDict()
        for n in nums:
            if n in C:
                C[n] += 1
            else:
                C[n] = 1
        s = 0
        vals = list(C.keys())
        while s < len(C) and C[vals[s]] != 0:
            p, is_first, need_break = s, True, False
            l = 0
            while p < len(C):
                if p != len(C) - 1 and C[vals[p]] > 1 and C[vals[p + 1]] < C[vals[p]] and l >= 2:
                    need_break = True
                C[vals[p]] -= 1
                if C[vals[p]] == -1: return False
                if C[vals[p]] > 0 and is_first: s, is_first = p, False
                p += 1
                l += 1
                if need_break: break
            if l < 3: return False
        return True

test = [1,2,3,3,4,5] # True
# test = [1,2,3,4,4,5] # False
# test = [1,2,3,3,4,4,5,5] # True
# test = [1,2,3,4] # True
# test = [1,2,3,3,3,4,4,5] # False
# test = [1] # False
# test = [1,8,9,10,11,12,13,14,15,16] # False
# test = [1,2,3,4,6,7,8,9,10,11] # True
print(Solution().isPossible(test))