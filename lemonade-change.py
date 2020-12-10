from collections import Counter
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        c = Counter()
        for b in bills:
            if b == 5:
                c[5] += 1
            elif b == 10:
                c[5] -= 1
                c[10] += 1
            elif b == 20:
                if c[10] > 0:
                    c[10] -= 1
                    c[5] -= 1
                else:
                    c[5] -= 3
            if c[5] < 0: return False
        return True

tests = [
    [5,5,5,5,10,5,10,10,10,20],
    [5,5,5,10,20],
    [5,5,10],
    [10,10],
    [5,5,10,10,20],
    [5,5,5,5,20,20,5,5,5,5],
]
for test in tests:
    print(Solution().lemonadeChange(test))

