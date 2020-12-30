import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-e for e in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            a1,a2 = heapq.heappop(stones),heapq.heappop(stones)
            if a1 != a2:
                heapq.heappush(stones,a1-a2)
        if not stones: return 0
        return -stones[0]

test = [2,7,4,1,8,1]
# test = [2]
print(Solution().lastStoneWeight(test))
