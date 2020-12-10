from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1: return False
        if sum(nums) % 2 != 0: return False

        T = sum(nums) // 2
        dp = [[False for i in range(T+1)] for _ in range(len(nums))]
        # initialize
        for col in dp:
            col[0] = True
        if nums[0] <= T: dp[0][nums[0]] = True
        # iterate
        for i in range(1,len(nums)):
            for j in range(1,T+1):
                if j - nums[i] >= 0:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]

test = [1, 5, 11, 5]
# test = [1,2,3,5]
# test = [1,2,3,6,8]
# test = [1,1]
test = [9,5]
print(Solution().canPartition(test))