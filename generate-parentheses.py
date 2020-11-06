from typing import List


class Solution:
    def generateParenthesis2(self, n: int) -> List[str]:
        if n == 0: return ['']
        return list(self.gP(n))

    def gP(self, n):
        if n == 1: return {'()'}
        res = self.gP(n-1)
        return {'(' + s + ')' for s in res} | {'()' + s for s in res} | {s + '()' for s in res}

    def generateParenthesis(self, n: int) -> List[str]:
        p = [['']]
        for j in range(1,n+1):
            f = [[] for _ in range(j+1)]
            for i in range(j+1):
                if i == 0: f[i] = [')' + s for s in p[i]]
                if i != j: f[i] = ['(' + s for s in f[i-1]] + [')' + s for s in p[i]]
                else: f[i] = ['(' + s for s in f[i-1]]
            p = f
            del f
        return p[-1]


res = Solution().generateParenthesis(4)
print(res)