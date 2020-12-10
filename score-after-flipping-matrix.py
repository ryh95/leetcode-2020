from typing import List


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        # todo: write a better solution
        self.A = A
        self.m = len(A)
        self.n = len(A[0])
        # init,compute all scores
        rs = [self.score_row_flip(i) for i in range(self.m)]
        cs = [self.score_col_flip(i) for i in range(self.n)]
        is_row_change = True if max(rs) >= max(cs) else False
        id = max(range(self.m),key=lambda x:rs[x]) if is_row_change else max(range(self.n),key=lambda x:cs[x])
        if is_row_change:
            self.A[id] = [int(not e) for e in self.A[id]]
            rs[id] = self.score_row_flip(id)
        else:
            for i,row in enumerate(self.A):
                for j,e in enumerate(row):
                    if j == id: self.A[i][j] = int(not self.A[i][j])
            cs[id] = self.score_col_flip(id)

        # iterate
        while True:
            if is_row_change:
                cs = [self.score_col_flip(i) for i in range(self.n)]
            else:
                rs = [self.score_row_flip(i) for i in range(self.m)]
            if max(rs) <= 0 and max(cs) <= 0: break
            is_row_change = True if max(rs) >= max(cs) else False
            id = max(range(self.m), key=lambda x: rs[x]) if is_row_change else max(range(self.n), key=lambda x: cs[x])
            if is_row_change:
                self.A[id] = [int(not e) for e in self.A[id]]
                rs[id] = self.score_row_flip(id)
            else:
                for i, row in enumerate(self.A):
                    for j, e in enumerate(row):
                        if j == id: self.A[i][j] = int(not self.A[i][j])
                cs[id] = self.score_col_flip(id)
        # return score
        res = 0
        for i,row in enumerate(self.A):
            for j, e in enumerate(row):
                res += 2 ** (self.n-1-j) * e
        return res

    def score_row_flip(self,r_id):
        res = 0
        for i,e in enumerate(self.A[r_id]):
            res += 2 ** (self.n-1-i) if e == 0 else -2 ** (self.n-1-i)
        return res

    def score_col_flip(self,c_id):
        A_c = []
        for row in self.A:
            for i,e in enumerate(row):
                if i == c_id: A_c.append(e)
        return (2 ** (self.n-1-c_id)) * (self.m - 2 * sum(A_c))

test = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
print(Solution().matrixScore(test))