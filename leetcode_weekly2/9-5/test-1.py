from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diag_sum = 0
        for i in range(len(mat)):
            diag_sum += mat[i][i]
        for i in range(len(mat)):
            diag_sum += mat[i][len(mat)-1-i]
        if len(mat) % 2 != 0: diag_sum -= mat[len(mat)//2][len(mat)//2]
        return diag_sum

mat = [[1,2,3],
    [4,5,6],
    [7,8,9]]
# mat = [[1,1,1,1],
#     [1,1,1,1],
#     [1,1,1,1],
#     [1,1,1,1]]
mat = [[5]]

sol = Solution()
print(sol.diagonalSum(mat))