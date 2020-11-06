from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.res,self.ress = [-1 for _ in range(n)],[]
        self.visited_cols,self.visited_diags1,self.visited_diags2 = set(),set(),set()
        self.solve_at_row(0)
        return self.ress

    def solve_at_row(self,r):
        if r == self.n:
            self.ress.append(self.print_res(self.res))
            return
        for i in range(self.n):
            if not self.is_col_valid(r,i): continue
            self.res[r] = i
            self.visited_cols.add(i)
            self.visited_diags1.add(r + i)
            self.visited_diags2.add(r - i)
            self.solve_at_row(r+1)
            self.visited_cols.remove(i)
            self.visited_diags1.remove(r + i)
            self.visited_diags2.remove(r - i)

    def is_col_valid(self, row, col):
        if col in self.visited_cols or \
               row + col in self.visited_diags1 or row - col in self.visited_diags2: return False
        return True

    # def solve_with_feasible_set(self, n, feasible_set):
    #     if n == 0 and not feasible_set:
    #         self.ress.append(self.res[:])
    #     for poss_moves in feasible_set:
    #         self.res.append(poss_moves)
    #         next_feasible_set = feasible_set - set([poss_moves,poss_moves-1,poss_moves+1])
    #         self.solve_with_feasible_set(n-1,next_feasible_set)
    #         self.res.pop()
    #
    # def print_ress(self):
    #     if not self.ress: return [[]]
    #     return [self.print_res(res) for res in self.ress]
    #
    def print_res(self,res):
        printed_res = []
        for r,c in enumerate(res):
            row_res = ['.' for _ in range(len(res))]
            row_res[c] = 'Q'
            printed_res.append(''.join(row_res))
        return printed_res



sol = Solution()
ress = sol.solveNQueens(3)
print(ress)