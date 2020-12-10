from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n1,n2 = len(nums1),len(nums2)
        max_res = []
        for k1 in range(k+1):
            k2 = k - k1
            if k1 > n1 or k2 > n2: continue
            sub1 = self.get_max_k_subseq(nums1,n1-k1)
            sub2 = self.get_max_k_subseq(nums2,n2-k2)
            res = self.merge(sub1,sub2)
            max_res = max(max_res,res)
        return max_res

    def get_max_k_subseq(self,nums,k):
        # k is the number of digits to pop
        stack = []
        i,j = 0,k
        while i < len(nums):
            while j and stack and nums[i] > stack[-1]:
                stack.pop()
                j -= 1
            stack.append(nums[i])
            i += 1
        return stack[:len(nums)-k]

    def merge(self,seq1,seq2):
        res = []
        while seq1 or seq2:
            bigger_seq = seq1 if seq1 > seq2 else seq2
            res.append(bigger_seq[0])
            bigger_seq.pop(0)
        return res

nums2 = [9, 1, 2, 5, 8, 3]
nums1 = [3, 4, 6, 5]
nums1 = [6, 7]
nums2 = [6, 0, 4]
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
nums1 = [1,2]
nums2 = []
k = 2
print(Solution().maxNumber(nums1,nums2,k))