from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1],[1,1]]
        i,pre = 0,[1,1]
        res = [[1],[1,1]]
        while i < numRows - 2:
            pre = [1] + [pre[j] + pre[j+1] for j in range(len(pre)-1)] + [1]
            res.append(pre)
            i += 1
        return res

n = 5
print(Solution().generate(n))