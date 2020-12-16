import bisect
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for l in matrix:
            pos = bisect.bisect_left(l,target)
            if pos < len(l) and l[pos] == target:
                return True
        return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5

# matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# target = 20

print(Solution().searchMatrix(matrix,target))

