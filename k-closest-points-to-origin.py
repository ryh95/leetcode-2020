from heapq import heappush, heappushpop, heappop
from math import sqrt
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        h = []
        for id,p in enumerate(points):
            dp = self.compute_distance(p)
            if len(h) < K:
                heappush(h,(-dp,id))
            else:
                if -dp > h[0][0]:
                    heappushpop(h,(-dp,id))
        return [points[heappop(h)[1]] for _ in range(len(h))]

    def compute_distance(self, p):
        return sqrt(p[0] ** 2 + p[1] ** 2)

points = [[1,3],[-2,2]]
K = 1
points = [[3,3],[5,-1],[-2,4]]
K = 2
print(Solution().kClosest(points,K))