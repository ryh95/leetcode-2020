import heapq
from collections import deque
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        self.matrix = matrix
        self.n = len(matrix)
        c,arrived_id,q = 1,set([(0,0)]),[]
        i,j,cur_element = 0,0,matrix[0][0]
        while c < k:
            cands = [(self.get_element(i, j + 1), i, j + 1) if (i,j+1) not in arrived_id else (float('inf'),0,0), \
                    (self.get_element(i + 1, j), i + 1, j) if (i+1,j) not in arrived_id else (float('inf'),0,0), \
                    q[0] if q else (float('inf'),0,0)]
            argmin_id = min(range(len(cands)),key=lambda x: cands[x])
            cur_element,i,j = cands[argmin_id] if argmin_id != 2 else heapq.heappop(q)
            arrived_id.add((i,j))
            for id,e in enumerate(cands):
                if (e[1],e[2]) not in arrived_id:
                    heapq.heappush(q,e)
                    arrived_id.add((e[1],e[2]))
            c += 1
        return cur_element

    def get_element(self,i,j):
        if i>self.n-1 or j>self.n-1:
            return float('inf')
        return self.matrix[i][j]

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 1

print(Solution().kthSmallest(matrix,k))