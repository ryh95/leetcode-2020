from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1: return [nums]
        cur_ress = []
        for n in set(nums):
            nums.remove(n)
            next_ress = self.permuteUnique(nums)
            cur_ress += [[n] + res for res in next_ress]
            nums.append(n)
        return cur_ress

test = [1,1,2]
test = [1]
test = [1,1,2,2,3,3]
print(Solution().permuteUnique(test))

