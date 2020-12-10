from typing import List


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        # todo: finish it later

        d_ab,d_bc = abs(a-b),abs(b-c)
        if d_ab == 1 and d_bc == 1: return [0,0]
        if d_ab == 1 or d_bc == 1: return [1,max(d_ab,d_bc) - 1]
        return [2,d_ab + d_bc - 2]