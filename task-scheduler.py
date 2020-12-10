from collections import Counter
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # todo: give a better solution
        c = Counter(tasks)
        q = [(-x[1],x[0]) for x in c.items()]
        heapify(q)
        res = 0
        while q:
            s = len(q)
            es = [heappop(q)[1] for _ in range(min(s,n+1))]
            for e in es:
                c[e] -= 1
                if c[e] > 0: heappush(q,(-c[e],e))
            res += n + 1 if q else s
        return res

tasks = ["A","A","A","B","B","B"]
n = 2
tasks = ["A","A","A","B","B","B"]
n = 0
tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
tasks = ["A"]
n = 4
print(Solution().leastInterval(tasks,n))