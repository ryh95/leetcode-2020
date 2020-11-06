import heapq
class KthLargest:

    def __init__(self, k, nums):
        
        self.nums = nums
        heapq.heapify(self.nums)
        self.n = len(nums)
        self.k = k
        while self.n > k:
            heapq.heappop(self.nums)
            self.n -= 1

    def add(self, val: int) -> int:
        if self.n == self.k - 1:
            heapq.heappush(self.nums,val)
            self.n += 1
            return self.nums[0]
        if val < self.nums[0]: return self.nums[0]
        heapq.heappop(self.nums)
        heapq.heappush(self.nums,val)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
nums = []
k = 1
vals = [-3,-2,-4,0,4]
obj = KthLargest(k, nums)
print(obj.nums)
for val in vals:
    print(obj.add(val))
    print(obj.nums)