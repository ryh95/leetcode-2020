from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res,self.ress,self.n = [],[],n
        self.array = list(range(1,n+1))
        self.combine_at_id(0,k)
        return self.ress

    def combine_at_id(self,i,k):
        if self.n - i < k: return # 剪枝
        if k == 0:
            self.ress.append(self.res[:])
            return
        while i < self.n:
            self.res.append(self.array[i])
            self.combine_at_id(i+1,k-1)
            self.res.pop()
            i += 1

n,k = 4,3
n,k = 4,2
print(Solution().combine(n,k))