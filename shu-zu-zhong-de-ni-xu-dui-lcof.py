from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums: return 0
        self.nums = nums
        res,_ = self.helper(0,len(nums))
        return res

    def helper(self,s,e):
        if e - s == 1: return 0,[self.nums[s]]
        m = s + (e-s) // 2
        res_left,merged_left = self.helper(s,m)
        res_right,merged_right = self.helper(m,e)
        res_merge,merged_l = self.merge(merged_left,merged_right)
        return res_left+res_right+res_merge,merged_l

    def merge(self,l1,l2):
        m,n = len(l1),len(l2)
        i,j = 0,0
        res,merged_l = 0,[]
        while i < m:
            if l1[i] > l2[j]:
                res += m-i
                merged_l.append(l2[j])
                j += 1
            else:
                merged_l.append(l1[i])
                i += 1
            if j == n: break
        while j < n:
            merged_l.append(l2[j])
            j += 1
        while i < m:
            merged_l.append(l1[i])
            i += 1
        return res,merged_l

test = [7,5,6,4]
test = [7,4,5]
# test = [7]
print(Solution().reversePairs(test))