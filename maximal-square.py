from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        res = 0
        f = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    f[i][j] = 0
                else:
                    if i != 0 and j != 0:
                        f[i][j] = min(f[i-1][j],f[i][j-1],f[i-1][j-1]) + 1
                    else:
                        f[i][j] = 1
                # update results
                if f[i][j] > res:
                    res = f[i][j]

        return res ** 2

test = [
    ['1','0','1','0','0'],
    ['1','0','1','1','1'],
    ['1','1','1','1','1'],
    ['1','0','0','1','0']
]
test = [['1','1','1','0','0']]
test = [
    ['1'],
    ['1'],
    ['0'],
    ['1']
]
test = [['1']]
test = []
sol = Solution()
res = sol.maximalSquare(test)
print(res)