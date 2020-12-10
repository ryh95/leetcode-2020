class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i - 1 < 0 and j - 1 < 0:
                    f[i][j] = 1
                elif i - 1 < 0:
                    f[i][j] = f[i][j-1]
                elif j - 1 < 0:
                    f[i][j] = f[i-1][j]
                else:
                    f[i][j] = f[i][j-1] + f[i-1][j]
        return f[-1][-1]

m = 3
n = 7
m = 7
n = 3
m = 3
n = 3
m = 1
n = 1
print(Solution().uniquePaths(m,n))