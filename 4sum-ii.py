from typing import List
from collections import Counter


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        sum_ab,sum_cd = Counter(),Counter()
        for i,a in enumerate(A):
            for j,b in enumerate(B):
                sum_ab[a+b] += 1
        for i, c in enumerate(C):
            for j, d in enumerate(D):
                sum_cd[c + d] += 1
        res = 0
        for k in sum_ab.keys():
            if -k in sum_cd:
               res += sum_ab[k]*sum_cd[-k]
        return res

A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
print(Solution().fourSumCount(A,B,C,D))