import math
from typing import List


class Solution:
    # def minOperations(self, nums: List[int], x: int) -> int:

        # self.f = {}
        # self.nums = nums
        # self.n = len(nums)
        # res = self.helper(0,len(nums)-1,x)
        # if math.isinf(res):
        #     return -1
        # return res

    # def helper(self,i,j,x):
    #
    #     if x == 0: return 0
    #     # if i > j: return float('inf')
    #     if x < 0 or i > j: return float('inf')
    #
    #
    #     if '_'.join([str(i),str(j),str(x)]) in self.f:
    #         return self.f['_'.join([str(i),str(j),str(x)])]
    #
    #     case1 = self.helper(i+1,j,x-self.nums[i])
    #     case2 = self.helper(i,j-1,x-self.nums[j])
    #     self.f['_'.join([str(i),str(j),str(x)])] = min(case1,case2) + 1
    #
    #     return self.f['_'.join([str(i),str(j),str(x)])]

    def minOperations(self, nums: List[int], x: int) -> int:

        target = sum(nums) - x
        if target < 0: return -1
        i,j,cur_sum,max_len = 0,0,0,float('-inf')
        while j < len(nums):

            cur_sum += nums[j]
            j += 1
            if cur_sum >= target:
                # shrink i
                while i < j and cur_sum > target:
                    cur_sum -= nums[i]
                    i += 1
                cur_len = j - i
                if cur_sum == target: max_len = max(max_len,cur_len)

        if math.isinf(max_len): return -1
        return len(nums) - max_len

# nums = [1,1,4,2,3]
# x = 5
# 2
# nums = [5,6,7,8,9]
# x = 4
# -1
# nums = [3,2,20,1,1,3]
# x = 10
# 5
# nums = [1,1]
# x = 3
# -1
# nums = [5,2,3,1,1]
# x = 5
# 1
# nums = [8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309]
# x = 134365
# 16
nums = [6016,5483,541,4325,8149,3515,7865,2209,9623,9763,4052,6540,2123,2074,765,7520,4941,5290,5868,6150,6006,6077,2856,7826,9119]
x = 31841

print(Solution().minOperations(nums,x))