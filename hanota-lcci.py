from typing import List

import sys

sys.setrecursionlimit(1000000)

class Solution:

    def __init__(self):
        self.finish = False
        self.arrived_states = set()

    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        # todo: reduce the running time
        """
        Do not return anything, modify C in-place instead.
        """
        self.finish_state = A[:]
        self.solve_hanota(A,B,C)
        # print(C)

    def solve_hanota(self, A: List[int], B: List[int], C: List[int]):

        if C == self.finish_state:
            self.finish = True
            return self.finish
        cur_state = (tuple(A),tuple(B),tuple(C))
        # cur_state = '|'.join([' '.join([str(i) for i in l]) for l in [A, B, C]])
        if cur_state in self.arrived_states:
            return self.finish

        self.arrived_states.add(cur_state)
        for pop_id,pop_l in enumerate([A,B,C]):
            if pop_l:
                item = pop_l.pop()
                for append_id,append_l in enumerate([A,B,C]):
                    if pop_id != append_id:
                        if not append_l or append_l[-1] > item:
                            append_l.append(item)
                            if self.solve_hanota(A, B, C): return self.finish
                            append_l.pop()
                pop_l.append(item)


A,B,C = [5,4,3,2,1,0], [], []
sol = Solution()
sol.hanota(A,B,C)