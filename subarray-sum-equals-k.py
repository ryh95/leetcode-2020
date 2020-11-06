from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum2id,pre_sum,res = defaultdict(set),0,0
        sum2id[0].add(-1)
        for i in range(len(nums)):
            pre_sum += nums[i]
            if pre_sum - k in sum2id: res += len(sum2id[pre_sum - k])
            sum2id[pre_sum].add(i)
        return res

nums = [1,1,1]
nums = [1,-1,1]
k = 0
sol = Solution()
res = sol.subarraySum(nums,k)
print(res)