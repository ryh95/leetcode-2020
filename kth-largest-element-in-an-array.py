import heapq
class Solution:
    def findKthLargest(self, nums, k):
        q_nums = [-i for i in nums]
        heapq.heapify(q_nums)
        while k > 0:
            ans = -heapq.heappop(q_nums)
            k -= 1
        return ans

nums = [1]
k = 1
print(Solution().findKthLargest(nums,k)) 