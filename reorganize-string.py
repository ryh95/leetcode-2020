import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, S: str) -> str:
        c = Counter(S)
        _ , c1 = c.most_common(1)[0]
        if c1 > (len(S) + 1) // 2: return ''

        q = [(-x[1],x[0]) for x in c.items()]
        heapq.heapify(q)
        res = []
        while len(q) > 1:
            _ , l1 = heapq.heappop(q)
            _ , l2 = heapq.heappop(q)
            res += [l1,l2]
            c[l1] -= 1
            c[l2] -= 1
            if c[l1] > 0: heapq.heappush(q,(-c[l1],l1))
            if c[l2] > 0: heapq.heappush(q,(-c[l2],l2))
        if q:
            res.append(heapq.heappop(q)[1])
        return ''.join(res)

test = 'aba'
test = 'aaab'
print(Solution().reorganizeString(test))