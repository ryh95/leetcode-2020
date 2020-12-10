from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.nums = nums
        res,_ = self.helper(0,len(nums))
        return res

    def helper(self,l,h):
        # obtain result on [l,h)
        if l == h: return 0,[]
        if h - l == 1: return 0,[self.nums[l]]
        mid = l + (h-l) // 2
        res_l,sorted_l = self.helper(l,mid)
        res_r,sorted_r = self.helper(mid,h)
        res_merge,merged = self.merge(sorted_l,sorted_r)
        return res_l + res_r + res_merge,merged

    def merge(self,l_list,r_list):
        haf_l_list = [i / 2 for i in l_list]
        n_l,n_r = len(haf_l_list),len(r_list)
        res,merged_list = 0,[]
        i, j = 0, 0
        while i < n_l and j < n_r:
            # calculate the result
            if haf_l_list[i] > r_list[j]:
                res += n_l - i
                j += 1
            else:
                i += 1
        i, j = 0, 0
        while i < n_l and j < n_r:
            # obtain merged list
            if l_list[i] < r_list[j]:
                merged_list.append(l_list[i])
                i += 1
            else:
                merged_list.append(r_list[j])
                j += 1
        while i < n_l:
            merged_list.append(l_list[i])
            i += 1
        while j < n_r:
            merged_list.append(r_list[j])
            j += 1
        return res,merged_list

test = [1,3,2,3,1]
test = []
# test = [2,4,3,5,1]
print(Solution().reversePairs(test))