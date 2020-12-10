from typing import List


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:

        pre_csum,pre_ecsum = [],[]
        suf_csum,suf_ecsum = [],[]

        n = len(nums)
        t_sum,e_tsum = sum(nums),sum([n for i,n in enumerate(nums) if i % 2 == 0])

        csum,ecsum = 0,0
        for i in range(n):
            suf_csum.append(t_sum - csum)
            csum += nums[i]
            pre_csum.append(csum)

            suf_ecsum.append(e_tsum - ecsum)
            if i % 2 == 0:
                ecsum += nums[i]
            pre_ecsum.append(ecsum)


        res = 0
        for i in range(n):

            le_ecsum = pre_ecsum[i] - nums[i]
            ri_ecsum = suf_csum[i] - suf_ecsum[i]
            ecsum_i = le_ecsum + ri_ecsum

            le_ocsum = pre_csum[i] - pre_ecsum[i]
            ri_ocsum = suf_ecsum[i] - nums[i]
            ocsum_i = le_ocsum + ri_ocsum

            if ecsum_i == ocsum_i:
                res += 1

        return res

nums = [2,1,6,4]
nums = [1,1,1]
nums = [1,2,3]
print(Solution().waysToMakeFair(nums))