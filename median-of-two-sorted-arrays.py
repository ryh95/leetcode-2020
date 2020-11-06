from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n = len(nums1), len(nums2)
        if (m + n) % 2 == 0:
            self.is_even = 1
        else:
            self.is_even = 0
        if self.is_even:
            return self.helper((m + n) // 2 - 1, nums1, nums2)
        else:
            return self.helper((m + n) // 2, nums1, nums2)


    def helper(self,k,nums1,nums2):

        if k == 0:
            if self.is_even:
                first,second = self.get_first_two_small(nums1,nums2)
                return (first + second) / 2
            else:
                return self.get_first_small(nums1,nums2)

        if not self.is_even:
            if not nums1: return nums2[k]
            if not nums2: return nums1[k]
        else:
            if not nums1: return (nums2[k]+nums2[k+1])/2
            if not nums2: return (nums1[k]+nums1[k+1])/2

        i = min((k + 1) // 2, len(nums1), len(nums2)) - 1
        if nums1[i] <= nums2[i]:
            nums1 = nums1[i + 1:]
        else:
            nums2 = nums2[i + 1:]
        k = k - i - 1
        return self.helper(k,nums1,nums2)


    def get_first_two_small(self,n1,n2):
        if not n1: return n2[:2]
        if not n2: return n1[:2]
        first = n1[0] if n1[0] < n2[0] else n2[0]
        if first == n1[0]:
            if len(n1) >= 2:
                second = min(n2[0],n1[1])
            else:
                second = n2[0]
        else:
            if len(n2) >= 2:
                second = min(n2[1], n1[0])
            else:
                second = n1[0]
        return first,second

    def get_first_small(self,n1,n2):
        if not n1: return n2[0]
        if not n2: return n1[0]
        return min(n1[0],n2[0])

m = [0,0,0,0,0]
n = [-1,0,0,0,0,0,1]

# m = [1,2]
# n = [1,2,3]
print(Solution().findMedianSortedArrays(m,n))