import operator
from collections import deque
from itertools import accumulate, chain
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod = chain([1],accumulate(nums[:-1],operator.mul))
        suf_prod = reversed(deque(chain([1],accumulate(nums[:0:-1],operator.mul))))
        return [x*y for x,y in zip(pre_prod,suf_prod)]

    def productExceptSelf2(self, nums: List[int])-> List[int]:
        pre_prod = chain([1], accumulate(nums[:-1], operator.mul))
        suf_prod = chain([1], accumulate(nums[:0:-1], operator.mul))
        n = len(nums)
        res = [1] * n
        for i,(x,y) in enumerate(zip(pre_prod,suf_prod)):
            res[i] *= x
            res[n-1-i] *= y
        return res


test = [1,2,3,4]
sol = Solution()
res = sol.productExceptSelf2(test)
print(res)