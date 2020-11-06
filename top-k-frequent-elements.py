import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        klargest_kvs = heapq.nlargest(k,c.items(),lambda x:x[1])
        return [e[0] for e in klargest_kvs]

        # return [num for num, _ in Counter(nums).most_common(k)]

nums = [1,1,1,2,2,3]
k = 2
nums = [1]
k = 1
print(Solution().topKFrequent(nums,k))
